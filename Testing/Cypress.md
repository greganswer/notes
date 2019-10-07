# Cypress

- [Summary](#summary)
- [Details](#details)
  - [Advantages](#advantages)
  - [Disadvantages](#disadvantages)
  - [FAQs](#faqs)
- [Examples](#examples)
- [References](#references)

## Summary

- Cypress is a front end Automation testing tool built for the modern web applications
- Cypress automatically waits for commands and assertions before moving on. No more async hell.
- Ability to test Edge Test cases by Mocking the server response
- Cypress takes snapshots as your tests run. We can hover over each commands in the Command Log to see exactly what happened at each step.
- View videos of your entire tests execution when run from the Cypress Dashboard.
- Cypress engine directly operates inside the browser
- listen and modify the browser behavior at run time by manipulating DOM and altering Network requests and responses on the fly

## Details

### Advantages

- It is easy to install Cypress. It is easy to write tests with it. It is very easy to debug tests. It is easy to include it in continuous integration or continuous delivery pipelines.
- Can be run in parallel [with some additional setup](https://docs.cypress.io/guides/guides/parallelization.html)

### Disadvantages

- Only supports Chrome
- No native event handling capabilities.
- Such as upload, download file, tab key, etc. This is one feature that we genuinely miss, and its lack gets more noticeable as the app grows. Native events don’t actually handle our killer features, but we’d feel more secure if we could at least test them in our end-to-end tests.

### FAQs

- When to use `cy.contains()`?
    - If you want the test to fail when the content changes then use `cy.contains()`. Otherwise use a data attribute

See more [ Cypress Best Practices](https://docs.cypress.io/guides/references/best-practices.html)

## Examples

1. [Cypress cucumber example repo](https://github.com/jmarti-theinit/cypress-cucumber-example)
      1. [Google search feature](https://github.com/jmarti-theinit/cypress-cucumber-example/blob/master/cypress/integration/google/search.feature)

```bash
# Opens the Cypress Test Runner in interactive mode.
# https://docs.cypress.io/guides/guides/command-line.html#cypress-opennpx cypress open

# Run tests in headless mode in the Electron browser.
# https://docs.cypress.io/guides/guides/command-line.html#cypress-run
npx cypress run 
```

- You can use any [CSS selectors](https://www.w3schools.com/cssref/css_selectors.asp) to target elements on the page
- You can also use the [Cypress Selector Playground](https://docs.cypress.io/guides/core-concepts/test-runner.html#Selector-Playground) to help find the most unique selector

```javascript
describe('My First Test', function() {
  it('Does not do much!', function() {
    expect(true).to.equal(true)
    cy.visit("https://google.com")
  })
})
```

## References

- [End-to-end testing with Cypress](https://www.monterail.com/blog/end-to-end-testing-with-cypress)
- [Cypress vs Selenium](https://automationrhapsody.com/cypress-vs-selenium-end-era)
- [Cypress road map](https://docs.cypress.io/guides/references/roadmap.html#Test-Runner)
- [Cypress Cucumber preprocessor](https://github.com/TheBrainFamily/cypress-cucumber-preprocessor)
- [Cypress cheat sheet](https://github.com/janmanfai/cypress-cheat-sheet)
- [CSS Tricks article](https://css-tricks.com/an-intro-to-web-app-testing-with-cypress-io)
- [Cypress FAQ](https://docs.cypress.io/faq/questions/using-cypress-faq.html)
- [Cypress Commands](https://docs.cypress.io/api/api/table-of-contents.html)
