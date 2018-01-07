# Regular Expressions

- [Regular Expressions](#regular-expressions)
    - [Examples](#examples)
        - [Phone number attempt](#phone-number-attempt)
        - [CSS hex color](#css-hex-color)
        - [Floats and integers](#floats-and-integers)
    - [References and tools](#references-and-tools)

```ruby
# Ignore the group while capturing `?:`
'ab' =~ /(?:ab)/ #=> 0

# Positive look ahead `?=`
'cool cat' =~ /cool(?=\ cat)/ #=> 0
'cool dog' =~ /cool(?=\ cat)/ #=> nil

# Negative look ahead `?!`
'cool dog' =~ /cool(?!\ cat)/ #=> 0
'cool cat' =~ /cool(?!\ cat)/ #=> nil

# Positive look behind `?<=`
'cool cat' =~ /(?<=cool\ )cat/ #=> 5
'cool dog' =~ /(?<=cool\ )cat/ #=> nil

# Negative look behind `?<!`
'silly cat' =~ /(?<!cool\ )cat/ #=> 6
'cool cat' =~ /(?<!cool\ )cat/ #=> nil

# Back reference - `\1` or `$1`
'me@new-example.com'.gsub!(/.*@([a-z0-9_-]+)\.\w*/i, '\1') #=> "new-example"
'me@new-example.com'.gsub!(/.*@([a-z0-9_-]+)\.\w*/i, $1) #=> "new-example"
'https://www.new-example.com'.gsub!(/(?:https?)?(?:\:\/\/)?(?:www\.)?([a-z0-9_-]+)(\.\w*)/i, '\1\2') #=> "new-example.com"
```

```html
# Match in a non-greedy way
<p>.*?</p>
```

## Examples

### Phone number attempt

```ruby
\D*(\d{1,2}*)(.*\d{,3})(\d{3}).*(\d{4})

(\+\d{1,2}.?)?
^(\+?\d{1,2}?).*(?\d{3}).*(\d{3}).*(\d{4})

# Matches the following:
# 123-4567
# 1234567
# 123-456-7890
# (123) 456-7890
# +1 123 456 7890
# 5043 850 924 3850

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
# Matches: -1, .05, +1000, 3.14159, 42., .+4 (without the dot)
```

## References and tools

1. [Ruby regular expression tool](http://rubular.com/)
1. [Intro to regular expressions (Udemy)](https://www.udemy.com/regex-academy-an-introduction-to-text-parsing-sorcery)
1. [Beginner regular expressions video (YouTube)](https://www.youtube.com/watch?v=sa-TUpSx1JA)
1. [Intermediate regular expressions video (YouTube)](https://www.youtube.com/watch?v=EkluES9Rvak)
1. [Regular expression tutorial](https://www.tutorialspoint.com/ruby/ruby_regular_expressions.htm)