Go Language
=====

- [Go Language](#go-language)
  - [Installation](#installation)
  - [Folder Structure](#folder-structure)
  - [Hello world](#hello-world)
  - [Terminal commands](#terminal-commands)
  - [General](#general)
  - [Variables](#variables)
    - [Scalar](#scalar)
    - [Reference](#reference)
  - [Constants](#constants)
  - [Functions](#functions)
  - [Scopes](#scopes)
  - [Conditional logic](#conditional-logic)

## Installation

1. Set the `GOROOT`
1. Add export `PATH=$PATH:/usr/local/go/bin` to `/etc/profile`
1. Add export `GOPATH=$HOME/<workspace_name>` to `~/.profile`
1. Add export `PATH=$HOME/<workspace_name>/bin:$PATH` to `~/.profile`

## Folder Structure

- go
  - bin
  - pkg
  - src
    - github.com
      - username
        - project repo 1
        - project repo 2

## Hello world

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello World")
}
```

## Terminal commands

```bash
# Show all environment variables
go env

# Format all files
go fmt

# Run the main file
go run main.go

# Build executable
go build

# Run the executable you just built
./main.exe

# Create a globally accessible executable
go install # The file will be placed in $HOME/<workspace_name>/bin
```

## General

- The folder name needs to be the same as the package name
- For something to be executable, it needs `package main` and `func main() {}`
- If the first letter of a function is capitalized, then this function will be exported (visible) outside the package 
- The `main.go` file with the `func main() {}` is the executable file. When you run `go build` from the terminal in that directory it will build the executable `main.exe` file in that directory

## Variables

### Scalar

- Shorthand syntax can only be used inside `func`
- Declared variables get set to their "zero" value

```go
// Declare a variable, then assign it a value
var x string // x is currently ''
x = "hello" // x is now hello

// Declared with shorthand
a:= 10
b:= "golang"

// Exported variable
var MyString = "hello" // Note the capitalization of the first letter
```

### Reference

- Slices hold references to an underlying array, and if you assign one slice to another, both refer to the same array. 
- If a function takes a slice argument, changes it makes to the elements of the slice will be visible to the caller, analogous to passing a pointer to the underlying array.

## Constants

```go
// Declare a single constant
const language = "Go"

// Declare multiple constants
const (
  pi = 3.14
  language = "Go"
)
```

## Functions

```go
// Declare a function of type string
func myFunc() string  { return "hello" } 

// Declare an exported function of type string
func MyFunc() string  { return "hello" } // Note the capitalization of the first letter

// Accept to string arguments and return multiple values
func fullName(first_name, last_name string) string {
  return fmt.Sprint(first_name, last_name), fmt.Sprint(last_name, first_name)
}
```

**Create a variadic function:**

```go
/*
Note the ellipsis prefix for the float64 type, denoting that this function
  accepts 0 or more arguments
*/
func average(sf ...float64) float64 {
  total := 0.0
  for _, v := range sf {
    total += v
  }
  return total / float64(len(sf))
}

/*
Note the ellipsis postfix for the float64 slice, denoting that the values
  will be split into a comma separated list
*/
data := []float64{43, 56, 12}
n := average(data...)
```

**Callbacks:**

```go
// The first parameter is a slice of integers
// The second parameter is a function that takes an int parameter
func visit(numbers []int, callback func(int)) {
  for _, v := range numbers {
    callback(v)
  }
}

func main() {
  // The first argument is a slice of integers
  // The second argument is an anonymous function that has an int argument
  visit([]int{1, 2, 3, 4}, func(n int) {
    fmt.Println(n)
  })
}
```

## Scopes

Levels: universe, package, file, block (curly braces)

## Conditional logic

```go
// Initialization statement in an if statement
b := true
if food := "Chocolate"; b {
  fmt.PrintLn(food)
}
// the food variable is not available outside the if block
```

```go
// Switch based on type
type Contact struct {
  greeting string
  name string
}
x := 42

switch x.(type) {
case int:
  fmt.Println("int")
case string:
  fmt.Println("string")
case Contact:
  fmt.Println("contact")
default:
  fmt.Println("unknown")
}
```