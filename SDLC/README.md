# SDLC

- [Summary](#summary)
- [Glossary](#glossary)
- [Details](#details)
  - [Acceptance criteria](#acceptance-criteria)
  - [User stories](#user-stories)
  - [Design](#design)
  - [Behavior driven development (BDD)](#behavior-driven-development-bdd)
    - [End to End](#end-to-end)
    - [Web API](#web-api)
    - [Unit](#unit)
  - [Bugs](#bugs)
- [Examples](#examples)
- [References](#references)

## Summary

- This document will help create **ubiquitous language** for the organization
- Each scenario in a Feature should be small enough that it can be **"done"** in one sprint
    - If not, try to decrease the scope of work
- Each stage does not need to be thoroughly completed before moving to the next
    - This is a case where the more details, the better

## Glossary

Unfortunately in software development the same word can be used to mean many things. 
This glossary is an attempt to create an explicit definition of the terms used in this document. 

**NOTE: These terms/definitions are subject to change.**

**General**

| Term                                  | Definition                                                                                                                                                                                                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Behavior Driven Development (BDD)** | A software development methodology based on the use of conversation and concrete examples to formalize a shared understanding of the business behaviors your code is implementing.<br>*Example documents: Use stories, Acceptance Criteria, End to End tests* |
| **Cucumber**                          | A software testing tool that supports behavior-driven development                                                                                                                                                                                             |
| **End to End (E2E) tests**            | Tests that exercise end user interactions with the application using production-like circumstances and data.                                                                                                                                                  |
| **Functional specification**          | specify the behavior of the unit being tested                                                                                                                                                                                                                 |
| **Gherkin language**                  | The plain language parser that Cucumber uses to define test cases                                                                                                                                                                                             |
| **Ubiquitous language**               | A (semi-)formal language that is shared by all members of a software development team — both software developers and non-technical personnel                                                                                                                  |
| **Unit tests**                        | Tests that validate the functionality of the smallest component of a system that can be tested in isolation.<br>*Example: Functions, Classes, Models, etc.*                                                                                                   |
| **Web API**                           | A backend (server-side) software layer that returns JSON/XML responses from requests to store, access, and modify data.<br>*Example: https://api.github.com*                                                                                                  |

**Acceptance Criteria**

| Term                                   | Definition                                                                                                                                                           |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Functional Acceptance Criteria**     | The user tasks, functions, and businesses process that should be in place.<br>*Example: When a I receive a new message then I should see an on-screen notification.* |
| **Non-functional Acceptance Criteria** | List of business rules that must be met.<br>*Example: When the user gets their password wrong 3 times then they are locked out of the system for 30 minutes.*        |
| **Performance Acceptance Criteria**    | List of performance rules that must be met.<br>*Example: The page must load in less than 3 seconds with 1000 concurrent users.*                                      |
 
## Details

### Acceptance criteria

![Acceptance criteria ball of yarn](/images/acceptance-criteria-ball-of-yarn.jpg)

*source: https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important*

- Document the functional, non-functional, and performance acceptance criteria

### User stories

- When writing user stories, define the minimum piece of functionality you're able to deliver and stick to it. 

> The common template for describing acceptance criteria using a scenario-oriented approach is the Given/When/Then format that is derived from behavior-driven development (BDD). The Given/When/Then format is used for writing acceptance tests that ensure that all the specification requirements are met. - [Writing Clear Acceptance Criteria for User Stories](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important)

| Term         | Definition                                                                  |
| ------------ | --------------------------------------------------------------------------- |
| **Feature**  | A Use Case that describes a specific function of the software being tested  |
| **Scenario** | A flow of events through the Feature. Each Feature has 1 or more Scenarios. |
| **Steps**    | The first word of a step is a Keyword (see below)                           |

List of Scenario Keywords:

| Keyword   | Definition                                                            |
| --------- | --------------------------------------------------------------------- |
| **Given** | This keyword represents some precondition or situation                |
| **When**  | This keyword represents the action performed by the user or system    |
| **Then**  | This keyword represents the expected result                           |
| **And**   | Which is the logical and                                              |
| **But**   | Which is logically the same as **And**, but used in the negative form |

**Examples**

```gherkin
Feature: Google Homepage Search
  As a user
  I can search for articles
  So that I can read them during my leisure

  Scenario: User can search with "Google Search"
    Given I'm on the homepage
    When I type "random page" into the search field
    And I click the Google Search button
    Then I should see the random page search results

  Scenario: User can search with "I'm Feeling Lucky"
    Given I'm on the homepage
    When I type "random page" into the search field
    And I click the I'm Feeling Lucky button
    Then I should be taken to a random page
```

*Notice the use of [Gherkin Markdown Syntax highlighting](https://bit.ly/2LVzW8k).*

### Design

### Behavior driven development (BDD)

The purpose of BDD is to focus on the behavior of the system and its components. This allows technical and non-technical people to discuss the desired outcomes of the software development efforts. 

> Writing automated tests is a developer responsibility. Write the tests that prove the code works. - [How to Use the Testing Pyramid to Fail Fast and Reduce Risk](https://www.contino.io/insights/the-testing-pyramid)
> 
**Tactics**

According to [the Agile Alliance](https://www.agilealliance.org/glossary/bdd) improves upon Test Driven Development by using the following tactics:

- Apply the "Five Why's" principle to each proposed user story, so that its purpose is clearly related to business outcomes
- thinking "from the outside in", in other words implement only those behaviors which contribute most directly to these business outcomes, so as to minimize waste
- describe behaviors in a single notation which is directly accessible to domain experts, testers and developers, so as to improve communication
- apply these techniques all the way down to the lowest levels of abstraction of the software, paying particular attention to the distribution of behavior, so that evolution remains cheap

**Priorities**

The tests should:

1. Cover all critical user flows
1. Be easy to read/write
1. Be fast to run (consider parallel testing)
1. Not fail randomly
1. Give you confidence to refactor code and add new features
1. Be easy to run both locally and on a continuous integration server

Reference: [Cypress FAQ](https://bit.ly/2AU1sNs)

**Test pyramid**

![Test pyramid](/images/test-pyramid.png)
source: https://www.ontestautomation.com/the-test-automation-pyramid

**NOTE:** In the Test pyramid diagram above, substitute "User Interface tests" with "E2E tests" because User Interface tests can be unit tests, which is misleading

According to Martin Fowler, *"The "Test Pyramid" is a metaphor that tells us to group software tests into buckets of different granularity."*

This is meant to create a wholistic view of stabilizing the app in a scalable way.

#### End to End

Modern software systems are complex and are interconnected with multiple sub-systems. 
A sub-system may be different from the current system or may be owned by another 
organization. If anyone of the sub-systems fails, the whole software system could 
collapse. This is a major risk and can be avoided by End-to-End testing.

It's best to select a few of the most critical user flows to test within that 
application to maximize this Return on Investment.

**Advantages**

- Confirms your application's health from a user's perspective
- Expands test coverage
- May catch the most bugs 

**Disadvantages**

- Typically the slowest to run
- Can be more complicated to setup

**Examples:**

When should I write a unit test and when should I write an end-to-end test?

> If a unit test requires a lot of mocking ... you may want to rewrite it as an end-to-end test. - [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#When-should-I-write-a-unit-test-and-when-should-I-write-an-end-to-end-test)

How do I convince my company to use Cypress?

> We believe that the best approach is a "bottoms up" approach, where you can demonstrate how Cypress solves your company’s particular needs. Implement a prototype with your project to see how it feels. Test a couple of common user stories. Identify if there are any technical blockers. Show the prototype to others before proceeding any further. If you can demonstrate the benefits of using Cypress as a developer tool for your project to other engineers, then Cypress will likely be more quickly adopted. - [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#How-do-I-convince-my-company-to-use-Cypress)

How to write scenario steps

> If your feature files are full of "I click this" and "I see this" you are in a wrong place - you should probably use cypress directly. Gherkin should NOT talk about UI layer. This is a common misconception. Your feature in 95% of cases has nothing to do with the UI. UI is an implementation detail. Feature description should be high level and make sense no matter if you are creating a feature to work with a web app, Alexa, or even a phone call. To be honest - this is not always easy or doable, but this should be your direction. - [The Brain Software House](https://thebrain.pro/blog/Cypress-Cucumber-Preprocessor-Update)

#### Web API

**Advantages**

- Typically faster than E2E tests
- Tests different components and units work together

**Disadvantages**

- Typically slower to run than unit tests

#### Unit

**Advantages**

- Can be written relatively quickly 
- Can be executed quickly 
- Give the programmer very specific information about the origins of a bug, up to the exact line of code where a failure occurs

**Disadvantages**

- Unable to detect integration or system level bugs due to focus on small pieces of code

**Examples:**

```gherkin
Specification: Stack
  Scenario: New stack
    When a new stack is created
    Then it is empty
    
  Scenario: Add to stack
    When an element is added to the stack
    Then that element is at the top of the stack
    
  Scenario: Remove from stack
    When a stack has N elements 
    And element E is on top of the stack
    Then a pop operation returns E
    And the new size of the stack is N-1
```

*Notice the use of [Gherkin Markdown Syntax highlighting](https://bit.ly/2LVzW8k).*

### Bugs

> ... before fixing a bug exposed by a high level test, you should replicate the bug with a unit test. Then the unit test ensures the bug stays dead. - [Martin Fowler](https://martinfowler.com/bliki/TestPyramid.html)

## Examples

## References 

- [Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Cucumber syntax](https://cucumber.io/docs/gherkin/reference)
- [API Wikipedia definition](https://en.wikipedia.org/wiki/Application_programming_interface)
- [Writing clear user stories](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important)
- [Acceptance Criteria](http://www.professionalqa.com/acceptance-criteria)
- [Acceptance Criteria examples](https://simplicable.com/new/acceptance-criteria-examples)
- [End to End testing](https://dzone.com/articles/what-is-end-to-end-testing-1)
- [Behavior Driven Development wiki page](https://en.wikipedia.org/wiki/Behavior-driven_development)
- [Behavior Driven Development from the Agile Alliance](https://www.agilealliance.org/glossary/bdd)
- [Cucumber language definition](https://en.wikipedia.org/wiki/Cucumber_(software))
- [How to Use the Testing Pyramid to Fail Fast and Reduce Risk](https://www.contino.io/insights/the-testing-pyramid)
- [The test automation pyramid](https://www.ontestautomation.com/the-test-automation-pyramid)
 