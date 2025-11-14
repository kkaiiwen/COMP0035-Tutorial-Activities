# 3. Pydantic classes

[Pydantic](https://docs.pydantic.dev/latest/) is a Python library used for data validation and settings management using
[Python type annotations](https://typing.python.org/en/latest/spec/annotations.html). It's widely used in modern Python
projects, particularly with frameworks like FastAPI.

You will be using pydantic and FastAPI in COMP0034.

Key features of Pydantic:

- Validates data: Ensures that the data you receive from users, APIs, files, etc. matches the types and constraints
  you specify.
- Parses data: Converts input data into Python objects with the correct types.
- Automatic error messages: Provides clear feedback when data is invalid.

To use Pydantic, your class should inherit it's `BaseModel` class. This inheritance gives your class all the
attributes and [methods](https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties) of the Pydantic
BaseModel.

Classes defined using Pydantic are typically referred to as **models**. A Pydantic model is simply a
Python class that:

- Inherits from BaseModel
- Uses type annotations to define fields

Note that pydantic syntax varies for different versions of pydantic and different versions of Python. Use
the latest [pydantic documentation](https://docs.pydantic.dev/latest/) rather than other sources of information.

The `Athlete` class is rewritten as a Pydantic model class:

```python
from pydantic import BaseModel


class Athlete(BaseModel):
    first_name: str
    last_name: str
    team_code: str
    disability_class: str
    medals: list[Medal]
```

Pydantic classes can contain methods:

```python
from pydantic import BaseModel


class Athlete(BaseModel):
    first_name: str
    last_name: str
    team_code: str
    disability_class: str
    medals: list[Medal]

    def introduce(self) -> str:
        return f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}."
```

The function signature `def introduce(self) -> str:` uses Python's type hinting to specify that the function
returns a string. This is optional but improves readability and clarity.

You can find a version of the classes with Pydantic
in [starter_pydantic.py](../../src/activities/starter/starter_pydantic.py)

## Pydantic validation

You can specify optional fields and default values using type hints and assignment:

```python
class Athlete(BaseModel):
    first_name: str  # Must be provided
    last_name: str  # Must be provided
    team_code: str | None  # Optional, can be None
    disability_class: str | None  # Optional, can be None
    medals: list[Medal] = []  # Set to empty as default
```

## Activity: Add validation to the Athlete

1. Make a copy of [starter_pydantic.py](../../src/activities/starter/starter_pydantic.py)
2. Add validation to the `Athlete` and optionally to the `Medal` class.
3. Create an instance with valid data e.g.
    - create an `athlete` with no medals
    - create a new medal
    - add the new medal to the athlete's medals list e.g. `athlete.medals.append(new_medal)`

   Examples of real para athletes from Paris 2024:
    - Yuyan Jiang from team CHN People's Republic of China won 7 gold medals
    - Catherine Debrunner from ITA Italy won 5 gold and 1 bronze
    - Bianka Pap from HUN Hungary won 1 gold, 1 silver and 1 bronze
4. Create an instance with invalid data. Try with and without the use of `try/except` with `ValidationError:` to catch
   validation errors.

    ```python
   from pydantic import ValidationError
   
     try:
        bp = Athlete(first_name="Bianka", medals=1)
    except ValidationError as e:
        print(e.errors())
    ```

[Next activity](5-04-orm-sqlmodel.md)