# 1. Introduction to application design

## Design principles

This is covered in the lecture notes with references for more information in the reading list.

Summary of some common design principles:

- KISS: prefer simple to complex. Follow standards that make code easier to read. Deconstruct problems into smaller
  ones; give each function one thing to do. Use the least complex algorithm, data structure, etc.
- DRY: do not repeat business logic; some code may be repeated if it relates to different business logic.
- Loose coupling: Coupling is the degree of interdependence between software modules. Keep dependencies between
  modules/classes to the minimum needed.
- High cohesion: Cohesion refers to how strongly related and focused are the various responsibilities of a
  module; and how they work together to create something more valuable than the individual parts. Suggestions to
  increase cohesion:
    - The functionalities embedded in a class, accessed through its methods, have much in common.
    - Methods carry out a small number of related activities.
- Separation of concerns: A design principle for separating an application into distinct sections such that each section
  addresses a separate concern. A concern is a set of information that affects the code of a computer program.
- Modular: separate code into modules. The functions within a module should be cohesive. Modules should be loosely
  coupled.

There are many more sets of principles such as SOLID, GRASP if you want to try and apply these!

Many of the principles relate to object-oriented design. While your design will have some classes, you may also
have functions that do not belong to a class. In Python, functions can be grouped in modules.

Consider the principles when you design your app.

## Design patterns

One way to follow these principles in your application's design is to apply relevant design patterns.

A design pattern is a general blueprint to solve a common problem. First documented as design patterns in the
book [Design Patterns: Elements of Reusable Object-Oriented Software in 1994](https://en.wikipedia.org/wiki/Design_Patterns).

There are now many patterns, and you can find Python examples e.g. see those
in [Refactoring Guru](https://refactoring.guru/design-patterns/python).

Some of the patterns that may be relevant to your coursework:

- Model view controller (MVC): application design pattern for apps with a user interface that separates business logic
  and views from the underlying data.
  This [Real Python tutorial](https://realpython.com/lego-model-view-controller-python/) explains MVC using Python.
- REST (or RESTful) API: REpresentational State Transfer (REST) was first discussed by Roy Fielding. This is a software
  architecture style for client and server communications using HTTP. REST APIs are often used to access data as web
  service. This [Real Python tutorial](https://realpython.com/api-integration-in-python/) gives an explanation of Python
  REST APIs.
- Object relational mapper (ORM): An [ORM](https://www.fullstackpython.com/object-relational-mappers-orms.html) provides
  an abstraction that maps Python classes to relational database tables. SQLModel follows the ORM pattern.

Optionally, you may consider design patterns, for all or part of your application.

## Documenting the application design

To design the app, you are likely to consider the requirements, wireframes and data. Determine what your code needs to
be
able to do. Then consider how to structure that code in line consistent with design principles. Think about the Python
packages, modules, functions and classes that will be needed.

Having done that, you then need to document that as a diagram. Yet unlike the database design, there is no prescribed
diagram format. The next activity offers some examples for you to reflect on.

Specific techniques that you can read about include:

1. [UML class diagrams](https://realpython.com/lessons/uml-diagrams/), or variants of these.

   Most examples of class diagrams assume an object-oriented design. You are not expected to apply a fully
   object-oriented design.

   UML also has its critics, with some seeing it as overly complex.

   The assessment considers the clarity of the design and the application architecture. Diagrams should be easy to read,
   though strict adherence to UML is not assessed.

   The class diagram focuses on classes, so you may need to adapt it to include packages, modules and functions.

2. [C4 model](https://c4model.com/) is a more recent approach to visualizing software architecture.

   C4 describes a set of hierarchical diagrams, rather than notation.

    - Level 1: Context - System context diagram
    - Level 2: Containers - Container diagram
    - Level 3: Components - Component diagram
    - Level 4: Code diagram

   For the coursework you will need the level of detail shown at level 4.

### Tools for diagrams

For the coursework all diagrams can be hand drawn and do not need to be created with a diagramming app.

Tablet drawing apps, or apps such as PowerPoint can be used.

Mermaid is used in the course materials. Most digrams can be created in the Python version, though you may need to go
[Mermaid online](https://mermaid.live/edit#pako:eNqdVV1vmzAU_StXfuoklpHQfKFpUghptYdK3dq9TEiVASexCnZkmzVZlf8-YyCQxGm38ZLYnONzj--xeUUJTwny0fx6zpkiWxUx0I-iKiPwsJOK5FC_gZTilcA5LLmAr3pKMKIgwOyZslWNrdiL8uVGUEmeAl6wFIvdVew6EKES3Uy5EfoArxWjfO6JkJxdJYVUPCdi1uDL1ef1JMwiVM7PoIEBX4JaE4g10oEXqtawMQvhzMwBThItqGRPy10UC6xigYXytNiqA21upc2rGlMiE7PARdXQSg_ftvg5Fp--vG-0Fa06c1X9zMy2XupeJZxl_EUe1CUoDr8oeQHKdOdzrChngGNeqLIqKo7VHcAshRw_E9jgXU4sBVnj0T-Nx0k6WidhbHpQDRYl7Q7r0nQyidXPg-KCSMBZ1mxkoidM1SX03NXBudNxpQRmEiclTI-ISk5dtQV2XA1OXQ0sts6b1M1FfQhnR1m00gILLWjCJKvxX58WYOWRzygjvTPl_QXfbVvMwVh8zDHNauWqjketTU34tOAdTQSXfKlgsU3WmK0IkC7lXLgJQK0SWgyHEGKFYyzJ_zq39LVtqHfaUK-SiS-nti38W0EKUtd-Y6n9BgzicuG9N0JgqJ0W3FoEbt8T-IcbtA7Cyd9DNAL6nWTdy7x7__yQRB4Wq5Dt687BPsLZUCZnD4Slso6OrM_83eO9hajhR5-XI6a-5zQFOWglaIp8JQriII3UL_UQma5GSO9UrjfQNxf8EheZilDE9pq2wewn53nDFLxYrZG_xJnUo2KTYkXC6gt6gGh5_REpNxf5g6FZAvmvaFuORr3RxBt7_cl05Ln94bWDdsgfuT3Pm06nk9F0cu1N-97eQb-NqNubjIeufgYjdzx2B8P-_g9eH4F0)
for the C4 diagrams.

There are online tools such as LucidChart, you may need to create an account, and free versions may limit the number of
diagrams you can create.

Tools specific to C4:

- [Structurizr](https://www.structurizr.com/)
- [Structuizer for VSCode](https://marketplace.visualstudio.com/items?itemName=systemticks.c4-dsl-extension)

For apps that have already been written, you can generate a UML diagram from the code.
See [PyCharm UML class diagrams](https://www.jetbrains.com/help/pycharm/class-diagram.html) or search for
a [VS Code extension](https://marketplace.visualstudio.com/search?term=UML&target=VSCode&category=All%20categories&sortBy=Relevance).

[Next activity](7-03-identify-classes.md)