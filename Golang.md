Go Language
=====

- [Go Language](#go-language)
  - [Installation](#installation)
  - [Folder Structure](#folder-structure)
  - [General](#general)

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

## General

```bash
# Show all environment variables
go env
```