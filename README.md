SQLAlchemy query builder for jQuery QueryBuilder
================================================

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active) [![builds.sr.ht status](https://builds.sr.ht/~ocurero/sqlalchemy-querybuilder/.build.yml.svg)](https://builds.sr.ht/~ocurero/sqlalchemy-querybuilder/.build.yml?) [![codecov](https://codecov.io/gh/ocurero/sqlalchemy-querybuilder/branch/master/graph/badge.svg)](https://codecov.io/gh/ocurero/sqlalchemy-querybuilder) [![readthedocs](https://readthedocs.org/projects/sqlalchemy-querybuilder/badge/?version=latest&style=flat)](https://sqlalchemy-querybuilder.readthedocs.io/)

This package implements a sqlalchemy query builder for json data
generated with (but not limited to) [`jQuery QueryBuilder`](http://querybuilder.js.org/).

* Open Source: Apache 2.0 license.
* Website: <https://sr.ht/~ocurero/sqlalchemy-querybuilder/>
* Documentation: <https://sqlalchemy-querybuilder.readthedocs.io/>

Quickstart
----------

Using **sqlalchemy-querybuilder** is very simple:

```python

from sqlalchemy_querybuilder import Filter
from myapp import models, query

    rules = {
            "condition": "OR",
            "rules": [{
                       "field": "mytable.myfield",
                       "operator": "equal",
                       "value": "foo"
                       },
                      ],
             }

    myfilter = Filter(models, query)
    print(myfilter.querybuilder(rules))
```
