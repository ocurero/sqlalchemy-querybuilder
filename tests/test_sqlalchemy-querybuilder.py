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


def test_simple_filter(query):
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
                      ],
    }
    filter = Filter(models, query)
    assert len(filter.querybuilder(rule).all()) == 1


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
