# Regular Expressions

```ruby
# Ignore the group while capturing `?:`
/(?:ab)/
```

## Examples

### Phone number attempt

```ruby
\D*(\d{0,2}*).*(.*\d{,3}*)(\d{3}).*(\d{4})
```

### CSS hex color

```ruby
/^#(?:[a-f\d]{3}){1,2}$/i
```

Captures | Ignores
---------|---------------
#abc     |  #BADA55 with a space in front
#f00     | F043295
#C00FEE  | ASD
#BADA55  | #ASD
#FFF     | #abca
