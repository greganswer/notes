# Programming Principles 

- [Programmer's oath](#programmers-oath)
- [Personal workflow](#personal-workflow)
- [Programming Principles](#programming-principles)
- [References](#references)

## Programmer's oath

Reference: [Uncle Bob's Programmer's Oath](https://blog.cleancoder.com/uncle-bob/2015/11/18/TheProgrammersOath.html)

1. **Don't produce harmful code**
1. **Avoid bugs**
1. **Write tests** (preferably first)
1. **Make small frequent releases**
1. **Refactor and improve frequently**
1. **Improve productivity for you and your team**
1. **Continuously transfer knowledge** to reduce the bus factor
1. **Always give a ranged estimate** (Ex: This will take 2-4 days)
1. **Continuously learn and improve**

**Avoid bugs**
- Write tests
- Write simple, readable code
- Use clear names
- Follow best practices (convention over configuration)

**Continuously transfer knowledge**
- Pair programming
- Written documentation
- Weekly demos

## Personal workflow

| Step | Title                             | Details                                                                            |
| ---- | --------------------------------- | ---------------------------------------------------------------------------------- |
| 1.   | **QA the application**            | Does the fix/feature already exist? Is there a workaround?                         |
| 2.   | **Write the Commit**              | Write the Git commit message before coding                                         |
| 3.   | **Update the Changelog**          | Update the Changelog before coding                                                 |
| 4.   | **Write Documentation**           | Create/update documentation before, during, and after coding                       |
| 5.   | **Pseudo-code acceptances tests** | Write pending tests in pseudo-code `Given/When/Then` comments                      |
| 6.   | **Write the tests and code**      | Write console log statements for behavior instead of comments                      |
| 7.   | **Consider edge cases**           | Document and discuss edge cases                                                    |
| 8.   | **QA the application**            | Ensure the fix/feature works, check regressions (functionality, performance, etc.) |
| 9.   | **Refactor**                      | DRY it up, Remove unnecessary comments                                             |
| 10.  | **Update documentation**          | CHANGELOG.md, README.md files, Confluence docs, etc.                               |

## Programming Principles

1. Always test the empty state of objects
    ```python
    stack = Stack()
    self.assertIsNone(stack.peek())
    self.assertTrue(stack.is_empty())
    self.assertEqual(len(stack), 0)
    ```
1. Always check that the object is present before accessing its values
    ```python
    if self.list:
        return self.list[-1]
    if self.top:
        return self.top.data
    ```

## References

1. [Google's documentation style guide](https://github.com/google/styleguide/tree/gh-pages/docguide
