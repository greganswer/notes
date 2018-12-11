# Programming Principles 

## Programmer's oath

Reference: [Uncle Bob's Programmer's Oath](https://blog.cleancoder.com/uncle-bob/2015/11/18/TheProgrammersOath.html)

1. Don't produce harmful code
1. Avoid bugs
1. Write tests (preferably first)
1. Make small frequent releases
1. Refactor and improve frequently
1. Improve productivity for you and your team
1. Continuously transfer knowledge to reduce the bus factor
1. Always give a ranged estimate (Ex: This will take 2-4 days)
1. Continuously learn and improve

## Personal workflow

1. QA the current application (end-to-end)
   1. Check if fix/feature already exists 
   1. Check if there is a workaround
1. Commit Driven Development - write the Git commit message before coding
1. Changelog Driven Development - update the Changelog before coding
1. Document Driven Development - create/update documentation before coding
1. Write integration tests as pseudo-code comments for these scenarios
   1. Write Given When Then scenarios
   1. Write acceptance tests as pending tests
   1. TDD the functions you plan to create/update 
1. Write the code
   1. Write console logs instead of comments
   1. Console log inputs and outputs for each function as necessary
1. Refactor tests 
   1. DRY it up
   1. Remove comments
   1. Consider edge cases
1. Refactor code 
   1. DRY it up
   1. Remove comments
1. QA the application (end-to-end) 
   1. Ensure that the fix/feature works 
   1. Check if anything related broke (regressions)
   1. Make sure performance is acceptable
1. Update documentation
   1. Commit message
   1. Changelog 
   1. README files, Confluence docs, etc.

## SOLID principles

- **Single Responsibility Principle (SRP):** every function, module, and class should have responsibility over a single part of the functionality.

```ruby
# bad
def deal_processor(deal)
  commission_amount = deal.price * 0.15
  if Commission.create(deal: deal, amount: commission_amount)
    deal.processed = true
    deal.save!
  end
end

# good
COMMISSION_PERCENTAGE = 0.15

def deal_processor(deal)
  return false unless commission_processor(deal)
  deal.processed = true
  deal.save!
end

def commission_processor(deal)
  Commission.create(deal: deal, amount: commission_amount(deal.price))
end

def commission_amount(price)
  price * COMMISSION_PERCENTAGE
end
```

- **Open-closed Principle:** 

```ruby
# bad - the login function has to change when the Gun or Web login functionality changes.
def login(username, password, source)
  case source
  when :gun
    # 20 lines of code...
  when :web
    # 10 lines of code...
  else
    invalid_source_error
  end
end

# better - the login function only changes when a new login source is added.
def login(username, password, source)
  case source
  when :gun
    gun_login(username, password)
  when :web
    web_login(username, password)
  else
    invalid_source_error
  end
end

def gun_login(username, password)
  # 20 lines of code...
end

def web_login(username, password)
  # 10 lines of code...
end
```

- **Liskov's Substitution Principle:** Subclasses should add to a parent classes behaviour, without needing to replace it

```ruby
# Bad - Penguin MUST override the fly() function in a very different way.
class Bird
  def has_wings?
    true
  end

  def fly
    # Flying logic...
  end
end

class Pigeon < Bird; end

class Penguin < Bird
  def fly
    raise CannotFlyError
  end
end

# Better
class Bird
  def has_wings?
    true
  end
end

module FlyingBird
  def fly
    # Flying logic...
  end
end

class Pigeon < Bird
  include FlyingBird
end

class Penguin < Bird; end
```

- **Inversion of Control Principle (IoC):** No client should be forced to depend upon methods it does not use

```ruby
```

- **Dependency Inversion Principle (DIP):** everything inside of a function should come from outside of it

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