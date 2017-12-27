Linux
=======

- [Linux](#linux)
  - [General](#general)
  - [Environment Variables](#environment-variables)
  - [Folders](#folders)
  - [Files](#files)
  - [Processes](#processes)
  - [SSH](#ssh)

## General

```bash
# Download a file from the web
wget https://localhost/file.txt
```

## Environment Variables

```bash
# Show all variables
env

# Add a variable
export VAR_NAME="value"

# Show contents of a variable
echo $PATH

# Delete a variable
unset VAR_NAME
```

## Folders

```bash
# Make multiple directories in current folder
mkdir bin pkg src

# Make a directory with multiple sub directories
mkdir -p parent_folder/{bin,pkg,src}
```
**Reference:** https://askubuntu.com/questions/731721/is-there-a-way-to-create-multiple-directories-at-once-with-mkdir

## Files

```bash
# Make multiple files in current folder
touch a.txt b.txt c.txt

# Append the text "Hello World" to the file
echo "Hello World" >> my_file.txt

# Search for text "error" in "my_file.txt"
grep "error" my_file.txt
```

## Processes

```bash
# Status of current session
ps

# All Running
ps aux

# Processes running that match the pattern "mongo"
ps aux | grep mongo

# Using most CPU
top

# Stop foreground process
Ctrl-c

# Stop a process by PID
kill -9 3243
```

## SSH