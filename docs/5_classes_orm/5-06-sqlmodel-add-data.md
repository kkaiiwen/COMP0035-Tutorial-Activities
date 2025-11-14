# 6. Using SQLModel to add data to an SQLite database

To add a single record to a database table is conceptually similar to the code used with sqlite: 

- create the instance
- add it
- commit it

```python
hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")

engine = create_engine("sqlite:///database.db")

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.commit()
```

To add data to the database, you can read the values from the data file and create object instances. One way to do this 
is to read the data into a pandas DataFrame first, for example:

```python
import pandas as pd
from sqlmodel import Session, SQLModel, create_engine
from mymodels import MyData  # Replace with your actual model

# 1. Read Excel file
df = pd.read_excel("your_data.xlsx")

# 2. Convert DataFrame rows of values to SQLModel instances
records = []
for _, row in df.iterrows():
    record = MyData(**row.to_dict())
    records.append(record)

# 3. Insert into database
engine = create_engine("sqlite:///mydatabase.db")
with Session(engine) as session:
    session.add_all(records)
    session.commit()
```

Adding data to the paralympics database is more complex than the example above due to the number of tables and the
relationships. This is skipped for now and covered in week 8.

[Next activity](5-07-summary.md)