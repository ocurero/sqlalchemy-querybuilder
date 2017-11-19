from sqlalchemy import or_, and_
import sqlalchemy
from sqlalchemy.ext.declarative import DeclarativeMeta
from .exceptions import TableNotFoundError
from inspect import signature
import types

OPERATORS = {'equal': lambda f, a: f.__eq__(a),
             'not_equal': lambda f, a: f.__ne__(a),
             'less': lambda f, a: f.__lt__(a),
             'greater': lambda f, a: f.__gt__(a),
             'less_or_equal': lambda f, a: f.__le__(a),
             'greater_or_equal': lambda f, a: f.__ge__(a),
             'in': lambda f, a: f.in_(a),
             'not_in': lambda f, a: f.notin_(a),
             'ends_with': lambda f, a: f.like('%' + a),
             'begins_with': lambda f, a: f.like(a + '%'),
             'contains': lambda f, a: f.like('%' + a + '%'),
             'not_contains': lambda f, a: f.notlike('%' + a + '%'),
             'not_begins_with': lambda f, a: f.notlike(a + '%'),
             'not_ends_with': lambda f, a: f.notlike('%' + a),
             'is_empty': lambda f: f.__eq__(''),
             'is_not_empty': lambda f: f.__ne__(''),
             'is_null': lambda f: f.is_(None),
             'is_not_null': lambda f: f.isnot(None),
             'between': lambda f, a: f.between(a[0], a[1])
             }


class Filter(object):

    def __init__(self, models, query, operators=None):
        if isinstance(models, types.ModuleType):
            model_dict = {}
            for attr in models.__dict__.values():
                if isinstance(attr, DeclarativeMeta):
                    try:
                        table = sqlalchemy.inspect(attr).mapped_table
                        model_dict[table.name] = attr
                    except sqlalchemy.exc.NoInspectionAvailable:
                        pass
            self.models = model_dict
        else:
            self.models = dict(models)
        self.query = query
        self.operators = operators if operators else OPERATORS

    def querybuilder(self, rules):
        query, cond_list = self._make_query(self.query, rules)
        if rules['condition'] == 'OR':
            operator = or_
        elif rules['condition'] == 'AND':
            operator = and_
        return query.filter(operator(*cond_list))

    def _make_query(self, query, rules):
        cond_list = []
        for cond in rules['rules']:
            if 'condition' not in cond:
                try:
                    model = self.models[cond['field'].split('.')[0]]
                except KeyError:
                    raise TableNotFoundError(cond['field'].split('.')[0])
                for entity in query._entities:
                    if entity.mapper.class_ == model:
                        break
                else:
                    query = query.add_entity(model)
                value = cond['value']
                operator = cond['operator']
                try:
                    field = getattr(model, cond['field'].split('.')[1])
                except AttributeError as e:
                    raise e
                if operator not in OPERATORS:
                    raise NotImplementedError
                else:
                    function = OPERATORS[operator]
                arity = len(signature(function).parameters)
                if arity == 1:
                    cond_list.append(function(field))
                elif arity == 2:
                    cond_list.append(function(field, value))
            else:
                query, cond_subrule = self._make_query(query, cond)
                if cond["condition"] == "OR":
                    operator = or_
                    if len(cond_subrule) < 0:
                        # if this subgroup has only 1 condition, append it
                        # to the parent group
                        cond_subrule.append(cond_list.pop())
                else:
                    operator = and_
                query = query.filter(operator(*cond_subrule))
        return query, cond_list
