# 3. Determine the application structure

Model-View-Controller (MVC) MVC is a common design pattern for web applications. This activity assumes a decision has been made to structure the 
app in accordance with the MVC pattern. You are not required to follow this pattern in your coursework. It is used here for
speed in the tutorial, so you don't have to start from a blank sheet in determining the app structure.

## MVC design pattern

The goal of the MVC design pattern is to separate concerns in a web application:

- the **model** handles data and business logic,
- the **view** manages the user interface and presentation,
- and the **controller** acts as an intermediary between them.

Key concepts:

**Routes and controllers**

Each _route_ in a web app has a _controller_ action. When a user entera a URL, the application attempts to match it to a
defined route, and, if successful, calls that route's controller action. The controller typically:
- Retrieves data from the model (e.g., via a database)
- Passes that data to a view, which renders the page

**Models** 

Represent the data and its associated logic. They interact with the database and determine what data is
sent to the controller. You have already seen the ORM data mapper pattern to map between these model classes and the
database tables.

**Views**

In the view, the data is accessed and the information contained within is used to render the HTML content of
the page the user ultimately sees in their browser. You already designed the views as wireframes.

## Diagram format

This activity is loosely based on the UML class diagram format. This is not the only choice of diagram.

[Mermaid](https://mermaid.js.org/ecosystem/tutorials.html) is used as you likely installed to view the database
diagrams. If not, you may need to view these activities on GitHub.

Remember the following symbols for classes and relationships:

![UML class diagram notation](../img/uml-class-diag-notation.png)

## Add the model classes

The following were derived from the ERD and the activities to identify classes from the user stories.

```mermaid
classDiagram
    class Event {
        String type
        int year
        date start
        date end
        int duration
        int countries
        int events
        int sports
        String highlights
        String url
    }

    class Host {
        String host_name
    }

    class HostEvent {
        <<Association>>
    }

    class Country {
        String country_code
        String country_name
    }

    class Disability {
        String category
    }

    class Participants {
        int participants_m
        int participants_f
        int participants
    }

    class DisabilityEvent {
        <<Association>>
    }

    class Student {
        String first_name
        String last_name
    }

    class Teacher

    class Chart {
        String chart_type
        List~Participants~ participants_data
        List~Event~ event_data
    }

    class Quiz {
        String name
    }

    class Question {
        String question_type
        String question_text
    }

    class AnswerChoice {
        Question question
        String answer_text
        boolean is_correct_answer
        int score_value
    }

    class Response {
        List~Answer~ answers
        Student student
        int score
    }

    Teacher -- Quiz
    Teacher -- AnswerChoice
    Teacher -- Question
    Student -- Response
    Response -- AnswerChoice
    Chart -- Event
    Chart -- Participants
    Quiz -- Question
    Question -- AnswerChoice
    Event -- HostEvent
    Disability -- DisabilityEvent
    Event -- DisabilityEvent
    Host -- HostEvent
    Host -- Country
    Participants -- Event
```    

## Add the controller classes

These control the business logic. I have grouped them according to function; you may choose a different way to group
them. There is no single way to design these!

If not following the MVC model, these operations may be in the relevant model classes.

The logic to create, read, update and delete any of the model classes will be handled by the ORM, so has not been added
here. You can add them to the class diagram if you prefer.

```mermaid
classDiagram
    class QuizController {
        Quiz quiz
        Question question
        AnswerChoice answer
        generate_quiz()
        submit_student_resonses()
        generate_student_score()
    }

    class AuthenticationController {
        boolean is_authenticated
        sign_in()
        sign_out()
    }

    class ChartController {
        Filter filter
        generate_filter_values()
        create_line_chart(List filters)
        create_bar_chart(List filers)
        create_map()
    }
```

## Add all the classes to the class diagram and add the relationships

The 'view' classes have been omitted in the diagram below. In the coursework you have represented these with the
wireframes.

You may not agree with this diagram, you may have made different choices to structure it differently.

This version also groups the Python classes into Python packages. This is not required.

```mermaid
classDiagram
    namespace ParalympicsPackage {
        class Event {
            String type
            int year
            date start
            date end
            int duration
            int countries
            int events
            int sports
            String highlights
            String url
        }

        class Host {
            String host_name
        }

        class HostEvent {
            <<Association>>
        }

        class Country {
            String country_code
            String country_name
        }

        class Disability {
            String category
        }

        class Participants {
            int participants_m
            int participants_f
            int participants
        }

        class DisabilityEvent {
            <<Association>>
        }
    }

    namespace AuthenticationPackage {
        class Student {
            String first_name
            String last_name
        }

        class Teacher {
            boolean is_authenticated
        }

        class AuthenticationController {
            Teacher teacher
            verify_authentication(Teacher teacher)
        }
    }

    namespace ChartPackage {
        class Chart {
            String chart_type
            List~Participants~ participants_data
            List~Event~ event_data
        }

        class Filter {
            List~date~ date_range_filter
            String type_filter
        }

        class ChartController {
            Filter filter
            Chart chart
            generate_filter_values()
            create_line_chart(List filters)
            create_bar_chart(List filers)
            create_map()
        }
    }

    namespace QuizPackage {
        class Quiz {
            String name
        }

        class Question {
            String question_type
            String question_text
        }

        class AnswerChoice {
            Question question
            String answer_text
            boolean is_correct_answer
            int score_value
        }

        class Response {
            List~AnswerChoice~ answers
            Student student
            int score
        }

        class QuizController {
            Quiz quiz
            List~Question~ questions
            List~AnswerChoice~ answers
            List~Response~ student_responses
            int score
            generate_quiz()
            generate_student_score(responses)
        }
    }

    Teacher -- Quiz
    Teacher -- AnswerChoice
    Teacher -- Question
    Student -- Response
    Response -- AnswerChoice
    Chart -- Event
    Chart -- Participants
    Quiz -- Question
    Question -- AnswerChoice
    Event -- HostEvent
    Disability -- DisabilityEvent
    Event -- DisabilityEvent
    Host -- HostEvent
    Host -- Country
    Participants -- Event
    QuizController -- Quiz
    QuizController -- Question
    QuizController -- AnswerChoice
    QuizController -- Response
    ChartController -- Chart
    ChartController -- Filter
    AuthenticationController -- Teacher
```    

[Next activity](7-05-review-design.md)