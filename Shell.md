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

## Linting

Use `shellcheck` utility. Intallation: `brew install shellcheck`.  
Given a script named `my_script` run `shellcheck my_script`

**Reference:** 

- [Run a script n times](https://bit.ly/2HU6dgd)
- [Bash scripting best practices](https://bit.ly/2DcGHNI)
- [Bash exit traps](http://redsymbol.net/articles/bash-exit-traps/)
- [Writing Robust Shell Scripts](https://bit.ly/2Shpkpk)
- [Google Shell Style Guide](https://google.github.io/styleguide/shell.xml)