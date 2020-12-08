# Welcome to sqlalchemy-querybuilder’s documentation

sqlalchemy-querybuilder is a package that implements a sqlalchemy query builder for json
rules generated with (but not limited to)
[jQuery QueryBuilder](http://querybuilder.js.org/).

[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![builds.sr.ht status](https://builds.sr.ht/~ocurero/sqlalchemy-querybuilder/.build.yml.svg)](https://builds.sr.ht/~ocurero/sqlalchemy-querybuilder/.build.yml?)
[![codecov](https://codecov.io/gh/ocurero/sqlalchemy-querybuilder/branch/master/graph/badge.svg)](https://codecov.io/gh/ocurero/sqlalchemy-querybuilder)
[![readthedocs](https://readthedocs.org/projects/sqlalchemy-querybuilder/badge/?version=latest&style=flat)](https://sqlalchemy-querybuilder.readthedocs.io/)

* Open Source: Apache 2.0 license.
* Website: <https://sr.ht/~ocurero/sqlalchemy-querybuilder/>.
* Documentation: <https://sqlalchemy-querybuilder.readthedocs.io/>.
* Repository: <https://hg.sr.ht/~ocurero/sqlalchemy-querybuilder>.

## Quick start

Parsing rules using **sqlalchemy-querybuilder** is very simple:

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

That would produce the following SQL query:

```sql
SELECT * FROM mytable WHERE mytable.myfield = 'foo'
```

The following attributes from the rules are ignored and therefore can be omitted:

-   `id`
-   `type`
-   `input`

!!! warning
    There's no rule syntax validation. Rules should be compatible with jquery
    QueryBuilder.
