# Setup Instructions for Windows

## 1. Prerequisites

- Windows 11
- WSL2
- Docker Desktop
- NVIDIA GPU (optional) with latest drivers
- Intel GPU (optional) with latest drivers

Typically, modern laptop (think post 2018) will have both NVIDIA and Intel GPUs. If you have a
desktop, you may only have an NVIDIA GPU. If you have an older laptop, you may only have an Intel
GPU.

Assuming you have a fresh or mostly unmodified version of latest Windows 11 with all the necessary
updates pre-installed (as in, Windows does this for you anyway):

### 1.1 Install or update to WSL2

In an elevated PowerShell terminal, run the following command:

```console
wsl --install -d Ubuntu-22.04
```

This will install as WSL2 by default. If you have WSL1, see [Official WSL1 to WLS2
instruction](https://learn.microsoft.com/en-us/windows/wsl/install#upgrade-version-from-wsl-1-to-wsl-2).

Restart your machine, and finish the WSL2 setup as instructed.

### 1.2 Install Docker Desktop

Download and install Docker Desktop from https://docs.docker.com/desktop/install/windows-install/.

You will be asked to restart again. Afterwards, verify that your Ubuntu terminal has access to
Docker.

### 1.3 Install latest graphics driver

For NVIDIA, go to https://www.nvidia.com/download/index.aspx.

For Intel, https://www.intel.com/content/www/us/en/download-center/home.html.

### 1.4 (Optional) Limited Resouce Configuration

If you have limited system resources i.e. low RAM or CPU count, you can adjust how much Docker
Desktop can use by defining a `.wslconfig` file in your Windows home directory.

For example, if your system has a 4-core/8-thread CPU and 16GB of RAM, you can limit Docker Desktop
to use only 8GB of RAM and 4 logical cores by creating a `.wslconfig` file with the following content

```
[wsl2]
memory=8GB
processors=4
```

and place it in `C:\Users\<your username>\.wslconfig`. Afterwards, force restart WLS2 and Docker by
**running the following command in Powershell**

```console
wsl --shutdown
```

To verify that the configuration is applied, run the following command in a new Ubuntu bash terminal

```console
user@DESKTOP:~$ sudo apt install -y htop && htop
```

You should see that the total memory available is 8GB and the total number of logical cores is 4.

## 2. Running the Docker Container

### 2.1 Verify Docker Installation

In an Ubuntu terminal, run the following command. **Your output should mostly match the output shown**.

```console
user@DESKTOP:~$ docker run --tty --rm hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
719385e32844: Pull complete
Digest: sha256:4f53e2564790c8e7856ec08e384732aa38dc43c52f02952483e3f003afbf23db
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

user@DESKTOP:~$
```

### 2.2 Clone the repository

In an Ubuntu terminal, run the following command to clone the repository.

```console
user@DESKTOP:~$ sudo apt -y install git
user@DESKTOP:~$ git clone https://github.com/mqt0029/ROS2-Tutorial.git
user@DESKTOP:~$ cd ROS2-Tutorial
```
### 2.3 Create the Docker container

Before you create a container, make sure WSL will use your desired GPU. If you have both NVIDIA and
Intel, WSL2 might enumerate them in the wrong order, which may result in NVIDIA GPU not being
utilized. To fix this, run the following command in your Ubuntu terminal:

```console
echo "export MESA_D3D12_DEFAULT_ADAPTER_NAME=NVIDIA" >> ~/.bashrc && source ~/.bashrc
```

This will force WSL2 to use the NVIDIA GPU. If you have only an Intel GPU, you can skip this step.

The `run_container.sh` script will allow you to create, start, and attach to the container when
opening new terminals. Running this script for the first time will create the container:

```console
user@DESKTOP:~/ROS2-Tutorial$ ./run_container.sh
[container hash]

user@DESKTOP:~/ROS2-Tutorial$
```

At this point, the container is created and running, but is not attached to any terminal. You can
run the script again for the current and any subsequent terminals to attach to the container.

```console
user@DESKTOP:~/ROS2-Tutorial$ ./run_container.sh

root@[container_hash]:~/colcon_ws$
```

> 🗒️ **NOTE**: The script can be run from anywhere, so you do not have to `cd` into the repository
> to run it!

## :tada: Congratulations! You are now ready!

Continue to [First Steps](./first_steps.md) to get started with ROS2!
