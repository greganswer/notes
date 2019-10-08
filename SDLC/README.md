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
| **End to End (E2E) tests**            | Tests that exercise end user interactions with the application using production-like circumstances and data.                                                                                                                                                  |
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

- When writing user stories, define the minimum piece of functionality you’re able to deliver and stick to it. 

> The common template for describing acceptance criteria using a scenario-oriented approach is the Given/When/Then format that is derived from behaviour-driven development (BDD). The Given/When/Then format is used for writing acceptance tests that ensure that all the specification requirements are met. - [Writing Clear Acceptance Criteria for User Stories](https://rubygarage.org/blog/clear-acceptance-criteria-and-why-its-important)

| Term      | Definition                                 |
| --------- | ------------------------------------------ |
| **Given** | Defines some precondition or situation     |
| **When**  | The action performed by the user or system |
| **Then**  | The expected result                        |

**Examples**

### Design

### Behavior driven development (BDD)

**Test pyramid**

According to Martin Fowler, *"The "Test Pyramid" is a metaphor that tells us to group software tests into buckets of different granularity."*

This is meant to create a wholistic view of stabilizing the app in a scalable way.

**Priorities**

The tests should:

1. Cover all critical user flows
1. Be easy to read/write
1. Be fast to run (consider parallel testing)
1. Be flake-free and do not fail randomly
1. Give you confidence to refactor code and add new features
1. Be easy to run both locally and on a continuous integration server

Reference: [Cypress FAQ](https://bit.ly/2AU1sNs)

#### End to End

Modern software systems are complex and are interconnected with multiple sub-systems. 
A sub-system may be different from the current system or may be owned by another 
organization. If anyone of the sub-systems fails, the whole software system could 
collapse. This is a major risk and can be avoided by End-to-End testing.

It's best to select a few of the most critical user flows to test within that 
application to maximize this Return on Investment.

**Advantages**

- Confirms your application’s health
- Expands test coverage
- Catches more bugs 

**Disadvantages**

- Typically slower to run
- Can be more complicated to setup

**Examples:**

When should I write a unit test and when should I write an end-to-end test?

> If a unit test requires a lot of mocking ... you may want to rewrite it as an end-to-end test. - [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#When-should-I-write-a-unit-test-and-when-should-I-write-an-end-to-end-test)

How do I convince my company to use Cypress?

> We believe that the best approach is a “bottoms up” approach, where you can demonstrate how Cypress solves your company’s particular needs. Implement a prototype with your project to see how it feels. Test a couple of common user stories. Identify if there are any technical blockers. Show the prototype to others before proceeding any further. If you can demonstrate the benefits of using Cypress as a developer tool for your project to other engineers, then Cypress will likely be more quickly adopted. - [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#How-do-I-convince-my-company-to-use-Cypress)

How to write scenario steps

> If your feature files are full of “I click this” and “I see this” you are in a wrong place - you should probably use cypress directly. Gherkin should NOT talk about UI layer. This is a common misconception. Your feature in 95% of cases has nothing to do with the UI. UI is an implementation detail. Feature description should be high level and make sense no matter if you are creating a feature to work with a web app, Alexa, or even a phone call. To be honest - this is not always easy or doable, but this should be your direction. - [The Brain Software House](https://thebrain.pro/blog/Cypress-Cucumber-Preprocessor-Update)

#### Web API

#### Unit

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