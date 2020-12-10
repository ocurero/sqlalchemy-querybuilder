# Usage

The entirety of sqlalchemy-querybuilder’s functionality is encapsulated in the Filter class.

## Getting started

Filter class accepts three parameters:

 - `models` (required) can be either a module defining classes which inherit from
   [`declarative_base`](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/api.html#sqlalchemy.ext.declarative.declarative_base) or a dictionary of such classes with the name of the tables as keys.
 - `query` (required) is a SQLAlchemy query object. Optionaly loaded with some entity.
 - `operators` (optional) is a dictionary of operators. By default all operators are
   enabled. This is how they are all implemented:
    -  **equal** &rarr; `__eq__(x)`
	-  **not_equal** &rarr; `__ne__(x)`
	-  **less** &rarr; `__lt__(x)`
    -  **greater** &rarr; `__gt__(x)`
    -  **less_or_equal** &rarr; `__le__(x)`
    -  **greater_or_equal** &rarr; `__ge__(x)`
    -  **in** &rarr; `in_(x)`
    -  **not_in** &rarr; `notin_(x)`
    -  **ends_with** &rarr; `like('%' + x)`
    -  **begins_with** &rarr; `like(x + '%')`
    -  **contains** &rarr; `like('%' + x + '%')`
    -  **not_contains** &rarr; `notlike('%' + x + '%')`
    -  **not_begins_with** &rarr; `notlike(x + '%')`
    -  **not_ends_with** &rarr; `notlike('%' + x)` 
    -  **is_empty** &rarr; `__eq__('')`
    -  **is_not_empty** &rarr; `__ne__('')`
    -  **is_null** &rarr; `is_(None)`
    -  **is_not_null** &rarr; `isnot(None)`
    -  **between** &rarr; `between(x[0], x[1])`


`Filter` only has one method: querybuilder. This method only accepts `rules` parameter, which is a dictionary that holds rules processed by jquery QueryBuilder or compatible.
 
## Examples

Given the file `module.py` containing the following mappings:
```python
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'test1'
    parentid = Column('test1id', Integer, primary_key=True)
```

You could use sqlalchemy-querybuild like:

### Using a module

```python
from sqlalchemy_querybuilder import Filter
import model

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
filter = Filter(model, session.query())
print(filter.querybuilder(rule)
```

### Using a dictionary instead of a module

```python
from sqlalchemy.orm import Session
from sqlalchemy_querybuilder import Filter
import model

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
filter = Filter({"test1": model.MyModel}, session.query())
print(filter.querybuilder(rule)
```

### Using a previously loaded query

```python
from sqlalchemy_querybuilder import Filter
import model
import other

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
filter = Filter(model, session.query(other.MyOtherModel))
print(filter.querybuilder(rule)
```
