# Homebrew

Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's macOS operating system and Linux. It's written in Ruby and the name means *building software based on your tastes*.

The focus of this tool is to build packages from source using *"formulae"*. A formula is a Ruby script constructed using a Domain Specific Language (DSL). It is used for managing dependencies, downloading source code, and configuring/compiling software.

Homebrew installs packages to their own directory and then symlinks the files into the `/usr/local` directory. All files and directories in the `/usr/local` directory have their ownership changed by Homebrew. This is considered a security risk by some in the community.

## Terms and Definitions

Term | Description | Example
-----|-------------|-------------
**Formula** | The package definition | /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core/Formula/foo.rb
**Keg** | The installation prefix of a Formula | /usr/local/Cellar/foo/0.1
**opt prefix** | A symlink to the active version of a Keg | /usr/local/opt/foo
**Cellar** | All Kegs are installed here | /usr/local/Cellar
**Tap** | A Git repository of Formulae and/or commands | /usr/local/Homebrew/Library/Taps/homebrew/homebrew-core
**Bottle** | Pre-built Keg used instead of building from source | qt-4.8.4.mavericks.bottle.tar.gz
**Cask** | An extension of Homebrew to install macOS native apps | /Applications/MacDown.app/Contents/SharedSupport/bin/macdown
**Brew Bundle** | An extension of Homebrew to describe dependencies | brew 'myservice', restart_service: true

## References

- [Homebrew Wikipedia page](https://bit.ly/2Vwo8PL)
- [Homebrew terms](https://bit.ly/2GPw70T)