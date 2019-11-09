# Cypress

  - [Summary](#summary)
  - [Details](#details)
    - [Advantages](#advantages)
    - [Disadvantages](#disadvantages)
    - [Best Practices](#best-practices)
    - [Folder structure](#folder-structure)
    - [Files](#files)
    - [Additional info](#additional-info)
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

### Best Practices

- Test specs in isolation, programmatically log into your application, and take control of your application’s state.
- Only test what you control. When necessary, always use `cy.request()` to talk to 3rd party servers via their APIs.
- Clean up state before tests run because there is no guarantee that `after` hooks will run, especially if their is an error in the test
- Use the `data-testid` HTML attribute to select elements on the page
- Avoid unnecessary use of `cy.wait`. Most Cypress functions automatically wait for a period of time that should be enough. Use may vary
- Set a `baseUrl` in your `cypress.json` file

For more information, visit the 
[Cypres Best Practices page](https://docs.cypress.io/guides/references/best-practices.html)

### Folder structure

```
cypress.json
package.json
cypress
├── README.md
├── fixtures
│   ├── DummyPic.png
│   └── users.json
├── integration
│   ├── Login
│   │   ├── AdminLogin
│   │   │   └── AdminLogin.js
│   │   └── AdminLogin.feature
│   └── common
│       └── index.js
├── pages
│   │   ├── AdminLoginPage.js
│   │   └── LoginPage.js
│   └── Page.js
├── plugins
│   └── index.js
└── support
    ├── commands.js
    └── index.js
```

### Files

`cypress.json`
```javascript
{
    "baseUrl": "http://localhost:3000",
    "chromeWebSecurity": false,
    "defaultCommandTimeout" : 10000,
    "numTestsKeptInMemory": 5,
    "testFiles": "**/*.feature"
}

```

`package.json`
```javascript
  "scripts": {
    // Additional commands
    "test:e2e:open": "cypress open",
    "test:e2e": "cypress run --env TAGS='@e2e-test' --spec 'cypress/integration/**/*.feature'"
  }
  "cypress-cucumber-preprocessor": {
    "nonGlobalStepDefinitions": true
  }
```

`fixtures/users.json`

```javascript
{
  "admin": {
    "email": "me@example.com",
    "password": "super_secret"
  },
}
```

`integration/Login/AdminLogin.feature`
```gherkin
Feature: Admin Login
  As an Admin
  I can log in
  So that I can access and modify system info

  Background:
    Given I have an Admin account
    And I'm on the Admin Login page

  @e2e-test
  Scenario: Valid credentials
    When I enter my email and password
    And I press the "Login" button
    Then I see the Admin Dashboard page
    When I log out
    Then I see the Admin Login page
```

`integration/common/index.js`
```javascript
import { Given, When, Then } from 'cypress-cucumber-preprocessor/steps';

// NOTE: this account should be seeded in the backend database.
Given(`I have a Admin account`, () => {});

// Additional step definitions below...
```

`integration/Login/AdminLogin/AdminLogin.js`
```javascript
import { Given, When, Then } from 'cypress-cucumber-preprocessor/steps';
import AdminLoginPage from '../../../pages/Login/AdminLoginPage';

When(`I enter my email and password`, () => {
  AdminLoginPage.enterValidCredentials();
});

// Additional step definitions below...
```

`pages/Page.js`
```javascript
class Page {
  static visit() {
    cy.visit(this.path());
  }

  /**
   * The URL path for the page.
   * NOTE: This should be overridden in each subclass.
   *
   * @returns {string}
   */
  static path() {
    return '';
  }
}

export default Page;
```

`pages/Login/AdminPage.js`
```javascript
import * as users from '../../fixtures/users';
import Page from '../Page';

class AdminLoginPage extends Page {
  static path() {
    return '/admin/login';
  }

  static user() {
    return users.admin;
  }

  static enterValidCredentials() {
    cy.get('[data-testid=login-email-input]').type(this.user().email);
    cy.get('[data-testid=login-password-input]').type(this.user().password);
  }
}

export default AdminLoginPage;
```

`plugins/index.js`
```javascript
const cucumber = require('cypress-cucumber-preprocessor').default;

module.exports = (on, config) => {
  // `on` is used to hook into various events Cypress emits
  // `config` is the resolved Cypress config
  on('file:preprocessor', cucumber());
};
```

`support/commands.js`
```javascript
/**
 * Programmatically login a user.
 *
 * @link https://docs.cypress.io/guides/getting-started/testing-your-app.html#Logging-in
 *
 * @param {string} userType is the type of user being logged out.
 * @param {object} options  additional options to modify login behavior.
 * @example
 * cy.login('admin')
 */
Cypress.Commands.add('login', (userType, options = {}) => {
  cy.fixture('users').then(users => {
    const { email, password } = users[userType];

    cy
      .request({
        method: 'POST',
        url: 'http://localhost:3000/admin/login',
        body: { email, password },
      })
      .then(resp => {
        // Add additional login logic...
        cy.wrap(resp.body.data).as('currentUser');
      });
  });
});

/**
 * Programmatically logout the current user.
 */
Cypress.Commands.add('logout', () => {
  cy.request({
    method: 'DELETE',
    url: 'http://localhost:3000/admin/logout',
  });
  // Add additional logout logic...
});

/**
 * Assert the current URL.
 *
 * @param {string} path The path portion of the URL.
 * @example
 * cy.currentUrlShouldBe('/companies')
 */
Cypress.Commands.add('currentUrlShouldBe', path => {
  cy.url().should('eq', Cypress.config().baseUrl + path);
});

/**
 * Access contents of an iframe.
 *
 * @link https://bit.ly/2OHw2lq
 *
 * @param {string} iframeSelector The CSS selector for the iframe.
 * @param {string} elSelector The element to be selected in iframe.
 * @example
 * cy.iframe('[title="Calendar"]').as('calenderIframe')
 * cy.get('@calenderIframe').find('.Calendar__day').eq(0).click()
 */
Cypress.Commands.add('iframe', (iframeSelector, elSelector = 'body') => {
  return cy
    .get(`iframe${iframeSelector || ''}`, { timeout: 10000 })
    .should($iframe => {
      expect($iframe.contents().find(elSelector)).to.exist
    })
    .then($iframe => {
      return cy.wrap($iframe.contents().find('body'))
    })
});
```

### Additional info

1. [Additional Cypress recipes](https://docs.cypress.io/examples/examples/recipes.html)
1. [File uploading](https://github.com/abramenal/cypress-file-upload)

### FAQs

- When to use `cy.contains()`?
    - If you want the test to fail when the content changes then use `cy.contains()`. Otherwise use a data attribute

See more [Cypress Best Practices](https://docs.cypress.io/guides/references/best-practices.html)

## Examples

1. [Integrate Cypress and Cucumber in your development flow](https://bit.ly/323KLLj)
   1. [Cypress cucumber example repo](https://github.com/jmarti-theinit/cypress-cucumber-example)
   1. [Google search feature](https://github.com/jmarti-theinit/cypress-cucumber-example/blob/master/cypress/integration/google/search.feature)

```bash
# Opens the Cypress Test Runner in interactive mode.
# https://docs.cypress.io/guides/guides/command-line.html#cypress-open
npx cypress open

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
