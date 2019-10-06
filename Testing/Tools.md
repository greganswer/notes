# Tools

## Cypress

**Advantages**

- It is easy to install Cypress. It is easy to write tests with it. It is very easy to debug tests. It is easy to include it in continuous integration or continuous delivery pipelines.
- Can be run in parallel [with some additional setup](https://docs.cypress.io/guides/guides/parallelization.html)

**Disadvantages**

- only supports Chrome
- No native event handling capabilities.
- Such as upload, download file, tab key, etc. This is one feature that we genuinely miss, and its lack gets more noticeable as the app grows. Native events don’t actually handle our killer features, but we’d feel more secure if we could at least test them in our end-to-end tests.

## Minitest

- Full backend test suite takes almost 13 minutes to run (as of Thu, Oct 3, 2019)

**Advantages**

**Disadvantages**

**Possible plugins**

- https://github.com/seattlerb/minitest-sprint
- https://github.com/seattlerb/minitest-focus
- https://github.com/teoljungberg/minitest-fail-fast
- https://github.com/seattlerb/minitest-debugger

## RSpec

**Advantages**

- Creating a matrix of different scenarios is easy through shared contexts, lets and the example hooks (before, after, around)

**Disadvantages**

- Takes longer to learn the DSL since it is not pure Ruby
- Tests take longer and have a larger memory footprint