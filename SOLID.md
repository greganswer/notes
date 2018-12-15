
# SOLID principles

- **Single Responsibility Principle (SRP):** every function, module, and class should have responsibility over a single part of the functionality.

```ruby
# Bad
def deal_processor(deal)
  commission_amount = deal.price * 0.15
  if Commission.create(deal: deal, amount: commission_amount)
    deal.processed = true
    deal.save!
  end
end

# Good
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

- **Open-closed Principle:** Classes and functions should be open for extension but closed for modification

```ruby
# Bad - the login function has to change when the Gun or Web login functionality changes.
def login(username, password, source)
  case source
  when :gun
    # some code...
  when :web
    # some code...
  else
    invalid_source_error
  end
end

# Better - the login function only changes when a new login source is added.
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
  # some code...
end

def web_login(username, password)
  # some code...
end

# Best - but it depends on your use case.
def login(username, password, login_function)
  login_function.call(username, password)
end

gun_login = lambda do |username, password|
  # some code...
end

login('jim', 'asdfasdf', gun_login)
```

- **Liskov's Substitution Principle:** Subclasses should add to a parent classes behaviour, without needing to replace it

```ruby
# Bad - Penguin MUST override the fly() function in a very different way.
class Bird
  def has_wings?
    true
  end

  def fly
    # some code...
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
    # some code...
  end
end

class Pigeon < Bird
  include FlyingBird
end

class Penguin < Bird; end
```

- **Interface Segregation Principle:** No client should be forced to depend upon methods it does not use

- **Dependency Inversion Principle (DI):** everything inside of a function should come from outside of it

```ruby
# Bad
def some_method
  x = some_object
  x.do_something
end

# Good
def some_method(x=nil)
  x ||= some_default_object
  x.do_something
end
```