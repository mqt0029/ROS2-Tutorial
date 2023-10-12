# Setup Instructions for MacOS

> :warning: EXPERIMENTAL: This guide is still in development and may not work as expected.

## 1. Prerequisites

- Docker Desktop for Mac
- Homebrew Package Manager
- `git` installed via Homebrew

To install Docker, see https://docs.docker.com/desktop/install/mac-install/.

To install Homebrew, see https://brew.sh/.

Afterwards, install `git` via Homebrew.

```
$ brew install git
```

> :warning: WARNING: There is no way to test whether the M1 or M2 version would work, because I don't have
> access to an M1 or M2 machine. If you have an M1 or M2 machine, please test it out and let me
> know.

## 2. Running the Docker Container

### 2.1 Verify Docker Installation

In a terminal, run the following command. **Your output should mostly match the output shown**.

```
$ docker run --tty --rm hello-world
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

$
```

### 2.2 Clone the repository

Run the following command to clone the repository.

```
$ git clone https://github.com/mqt0029/ROS2-Tutorial.git
$ cd ROS2-Tutorial
```

### 2.3 Create the Docker container

The `run_container.sh` script will allow you to create, start, and attach to the container when
opening new terminals. Running this script for the first time will create the container:

```
user@DESKTOP:~/ROS2-Tutorial$ ./run_container.sh
[container hash]

user@DESKTOP:~/ROS2-Tutorial$
```

At this point, the container is created and running, but is not attached to any terminal. To access
the container, you will be using NoVNC via a web browser.

### 2.4 Accessing the container

Open your preferred web browser and navigate to `http://localhost:6080`. You should see a page that
allows you to access the container. Click "Connect", and you will be prompted for a password, which
is `myrobotsim`.

## :tada: Congratulations! You are now ready!

Continue to [First Steps](./first_steps.md) to get started with ROS2!
