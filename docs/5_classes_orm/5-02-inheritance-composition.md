# 2. Class inheritance and composition

## Class inheritance

Inheritance is a feature in object-oriented programming that allows one class (called a **child** or **subclass**) to
inherit
attributes and methods from another class (called a **parent** or **superclass**).

Benefits of inheritance include:

- Reuse code across related classes
- Organize code more logically
- Extend functionality without rewriting everything

For example, you have an Athlete class. Now you want to add a more specific class Runner that inherits from it and adds
specific data and methods that are only relevant for runner:

```python
# Base class
class Athlete:
    def __init__(self, first_name, last_name, team_code, disability_class):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class

    def introduce(self):
        print(f"{self.first_name} {self.last_name} represents {self.team_code} in class {self.disability_class}.")


# Subclass
class Runner(Athlete):
    def __init__(self, first_name, last_name, team_code, disability_class, distance):
        super().__init__(first_name, last_name, team_code, disability_class)
        self.distance = distance  # e.g., 100m, 400m

    def race_info(self):
        print(f"{self.first_name} is running the {self.distance} race.")


# Example usage
runner1 = Runner("Li", "Na", "CHN", "T12", "100m")
runner1.introduce()  # Inherited method
runner1.race_info()  # Subclass-specific method
```

Key concepts in the code:

- `class Runner(Athlete)`: the Runner class inheirts from Athlete. A class can inherit from more than one class e.g.
  `class Runner(Athlete, TeamMember)`.
- `super().__init__()`: calls the constructor of the parent class to initialise inherited attributes.
- The Runner subclass now has access to the args and methods of the Athlete class and can also add its own specific
  attributes (e.g. `distance`), and methods ( e.g. `race_info()`).

## Class composition

Composition is a design principle where a class is made up of one or more objects from other classes, rather
than inheriting from them.

For example, an Athlete can have a list of Medal objects.

```python
from dataclasses import dataclass
from datetime import date
from typing import List


@dataclass
class Medal:
    type: str
    design: str
    date_designed: date


class Athlete:
    def __init__(self, first_name: str, last_name: str, team_code: str, disability_class: str, medals: List[Medal]):
        self.first_name = first_name
        self.last_name = last_name
        self.team_code = team_code
        self.disability_class = disability_class
        self.medals = medals  # Composition: Athlete has Medals
```

Note: The code above include [type annotations](https://typing.python.org/en/latest/spec/annotations.html). Type
annotations (type hints) are an optional notation in Python that specifies te tyoe of a parameter or function result. It
tells the programme using the function or class what kind of data to pass and what kind of data to expect when a value
is returned.

To create an athlete with medals:

```python
# Create medals
medal1 = Medal("gold", "Paris 2024 design", date(2023, 7, 1))
medal2 = Medal("silver", "Tokyo 2020 design", date(2019, 8, 25))

# Create an athlete with medals
athlete = Athlete(
    first_name="Wei",
    last_name="Wang",
    team_code="CHN",
    disability_class="T54",
    medals=[medal1, medal2]
)

print(athlete)
```

## Activity

1. Modify your `Athlete` class to include a list of `Medal` objects as an attribute.

[Next activity](5-03-pydantic.md)