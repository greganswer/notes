# Shell Scripting (Bash)

Shells are command interpreters. They are applications that provide users with the ability to give commands to their operating system interactively, or to execute batches of commands quickly. In no way are they required for the execution of programs; they are merely a layer between system function calls and the user.

Think of a shell as a way for you to speak to your system. Your system doesn't need it for most of its work, but it is an excellent interface between you and what your system can offer.

BASH is not your operating system. It is not your window manager. It is not your terminal (but it often runs inside your terminal). It does not control your mouse or keyboard. It does not configure your system, activate your screensaver, or open your files when you double-click them. It is generally not involved in launching applications from your window manager or desktop environment. It's important to understand that BASH is only an interface for you to execute statements (using BASH syntax), either at the interactive BASH prompt or via BASH scripts.

The header is called an interpreter directive (it is also called a hashbang or shebang). It specifies that /bin/bash is to be used as the interpreter when the file is used as the executable in a command. When the kernel executes a non-binary file, it reads the first line of the file. If the line begins with #!, the kernel uses the line to determine the interpreter to relay the file to. (There are other valid ways to do this as well, see below.) The #! must be at the very start of the file, with no spaces or blank lines before it. Our script's commands will appear on separate lines below this.

## Glossary

| Term           | Definition                                                                                                                                                                                   |
| :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Shell**      | A (possibly interactive) command interpreter, acting as a layer between the user and the system                                                                                              |
| **Bash**       | The Bourne Again Shell, a Bourne compatible shell                                                                                                                                            |
| **Script**     | A sequence of commands in a file                                                                                                                                                             |
| **Alias**      | A word that is mapped to a string. Whenever that word is used as a command, it is replaced by the string it has mapped.                                                                      |
| **Function**   | A name that is mapped to a set of commands. Whenever the function is used as a command, it is called with the arguments following it. Functions are the basic method of making new commands. |
| **Builtin**    | Certain commands have been built into Bash. These are handled directly by the Bash executable and do not create a new process.                                                               |
| **Executable** | A program that can be executed by referring to its file path (e.g. /bin/ls), or simply by its name if its location is in the PATH variable.                                                  |

## Special characters

| Character | Description                                                                                                                                                                                                                                |
| --------: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     **#** | A comment.                                                                                                                                                                                                                                 |
|    **\*** | Wildcard or Glob.                                                                                                                                                                                                                          |
|    **\\** | Escape character.                                                                                                                                                                                                                          |
|     **.** | The current directory.                                                                                                                                                                                                                     |
|     **?** | Test operator (ternary operator).                                                                                                                                                                                                          |
|     **[** | A Bash builtin that tests a condition.                                                                                                                                                                                                     |
|    **[[** | A Bash keyword that tests a condition.                                                                                                                                                                                                     |
|    **..** | The parent directory.                                                                                                                                                                                                                      |
|     **:** | The null command [colon]. This is the shell equivalent of a "NOP" *(no op, a do-nothing operation)*. It may be considered a synonym for the shell builtin true. The ":" command is itself a Bash builtin, and its exit status is true (0). |
|    **$?** | The exit status of a command, a function, or of the script itself                                                                                                                                                                          |
|    **$$** | The process ID of the script in which it appears.                                                                                                                                                                                          |

## Commands

| Command                                | Description                    |
| :------------------------------------- | :----------------------------- |
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

# Set magic variables for current file & dir
__dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
__file="${__dir}/$(basename "${BASH_SOURCE[0]}")"
__base="$(basename "${__file}")"
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

| Command                  | Description                                                                                                 |
| :----------------------- | :---------------------------------------------------------------------------------------------------------- |
| `scriptname > filename`  | Redirects the output of `scriptname` to file `filename`. Overwrite `filename` if it already exists.         |
| `command &> filename`    | Redirects both the stdout and the stderr of command to filename.                                            |
| `scriptname >> filename` | Appends the output of `scriptname` to file `filename`. If `filename` does not already exist, it is created. |

## Linting

Use `shellcheck` utility. Intallation: `brew install shellcheck`. Given a script named *my_script* run 
`shellcheck my_script`.

## References

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
- [BashGuide](https://mywiki.wooledge.org/BashGuide)
- [Good Coding Practices for Bash](https://bit.ly/2DKOUc9)
- [Output redirection](https://skorks.com/2009/09/output-redirection-with-bash)
- [When to use STDERR instead of STDOUT](https://bit.ly/2kCABkm)
- [Shell Script Template](https://natelandau.com/boilerplate-shell-script-template)
- [Shell FAQs](https://mywiki.wooledge.org/BashFAQ/035)