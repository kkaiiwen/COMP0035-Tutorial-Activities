# 1. Introduction to Python classes

A Python class is way of bundling data (attributes) and behaviour (methods) together. Classes are often described as
a "blueprint" for creating objects. Objects specific instances of things, with actual data values for the attributes.

Consider the Paralympics scenario. Each Paralympic Games such as Paris 2024, includes multiple sports, such as Boccia.
Each sport has multiple events, for example Boccia has "Men's individual BC1" or "Mixed Pairs BC4".

An event might have attributes such as:

- name
- sport
- category
- competing athletes

It may also have behaviours such as:

- describe the event
- register athletes

This can be represented as a Python class.

For example, _Men's 100m T54_, an athletics event for classification T54 (wheelchair racing), is a specific instance (
object), of an _event_ class.

A Python class to represent an event can be written as follows:

```python
class ParalympicEvent:
    """ Represents a Paralympic event

     Attributes:
         name: A string representing the name of the event
         sport: An integer representing the sport that the event belongs to
         classification: An integer representing the event classification
         athletes: A list of strings representing the athletes that compete in the event

     Methods:
         describe() Prints a description of the event
         register_athlete() Adds an athlete to the list of athletes
     """

    def __init__(self, name, sport, classification):
        self.name = name
        self.sport = sport
        self.classification = classification
        self.athletes = []  # Empty list to hold athlete names

    def describe(self):
        """ Describes the event """
        print(f"{self.name} is a {self.sport} event for classification {self.classification}.")
        print("Athletes competing:", ", ".join(self.athletes))

    def register_athlete(self, athlete_name):
        """ Register the athlete with the event

        Args:
            athlete_name: A string representing the name of the athlete
        """
        self.athletes.append(athlete_name)
```

Key concepts in the class definition are:

- `class ParalympicEvent:` the keyword `class` defines this as a Python class. Class names typically start with a
  capital letter and use CamelCase.
- `docstring`: describes the class and its methods. This example uses
  the [Google style of class docstring](https://google.github.io/styleguide/pyguide.html#384-classes).
- `def __init__(self, name, sport, classification, athletes)`: - `__init__` is a special method, the constructor method, used to initialize new
  objects from a class. When you create a new object for the class this lets you set the value of its attributes. The parameter `self` is how the current object refers to itself. It lets you access
  and modify its attributes (variables).
- `self.name, self.sport` are _attributes_ of the class
- `describe()` and `register_athlets()` are methods of the class

This is a basic introduction to the core features of a class.

## Creating objects from a class

To create an object to represent a specific event, pass values to the constructor. 

```python
event = ParalympicEvent(
    name="Men's individual BC1",
    sport="Boccia",
    classification="BC1",
)
```

Use dot notation to call methods:

```python
event.describe()  # Should print the event description, "Athletes competing" will be empty
event.register_athlete("Sungjoon Jung")  # should register the athlete
event.describe()  # Should print the event again, "Athletes competing" should include Sungjoon Jung
```

## Activity: Create an instance of a class and use its methods

1. The ParalympicEvent class is in [starter_class.py](../../src/activities/starter/starter_class.py).
2. Use the class to create an instance for a given event, and register an athlete.

## Activity: Create an Athlete class

1. An athlete likely has more detail than just their name.
2. Create a class _Athlete_ with attributes such as name, the team they represent and their disability classification.
3. Add a method that prints the athlete's details. Instead of `describe()`, create a string representation of the class. To do this you can overwrite the default method by defining a method
   called `__str__(self)`. See [example here](https://www.codecademy.com/resources/docs/python/dunder-methods/str).
4. Create an instance of the class and print it.

[Next activity](5-02-inheritance-composition.md)