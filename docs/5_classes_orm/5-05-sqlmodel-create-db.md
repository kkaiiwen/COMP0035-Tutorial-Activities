# 5. Using SQLModel to create an SQLite database

Classes that are defined with the argument `table=True` can be created in a database with a few lines of code.

```python
from sqlmodel import SQLModel, create_engine

# 1. Define the classes (code not shown here)

# 2. Create a connection to a SQLlite database, replace 'database_name.db' with path to the database and its name
engine = create_engine("sqlite:///database_name.db")

# 3. Create all the tables in the database
SQLModel.metadata.create_all(engine)
```

The following example is from the SQLModel documentation:

```python
from __future__ import annotations
from sqlmodel import Field, SQLModel, create_engine


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None


engine = create_engine("sqlite:///hero.db")

SQLModel.metadata.create_all(engine)
```

## Code files and structure

Typically, you will see model classes saved in a file called `models.py`.

The code to create the database using these models is likely in another file, e.g. `database.py`.

The code to run the app would call the function to create the database using the models. This is likely to be in an
`app.py` or `main.py` module.

The structure of this code is shown in
the [SQLModel tutorial here](https://sqlmodel.tiangolo.com/tutorial/code-structure/#single-module-for-models).

### Activity: Create the database using this code structure

Write code to create the paralympics database separated into `models.py`, `database.py` and `app.py` files (modules).

You can copy the model code
from [starter_models.py](../../src/activities/starter/starter_models.py) to `models.py`.

Write code in `database.py` and `app.py` to create the database. Use a new database name `paralympics_sqlmodel.db` as
you probably already have one called `paralympics.db` from an earlier activity.

[Next activity](5-06-sqlmodel-add-data.md)

The section below is optional, you can skip if you wish.

## Using copilot to generate the SQLModels from a sql schema

This is a reflection on my experience of using copilot to generate SQLModels from a SQL schema.

I generated the initial version of the SQLModel classes using copilot in Pycharm with paralympics_schema.sql attached
and the prompt: "Based on the .sql schema, write SQLModel classes"

The generated code was then checked against current SQLModel syntax:

- https://sqlmodel.tiangolo.com/tutorial/create-db-and-table/ to define a class (for a table)
- https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/ for relationship attributes

Limitations of the initial copilot-generated solution:

- The attributes for date were treated as string. I decided to leave this since SQLite store a date as a string.
- Foreign key constraints were not recognised.
  The [SQLModel documentation](https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/cascade-delete-relationships/#ondelete-options)
  explains how to include these if you need to use them.
- Check constraints were not recognised. These are not directly supported in SQLModel in the current version, SQLAlchemy
  syntax was needed. I did not find this in the SQLModel documentation. The SQLAlchemy documentation can be complex
  to follow so this article has a clear and shorter summary:
  https://plainenglish.io/blog/creating-table-constraints-with-sqlmodel

The following shows one solution for the check constraint:

```python
from typing import Optional

from sqlalchemy import CheckConstraint
from sqlmodel import Field, SQLModel


class Team(SQLModel, table=True):
    code: str = Field(primary_key=True)
    name: str
    region: Optional[str]
    sub_region: Optional[str]
    member_type: Optional[str]
    notes: Optional[str]
    country_id: Optional[int] = Field(default=None, foreign_key="country.id")

    __table_args__ = (
        CheckConstraint("member_type IN ('country', 'team', 'dissolved', 'construct')"),
        CheckConstraint("region IN ('Asia', 'Europe', 'Africa', 'America', 'Oceania')")
    )
```



