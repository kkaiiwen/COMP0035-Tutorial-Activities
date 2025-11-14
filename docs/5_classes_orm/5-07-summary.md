# 7. Summary

Many concepts have been introduced this week. These are key foundations that will support your design work over the next
five weeks and your application development work next term.

If you are unsure of the concepts, please ask questions during office hours or in a tutorial; or carry out your own
research, there are many helpful tutorials online.

Key concepts to understand:

- A Python **class** models a real world object. It has:
    - **attributes** to store data
    - **methods** to define behaviour.
    - A class can have just attributes. An **object** is one instance of a class that has been created.

- **Inheritance** allows one class to inherit the attributes and methods from another, whilst also
  implementing its own.

- **Pydantic** is a Python library for **data validation**. To use it, a class inherits from `BaseModel`. Validation is
  important when building apps that handle user or external data.

- **Object-Relational Mapping (ORM)** is a technique that lets you interact with a database using Python objects instead
  of writing raw SQL. ORMs map database tables to classes and rows to objects, making data handling more intuitive.

- **SQLModel** is ORM that is build on Pydantic and SQLAlchemy.

- In Pydantic and SQLModel, a **model** is a Python class that defines the structure and types of
  data. It 'models' the data that an application will use.

- Python classes, Pydantic models, and SQLModel classes vary in syntax, which can be confusing. Focus on
  learning SQLModel syntax, as that will be most relevant for your coursework.

Note: for coursework 2 you are welcome to use SQLAlchemy instead of SQLModel if you prefer. For those who wish to do so
the [next activity](5-08-sqlalchemy.md) provides an overview.