# Shell Scripting (Bash)

## Special characters

| Character | Description |
|--------:|:------------|
| **#**  | A comment. |
| **\*** | Wildcard. |
| **\\** | Escape character. |
| **.**  | The current directory. |
| **..** | The parent directory. |
| **:**  | The null command [colon]. This is the shell equivalent of a "NOP" *(no op, a do-nothing operation)*. It may be considered a synonym for the shell builtin true. The ":" command is itself a Bash builtin, and its exit status is true (0). |
| **$?** | The exit status of a command, a function, or of the script itself |
| **$$** | The process ID of the script in which it appears. |

## Commands

| Command | Description |
|:--------|:------------|
| **cp [OPTION]... SOURCE... DIRECTORY** | Copy source(s) to destination. |

## Basics

Apparently, every shell script should have some elements of the following:

```bash
#!/usr/bin/env bash
#
# Here's the description for this file.

set -o errexit # Stop the script when an error occurs.
set -o pipefail # `error here | true` will fail if this is enabled.
set -o nounset # Detect uninitialized variables and exit with an error.
[[ "${DEBUG}" == 'true' ]] && set -o xtrace # Print expressions before execution if `DEBUG=true`.
```

## Modules

In a file called `shared_functions.sh` you might have the following:

```bash
container() {
  eval "docker-compose exec app $@"
}
```

Then in your `bin/setup` script file you could do the following:

```bash
# The non standard functions in this script can be found in the local source file below.
readonly BINPATH="$(dirname "$0")"
source "${BINPATH}/shared_functions.sh"

container "rails restart"
```

## Loop

```bash
for run in {1..10}; do
  command
done
```

```bash
# Or as a one-liner for those that want to copy and paste easily:
for run in {1..10}; do command; done
```

## Error Handling

### Debugging

```bash
# Print expressions before execution if `DEBUG=true`.
# Detect uninitialized variables and exit with an error.
# Stop the script when an error occurs.
[[ "${DEBUG}" == 'true' ]] && set -o xtrace && set -o nounset && set -o errexit 
```

### Exceptions

```bash
err() {
  echo "[$(date +'%Y-%m-%dT%H:%M:%S%z')]: $@" >&2
}

if ! do_something; then
  err "Unable to do_something"
  exit "${E_DID_NOTHING}"
fi
```

### Exit Traps

The use case looks similar to Golang `defer` keyword but it behaves like Ruby's `rescue` keyword.

```bash
function finish {
    # re-start service
    sudo service mongdb start
}
trap finish EXIT
# Stop the mongod instance
sudo service mongdb stop
```

## Redirection

| Command | Description 
|:--------|:------------
| `scriptname > filename`  | Redirects the output of `scriptname` to file `filename`. Overwrite `filename` if it already exists.
| `command &> filename`    | Redirects both the stdout and the stderr of command to filename.
| `scriptname >> filename` | Appends the output of `scriptname` to file `filename`. If `filename` does not already exist, it is created.

## Linting

Use `shellcheck` utility. Intallation: `brew install shellcheck`. Given a script named *my_script* run 
`shellcheck my_script`.

**Reference:** 

- [Run a script n times](https://bit.ly/2HU6dgd)
- [Bash scripting best practices](https://bit.ly/2DcGHNI)
- [Bash exit traps](http://redsymbol.net/articles/bash-exit-traps/)
- [Writing Robust Shell Scripts](https://bit.ly/2Shpkpk)
- [Google Shell Style Guide](https://google.github.io/styleguide/shell.xml)
- [Best Practices for Writing Bash Scripts](https://bit.ly/2RMNsel)
- [Six Bash commands](https://astrobiomike.github.io/bash/six_commands)
- [Special characters](https://www.tldp.org/LDP/abs/html/special-chars.html)
- [13 Tips for Writing Shell Scripts with Awesome UX (Medium)](https://bit.ly/2GrjZW2)
- [Log 4 Bash](https://github.com/fredpalmer/log4bash/blob/master/log4bash.sh)
- [progrium/bashstyle](https://github.com/progrium/bashstyle)
- [Defensive Bash Programming](https://jonlabelle.com/snippets/view/markdown/defensive-bash-programming)
- [alexanderepstein/Bash-Snippets](https://github.com/alexanderepstein/Bash-Snippets)