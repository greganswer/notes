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

## References
