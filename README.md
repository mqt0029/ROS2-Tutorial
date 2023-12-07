# ROS 2 Humble Tutorial

This repository contains the Dockerfile for ROS 2 Humble with basic simulation support to get you
started with ROS 2.

## Quick Start

### 1. Install Docker

Follow the instructions on the [Docker website](https://docs.docker.com/get-docker/) to install for
Windows or Mac.

For native Linux, the same instructions may be used, but `docker.io` on apt would suffice.

```console
$ sudo apt install docker.io docker-compose python3-dev python3-pip python3-tk
```

> 🗒️ If you are on Linux, be sure to follow [Docker Post-Installtion
> Steps](https://docs.docker.com/engine/install/linux-postinstall/).

> :spiral_notepad: If you have NVIDIA GPU, be sure to install and configure
> 1. For native Linux, [NVIDIA Container Toolkit for
Docker](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt).
> 2. For WSL2 on Windows 11, [CUDA 12.1 for WSL2](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local).

### 2. Clone this repository

```console
$ git clone https://github.com/mqt0029/ROS2-Tutorial.git
```

### 3. Generate scripts for your specific platform

A convenient `config_generator.py` script is provided to generate the necessary scripts for your
specific host OS and GPU availability. The script will generate a `run.sh` script that will be used
to create and attach to the tutorial container going forward.

> :warning: This script needs the module `tkinter` to run, install it either through `pip` or `apt`

```console
$ cd ROS2-Tutorial/Docker && python3 config_generator.py
```

See [this README](Docker/README.md) for more details.

### 4. Run the container

The `run.sh` script is designed to automatically create and attach to the container with the
appropriate image and tag. You do not need to run anything else except this script to get your
terminal into the container.

```console
$ /path/to/this/repository/Docker/run_container.sh
```

### 5. Continue with the tutorial

🎉🎉🎉 Congratulations! You are now in the container and ready to start the tutorial. Continue with the [ROS
2 Tutorials](https://docs.ros.org/en/humble/Tutorials.html) or follow the [ROS 2 Progression Guide](GUIDES.md).

## Troubleshooting

### 1. Gazebo not starting

On WSL2, if you are seeing error `D3D12: Device Removed.` and Gazebo is not showing the GUI windows,
you may need to update your WSL2 kernel as well as your graphics driver. This is known to happen to Intel Iris Xe graphics.

In an elevated PowerShell, run the following commands:

```console
PS> wsl --update --pre-release
```

Additionally, download and install latest driver from [Intel's
website](https://www.intel.com/content/www/us/en/download/785597/intel-arc-iris-xe-graphics-windows.html?wapkw=Iris%20Xe).

## Resources

These are useful websites, cheatsheets, or tutorials that you can use to learn more about ROS 2 or
just the use of Linux in general.

1. [Learn X in Y minutes](https://learnxinyminutes.com): Aggregated language/feature summary for a
   lot of programming languages and tools.
2. [Rico's cheatsheets](https://devhints.io): Aggregated cheatsheets for a lot of programming
   languages and tools.
3. [Docker cheatsheet](https://docs.docker.com/get-started/docker_cheatsheet.pdf): Official Docker
   cheatsheet for Docker Command Line Interface (CLI).
4. [Wargame Bandit](https://overthewire.org/wargames/bandit/): A wargame that teaches you the basics
   of Linux command line.
5. [GitHub Awesome Awesome](https://github.com/sindresorhus/awesome): A curated list of "awesome" resources.

### WSL2 Specific Documentation

1. [WSL2 Documentation](https://docs.microsoft.com/en-us/windows/wsl)
2. [WSLg Container Configuration](https://github.com/microsoft/wslg/blob/main/samples/container/Containers.md)
3. [WSLg GPU Selection](https://github.com/microsoft/wslg/wiki/GPU-selection-in-WSLg)

### ROS Specific Documentation

1. [ROS 2 Documentation](https://docs.ros.org/en/humble/index.html)
2. [ROS Docker Hardware Acceleration](http://wiki.ros.org/docker/Tutorials/Hardware%20Acceleration)
3. [ROS GUI with Docker](http://wiki.ros.org/docker/Tutorials/GUI)
4. [ROS 2 Community](https://discourse.ros.org/)
