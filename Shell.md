## Basics

Apparently, every shell script should have some elements of the following:

```bash
#!/usr/bin/env bash

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
for run in {1..10}
do
  command
done
```

```bash
# Or as a one-liner for those that want to copy and paste easily:
for run in {1..10}; do command; done
```

## Exit Traps

Similar to Golang defer keyword.

```bash
function finish {
    # re-start service
    sudo service mongdb start
}
trap finish EXIT
# Stop the mongod instance
sudo service mongdb stop
```

**Reference:** 

- [Run a script n times](https://bit.ly/2HU6dgd)
- [Bash scripting best practices](https://bit.ly/2DcGHNI)
- [Bash exit traps](http://redsymbol.net/articles/bash-exit-traps/)