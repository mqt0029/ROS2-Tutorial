# ROS 2 Humble Tutorial

This repository contains the Dockerfile for ROS 2 Humble with basic simulation support to get you
started with ROS 2.

## Quick Start

For resource limited systems, just run the following commands

1. (Optional) Remove all existing containers

```
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
```

2. Run container accessible via NoVNC Web Browser

```
git clone https://github.com/mqt0029/ROS2-Tutorial.git && ./ROS2-Tutorial/Docker/run_container.sh --minimal
```

and your development environment will be accessible at [`http://localhost:6080`](http://localhost:6080). The password will be `myrobotsim`.

Otherwise, follow the detailed setup instructions for your specific system below.

Pick your development platform and follow the instructions that follows.

1. [Native Ubuntu 22.04](./Guides/ubuntu_setup.md)
2. [WLS2 Ubuntu 22.04 on Windows 11](./Guides/windows_setup.md)
3. [MacOS](./Guides/macos_setup.md)

## System Requirements

### Minimum Requirements

- 8GB RAM
- 4 CPU Cores
- 20GB Disk Space

### Recommended Requirements

- 16GB RAM
- 8 CPU Cores
- 50GB Disk Space
- NVIDIA GPU or at least Intel HD or Iris Pro Graphics

## Supported Platforms

- Ubuntu 22.04 (with or without NVIDIA GPU)
- WLS2 Ubuntu 22.04 on Windows 11 (with or without NVIDIA GPU)

> 🛠️ MacOS support is currently under development.

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
