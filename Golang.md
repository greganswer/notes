Go Language
=====

- [Go Language](#go-language)
  - [Installation](#installation)
  - [Folder Structure](#folder-structure)
  - [Hello world](#hello-world)
  - [Terminal commands](#terminal-commands)
  - [General](#general)
  - [Variables](#variables)
  - [Constants](#constants)
  - [Functions](#functions)
  - [Scopes](#scopes)

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
```

## Scopes

Levels: universe, package, file, block (curly braces)