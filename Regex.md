# Regular Expressions

```ruby
# Ignore the group while capturing `?:`
'ab' =~ /(?:ab)/ #=> 0

# Look ahead - Only match an 'a' when a 'b' follows `?:`
'ab' =~ /a(?=b)/ #=> 0
'ba' =~ /a(?=b)/ #=> nil

# Negative look ahead - Only match an 'a' when it is not followed by a 'b' `?:`
'ba' =~ /a(?!b)/ #=> 0
'ab' =~ /a(?!b)/ #=> nil

# Back reference - `\1` or `$1`
'me@new-example.com'.gsub!(/.*@([a-z0-9_-]+)\.\w*/i, '\1') #=> "new-example"
'me@new-example.com'.gsub!(/.*@([a-z0-9_-]+)\.\w*/i, $1) #=> "new-example"
'https://www.new-example.com'.gsub!(/(?:https?)?(?:\:\/\/)?(?:www\.)?([a-z0-9_-]+)(\.\w*)/i, '\1\2') #=> "new-example.com"
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

### Floats and integers

```ruby
/([.+-]?\.?\d+.?)/
```
Matches: -1, .05, +1000, 3.14159, 42., .+4 (without the dot)

## References and tools

1. [Ruby regular expression tool](http://rubular.com/)
1. [Beginner regular expressions video](https://www.youtube.com/watch?v=sa-TUpSx1JA)
1. [Intermediate regular expressions video](https://www.youtube.com/watch?v=EkluES9Rvak)
1. [Regular expression tutorial](https://www.tutorialspoint.com/ruby/ruby_regular_expressions.htm)