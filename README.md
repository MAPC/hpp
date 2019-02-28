# Housing Production Plan (HPP) Tool

### Running GUI inside of Docker on macOS

Macs don't have a fully accessible X server since they use all of their own proprietary windowing programs that wrap around X11. You have to install a couple of tools
on macOS for the GUI version of this app to work. 

#### Install 
```sh
brew cask install xquartz
brew install socat
```

You will have to pipe your X11 socket to an available port so Docker can have access to it.
```sh
open -a XQuartz
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\" &
```

Change your $DISPLAY environment variable to reflect the new location by using your local IP address.
```sh
ifconfig | grep 'inet 192.168.' # should see something like "en1 192.168.x.x netmask 0xffffff00 broadcast 192.168.1.255"

# Use your local IP for the display location
export DISPLAY="<local-ip>:0"
```

Now you may run `bin/run` from the repo root!
