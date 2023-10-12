# Setup Instructions for Ubuntu

## 1. Prerequisites

- Ubuntu 22.04
- Git
- (Optional) NVIDIA GPU and `nvidia-container-toolkit` installed

### 1.1 Install Docker and Git

Open a terminal and run the following commands:

```
sudo apt update && sudo apt -y install docker.io git
```

Once that is done, complete [Linux post-installation
steps](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user).
In summary, run the following commands:

```
sudo groupadd docker && sudo usermod -aG docker $USER
```

Log out (or just restart), and log back in. Verify that you can run Docker without `sudo`:

```
newgrp docker && docker run --rm hello-world
```

Your output should mostly match the output shown.

```
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
```

### 1.2 (Optional) Install NVIDIA Container Toolkit

This step is only required if you have an NVIDIA GPU and want to use it with Docker. If you don't
have an NVIDIA GPU, skip this step.

Follow the [NVIDIA Container Toolkit Official
Instructions](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installing-with-apt),
or run the following commands:

1. Configure the repository:

```
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list \
  && \
    sudo apt-get update
```

2. Install the NVIDIA Container Toolkit packages:

```
sudo apt-get install -y nvidia-container-toolkit
```

3. Configure Docker

```
sudo nvidia-ctk runtime configure --runtime=docker
```

4. Restart Docker

```
sudo systemctl restart docker
```

5. Verify you have access to the GPU

```
sudo docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

You should see the somewhat similar output:

```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 535.86.10    Driver Version: 535.86.10    CUDA Version: 12.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla T4            On   | 00000000:00:1E.0 Off |                    0 |
| N/A   34C    P8     9W /  70W |      0MiB / 15109MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```

## 2. Running the Docker Container

### 2.1 Clone the repository

In an Ubuntu terminal, run the following command to clone the repository.

```
git clone https://github.com/mqt0029/ROS2-Tutorial.git && cd ROS2-Tutorial
```
### 2.2 Create the Docker container

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
