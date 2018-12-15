# Docker for Mac

## Install

```bash
brew tap phinze/homebrew-cask
brew install brew-cask
brew tap caskroom/cask
brew cask install docker

open /Applications/Docker.app
```

## Config



## Complete Uninstall 

```bash
brew cask uninstall docker
```

```bash
sudo rm -Rf /Applications/Docker
sudo rm -f /usr/local/bin/docker
sudo rm -f /usr/local/bin/docker-machine
sudo rm -f /usr/local/bin/docker-compose
sudo rm -f /usr/local/bin/docker-credential-osxkeychain
sudo rm -Rf ~/.docker
sudo rm -Rf $HOME/Library/Containers/com.docker.*
```

## References

1. [Docker compose and rails](https://docs.docker.com/compose/rails/)
1. [Docker ps formatting](https://docs.docker.com/engine/reference/commandline/ps/)
1. [Docker config formatting](https://container42.com/2016/03/27/docker-quicktip-7-psformat/)
1. [Docker ps formatting](https://docs.docker.com/engine/reference/commandline/ps/#formatting)
