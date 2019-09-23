# React

## Summary

## Details

- Was open sourced by Facebook in 2013
- Update single page apps without making as many requests to the server
- Was created to handle the complexity of web development

### React core concepts

- Don't touch the Document Object Model (DOM). I'll do it.
    - Previous JavaScript frameworks were imperatively changing nodes in the DOM.
    - Declare what the page should look like and React will handle it.
    - Hold the state of the large JavaScript object and React to the changes
- Build websites like Lego blocks
    - Create components and reuse them
    - Plain JavaScript functions that return something that looks like HTML (JSX)
- Unidirectional data flow
    - You pass state and components to the React function which creates a Virtual Document Object Model
    - This Tree like object contains all the information required to render the real DOM
    - When the state changes, the information flows down to all the child nodes

### Keys to being a great React developer

1. Determine what components to create/reuse
1. Determine the state and where it lives
1. Determine what changes when state changes

### State management

- When state changes, the child components get re-rendered
- State management is asynchronous
    - If you need to use the state value after the update, use the callback parameter in the `setState` method
    - If you need to use the state value as part of setting state, pass a function as the first parameter
    - Otherwise use the simple object notation (most common)

### State management with Redux

3 Principles:
1. Single source of truth
1. State is read only
1. Changes using pure functions

Redux flow

| Term                | Definition                                               |
| ------------------- | -------------------------------------------------------- |
| **1. Action**       | When a user takes action in the application              |
| **2. Root Reducer** | A function that receives an action and outputs the state |
| **3. Store**        | The entire state of the application                      |
| **4. DOM changes**  | This happens as a result of the state change             |

### Lifecycle methods

- It's important to understand the lifecyle methods in order enhance performance
    - http://projects.wojtekmaj.pl/react-lifecycle-methods-diagram

## References

- https://blog.logrocket.com/understanding-redux-saga-from-action-creators-to-sagas-2587298b5e71
- https://devhints.io/react
- https://github.com/sudheerj/reactjs-interview-questions
