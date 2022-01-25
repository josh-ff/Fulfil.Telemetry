# LabJack Interface
Facilitates interfacing with LabJack products

## Dev Interface
Developer interface is facilitated via Makefile and Docker.
### Compilation:
`make image` - builds lab-jack-interfacer docker image
### Execution:
`make run` - runs lab-jack-interfacer docker image
### Structure:
* `Makefile` - Interface for high level build / deploy / exec commands
* `Dockerfile` - Specifies image strucutre. Inspired by [ljm_docker](https://github.com/labjack/ljm_docker)
* `code/` - contains code executed during image runtime. `code/main.py` should remain program entrypoint as specified in `Dockerfile`


## Useful tools, collect Labjack Knowledge:
* [Kipling](https://labjack.com/support/software/installers/ljm) LabJack software to update FW on devices and see things like device IP and serial number

* FW must be updated on T4 devices on bringup. [LabJack instructions](https://labjack.com/support/firmware/t4) for doing so here

## TODOs:
* figure out network solution, likely all LabJack devices should live on same subnet. Owner - Byron 
* implement trivial data pull from device and pub up to cloud. Owner - Eric H