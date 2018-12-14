# Docker for Mac

## Instal

```bash
brew tap phinze/homebrew-cask
brew install brew-cask
brew cask install docker

open /Applications/Docker.app
```

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