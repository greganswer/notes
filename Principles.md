# Programming Principles 

## Personal workflow

1. QA the current application (end-to-end). Check if fix/feature already exists or has a workaround
1. Write out Given When Then scenarios
1. Write integration tests as pseudo-code comments for these scenarios
1. Write input and output logs as you go
1. Write the code
1. Refactor tests (DRY, remove comments, etc.)
1. Refactor code (DRY, remove comments, etc.)
1. QA the application (end-to-end) to ensure that the fix/feature works and does not break anything else (regressions)
1. Check if end-to-end performance for the fix/feature is acceptable

## SOLID principles

- Dependency inversion: everything inside of a function should come from outside of it

```ruby
# bad
def some_method
  x = some_object
  x.do_something
end

# good
def some_method(x=nil)
  x ||= some_default_object
  x.do_something
end
```