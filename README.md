SQLAlchemy query builder for jQuery QueryBuilder
================================================

This package implements a sqlalchemy query builder for json data generated
with (but not limited to) [jQuery QueryBuilder](http://querybuilder.js.org/).


Installation
------------


```
#!python
    pip install sqlalchemy-querybuilder

```

Quickstart
----------

Using **sqlalchemy-querybuilder** is very simple:

```
#!python

    from sqlalchemy_querybuilder import Filter
    from myapp import models, query

        rule = {
                "condition": "OR",
                "rules": [{
                            "field": "mytable.myfield",
                            "operator": "equal",
                            "value": "foo"
                            },
                        ],
        }

    myfilter = Filter(models, query)
    print(myfilter)

```

The following attributes from the rules are ignored and therefore can be omitted:

- ``id``
- ``type``
- ``input``


### WARNING ###
sqlalchemy-querybuilder does not do any kind of json validation.


Filter class
------------

``Filter`` accepts two arguments, ``models`` and ``query``:

- models - can either be a module defining classes which inherit from
  :py:func:`declarative_base` or a dict of such classes with the name of the
  tables as keys 
- query - a SQLAlchemy query object. Optionaly loaded with some entity.