# Table of Contents

- [Priorities](#priorities)
- [Test pyramid](#test-pyramid)
  - [UI](#ui)
  - [API](#api)
  - [Models](#models)
- [Bugs](#bugs)
- [References](#references)
  
## Priorities

The tests should:

1. Cover all critical user flows
1. Focus on developer experience
1. Be easy to read/write
1. Be fast to run (consider parallel testing)

When writing tests focus on:

1. Focus on and test just one thing
1. Are flake-free and do not fail randomly
1. Give you confidence to refactor code and add new features
1. Are easy to run both locally and on a continuous integration server

Ref: [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#When-should-I-write-a-unit-test-and-when-should-I-write-an-end-to-end-test)

## Test pyramid

According to Martin Fowler, *"The "Test Pyramid" is a metaphor that tells us to group software tests into buckets of different granularity."*

This is meant to create a wholistic view 

### UI

**Examples:**

1. [Cypress cucumber example repo](https://github.com/jmarti-theinit/cypress-cucumber-example)
      1. [Google search feature](https://github.com/jmarti-theinit/cypress-cucumber-example/blob/master/cypress/integration/google/search.feature)

When should I write a unit test and when should I write an end-to-end test?

> If a unit test requires a lot of mocking ... you may want to rewrite it as an end-to-end test. - [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#When-should-I-write-a-unit-test-and-when-should-I-write-an-end-to-end-test)

How do I convince my company to use Cypress?

> We believe that the best approach is a “bottoms up” approach, where you can demonstrate how Cypress solves your company’s particular needs. Implement a prototype with your project to see how it feels. Test a couple of common user stories. Identify if there are any technical blockers. Show the prototype to others before proceeding any further. If you can demonstrate the benefits of using Cypress as a developer tool for your project to other engineers, then Cypress will likely be more quickly adopted. - [Cypress FAQ](https://docs.cypress.io/faq/questions/general-questions-faq.html#How-do-I-convince-my-company-to-use-Cypress)

How to write scenario steps

> If your feature files are full of “I click this” and “I see this” you are in a wrong place - you should probably use cypress directly. Gherkin should NOT talk about UI layer. This is a common misconception. Your feature in 95% of cases has nothing to do with the UI. UI is an implementation detail. Feature description should be high level and make sense no matter if you are creating a feature to work with a web app, Alexa, or even a phone call. To be honest - this is not always easy or doable, but this should be your direction. - [The Brain Software House](https://thebrain.pro/blog/Cypress-Cucumber-Preprocessor-Update)

### API

### Models

## Bugs

> ... before fixing a bug exposed by a high level test, you should replicate the bug with a unit test. Then the unit test ensures the bug stays dead. - [Martin Fowler](https://martinfowler.com/bliki/TestPyramid.html)

## References

**General**

- [Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)
- [Cucumber syntax](https://cucumber.io/docs/gherkin/reference)

**Frontend**

- https://www.monterail.com/blog/end-to-end-testing-with-cypress
- https://automationrhapsody.com/cypress-vs-selenium-end-era
- [Cypress roadmap](https://docs.cypress.io/guides/references/roadmap.html#Test-Runner)
- [Cypress Cucumber preprocessor](https://github.com/TheBrainFamily/cypress-cucumber-preprocessor)

**Backend**

- https://dev.to/truggeri/rspec-or-minitest-for-testing-rails-apps-42fi
- https://tenderlovemaking.com/2015/01/23/my-experience-with-minitest-and-rspec.html
