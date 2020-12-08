from sqlalchemy_querybuilder import Filter
from sqlalchemy_querybuilder.exceptions import TableNotFoundError
import models
import pytest


def test_model_not_found(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "field": "tableZZ.runid",
                        "operator": "equal",
                        "value": "a"
                        },
                      ],
    }
    filter = Filter(models, query)
    with pytest.raises(TableNotFoundError):
        filter.querybuilder(rule).all()


def test_attribute_error(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.invalid_attribute",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "1"
                        },
                      ],
    }
    filter = Filter(models, query)
    with pytest.raises(AttributeError):
        filter.querybuilder(rule).all()


def test_OR_simple_filter(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "1"
                      }, {
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "2"
                        },
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 2


def test_AND_simple_filter(query):
    rule = {
            "condition": "AND",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "greater",
                        "value": "1"
                      }, {
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "less",
                        "value": "3"
                        },
                      ],
    }
    filter = Filter(models, query)
    res = filter.querybuilder(rule).all()
    assert len(res) == 1
    assert res[0].parentid == 2


def test_OR_subfilter(query):
    rule = {
            "condition": "AND",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "1"
                        },
                      {
                        "condition": "OR",
                        "rules": [{
                                   "id": "category",
                                   "field": "test1.field",
                                   "type": "integer",
                                   "input": "select",
                                   "operator": "equal",
                                   "value": 1
                                  }, {
                                   "id": "category",
                                   "field": "test1.field",
                                   "type": "integer",
                                   "input": "select",
                                   "operator": "equal",
                                   "value": 2
                                  }]
                        },
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 1


def test_AND_subfilter(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "1"
                        },
                      {
                        "condition": "AND",
                        "rules": [{
                                   "id": "category",
                                   "field": "test1.parentid",
                                   "type": "integer",
                                   "input": "number",
                                   "operator": "greater",
                                   "value": "1"
                                  }, {
                                   "id": "category",
                                   "field": "test1.parentid",
                                   "type": "integer",
                                   "input": "number",
                                   "operator": "less",
                                   "value": "3"
                                  }]
                        },
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 2


def test_arity1_filter(query):
    rule = {
            "condition": "AND",
            "rules": [{
                        "id": "price",
                       "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "is_not_empty",
                        },
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 3


def test_model_map_filter(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "1"
                       },
                      {
                        "id": "price",
                        "field": "test2.childid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "2"
                       },
                      ],
    }
    filter = Filter({'test1': models.MyParentModel,
                     'test2': models.MyChildModel}, query)
    assert len(filter.querybuilder(rule).all()) == 5


def test_notfound_filter(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "0"
                        },
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 0


def test_invalid_operator(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.parentid",
                        "type": "integer",
                        "input": "number",
                        "operator": "notfound",
                        "value": "0"
                        },
                      ],
    }
    filter = Filter(models, query)
    with pytest.raises(NotImplementedError):
        filter.querybuilder(rule).all()


def test_hybrid_attribute(query):
    rule = {
            "condition": "OR",
            "rules": [{
                        "id": "price",
                        "field": "test1.childid",
                        "type": "integer",
                        "input": "number",
                        "operator": "equal",
                        "value": "1"
                        },
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 1
