SQLAlchemy query builder for jQuery QueryBuilder
================================================

[![builds.sr.ht
status](https://builds.sr.ht/~ocurero/sqlalchemy-querybuilder/.build.yml.svg)](https://builds.sr.ht/~ocurero/sqlalchemy-querybuilder/.build.yml?) [![codecov](https://codecov.io/gh/ocurero/sqlalchemy-querybuilder/branch/master/graph/badge.svg)](https://codecov.io/gh/ocurero/sqlalchemy-querybuilder)

This package implements a sqlalchemy query builder for json data
generated with (but not limited to) [`jQuery QueryBuilder`](http://querybuilder.js.org/).


Installation
------------

    #!python
        pip install sqlalchemy-querybuilder

Quickstart
----------

Using **sqlalchemy-querybuilder** is very simple:

```python

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

-   `id`
-   `type`
-   `input`

**WARNING**

sqlalchemy-querybuilder does not do any kind of json validation.

Filter class
------------

`Filter` accepts two arguments, `models` and `query`:

-   models - can either be a module defining classes which inherit from
    `declarative_base` or a dict of such classes with the name of the
    tables as keys.
-   query - a SQLAlchemy query object. Optionaly loaded with some
    entity.

Release History
---------------

0.1.3 (2020-05-10)
==================

**Improvements**

-   Use poetry for development.

**Bugfixes**

-   First release on sourcehut (bye bye bitbucket!).


0.1.2 (2017-11-19)
==================

**Bugfixes**

-   Fixed issue when models parameter was a dict() of classes.
-   Added missing test for models parameter

0.1 (2017-07-10)
================

**Improvements**

-   First release
