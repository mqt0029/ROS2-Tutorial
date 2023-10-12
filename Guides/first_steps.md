# Getting Familiar with ROS 2 Humble

This guide serves as a quick start guide to get you up and running with ROS 2 Humble where you will
learn basic concepts and tools to get you started with robotic development.

## 0. A Fresh Start

If at any point in time your container broke or not working correctly, you can always remake and
rerun the provided `run_container.sh` script. This will create a new container and attach to it.

```
docker stop $(docker ps -a -q) && docker container prune
```

Accepting will stop and remove all containers. You can then run the `run_container.sh` script again
until you reach the `root@[container_hash]:~/colcon_ws$` prompt.

## 1. Getting VS Code

VS Code, while not required, does have a very nice toolset that allows you to attach to running
container, where you can browse files, write code, and run commands. This is a very nice feature and
definitely worth the time to set up.

### 1.1 Installing VS Code

To install VS Code, you can follow the instructions on the [VS Code website](https://code.visualstudio.com/).

### 1.2 Install VS Code Extensions

You will need the following extensions:

- [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

Once these are installed, you will see a new icon in the left sidebar that indicates you can attach
to "remote" hosts, in our case, a container.

![](../Media/dev_container.mp4)

### 1.3 Install VS Code Extensions inside Container

Once you have VS Code installed, you will need to install some more extensions inside the container

- [C/C++](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [CMake](https://marketplace.visualstudio.com/items?itemName=twxs.cmake)
- [CMake Tools](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cmake-tools)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [ROS](https://marketplace.visualstudio.com/items?itemName=ms-iot.vscode-ros)

You are now ready to develop!

## 2. Going through the tutorials

Continue to https://docs.ros.org/en/humble/Tutorials.html and follow through until you reach
"Writing a simple service and client (Python)" under "Beginner: Client libraries". This is to
guarantee you are familiar with the ROS terminology and tools, as well as understanding fundamental
concepts of ROS 2 such as nodes, topics, publishers, and subscribers.
