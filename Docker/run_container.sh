#!/usr/bin/env bash

# some of the snippets here are borrowed
# hippity hoppity, this script is now my property
# https://unix.stackexchange.com/a/25131

# exit on error
set -e

# case-insensitive matching
shopt -s nocasematch

IMAGE_NAME="mqt0029/ros2-tutorial"
CONTAINER_NAME="rvl-ros2-tutorial-container"
CONTAINER_ID=`docker ps -aqf "name=^/${CONTAINER_NAME}$"`

# if the flag --minimal is passed
if [[ $1 == "--minimal" ]]; then
    # if container does not exist, create it
    if [ -z "${CONTAINER_ID}" ]; then
        docker run -i -t -d -p 6080:6080 \
        --name ${CONTAINER_NAME} \
        ${IMAGE_NAME}:macos
    else
        # if container exists but is not running, start it
        if [ -z `docker ps -qf "name=^/${CONTAINER_NAME}$"` ]; then
            docker start ${CONTAINER_ID}
        fi
    fi
    exit 0
fi

# ---------------------------------------------------------------------------- #
#                  CASE 1: WE'RE ON UBUNTU ON WSL2 ON WINDOWS                  #
# ---------------------------------------------------------------------------- #

if [[ "$(< /proc/version)" == *@(microsoft|wsl)* ]] &> /dev/null ; then
    # if container does not exist, create it
    if [ -z "${CONTAINER_ID}" ]; then
        docker run \
        --tty \
        --detach \
        --name ${CONTAINER_NAME} \
        --device /dev/dxg \
        --device /dev/dri/card0 \
        --device /dev/dri/renderD128 \
        --volume /tmp/.X11-unix:/tmp/.X11-unix \
        --volume /mnt/wslg:/mnt/wslg \
        --volume /usr/lib/wsl:/usr/lib/wsl \
        --env DISPLAY=$DISPLAY \
        --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
        --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
        --env PULSE_SERVER=$PULSE_SERVER \
        ${IMAGE_NAME}:wsl2
    else
        # if container exists but is not running, start it
        if [ -z `docker ps -qf "name=^/${CONTAINER_NAME}$"` ]; then
            docker start ${CONTAINER_ID}
        fi
        # enter container
        docker exec -it ${CONTAINER_ID} bash
    fi

# ---------------------------------------------------------------------------- #
#                      CASE 2: WE'RE ON SOME KIND OF LINUX                     #
# ---------------------------------------------------------------------------- #

elif [[ "$OSTYPE" == "linux-gnu"* ]]; then

    # if container does not exist, create it
    if [ -z "${CONTAINER_ID}" ]; then
        # check if we're on Ubuntu or not
        DISTRO=$( ( lsb_release -ds || cat /etc/*release || uname -om ) 2>/dev/null | head -n1 )
        # if we are, check if we have access to an NVIDIA GPU
        if [[ "$DISTRO" == *"Ubuntu"* ]]; then
            GPU=$(lspci | grep -i '.* vga .* nvidia .*')
            # if we do have access to an NVIDIA GPU, use the nvidia-docker image
            if [[ $GPU == *' nvidia '* ]]; then
                IMAGE_TAG="ubuntu_nvidia"
                    docker run \
                    --tty \
                    --detach \
                    --name ${CONTAINER_NAME} \
                    --gpus all \
                    --runtime nvidia \
                    --privileged \
                    --volume /tmp/.X11-unix:/tmp/.X11-unix \
                    --env DISPLAY=$DISPLAY \
                    ${IMAGE_NAME}:${IMAGE_TAG}
            # otherwise, use the regular (Intel) image
            else
                    docker run \
                    --tty \
                    --detach \
                    --name ${CONTAINER_NAME} \
                    --gpus all \
                    --device /dev/dri:/dev/dri \
                    --privileged \
                    --volume /tmp/.X11-unix:/tmp/.X11-unix \
                    --env DISPLAY=$DISPLAY \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                IMAGE_TAG="latest"
            fi
        # if we're not on Ubuntu, yell bloody murder and exit
        else
            echo "Unsupported Linux distro: $DISTRO"
            exit 1
        fi

    else
        # container already exists...
        # allow UI spawning through X server
        xhost +local:`docker inspect --format='{{ .Config.Hostname }}' ${CONTAINER_ID}`
        # if container exists but is not running, start it
        if [ -z `docker ps -qf "name=^/${CONTAINER_NAME}$"` ]; then
            docker start ${CONTAINER_ID}
        fi
        # enter container
        docker exec -it ${CONTAINER_ID} bash
        # disallow UI spawning through X server
        xhost -local:`docker inspect --format='{{ .Config.Hostname }}' ${CONTAINER_ID}`
    fi

# ---------------------------------------------------------------------------- #
#                            CASE 3: WE'RE ON MAC OS                           #
# ---------------------------------------------------------------------------- #

elif [[ "$OSTYPE" == "darwin"* ]]; then
    # if container does not exist, create it
    if [ -z "${CONTAINER_ID}" ]; then
        docker run \
        --tty \
        --detach \
        --publish 6080:6080 \
        --name ${CONTAINER_NAME} \
        ${IMAGE_NAME}:macos
    else
        # if container exists but is not running, start it
        # no need to attach, we'll be using NoVNC on browser
        if [ -z `docker ps -qf "name=^/${CONTAINER_NAME}$"` ]; then
            docker start ${CONTAINER_ID}
        fi
    fi
    echo "Connect to http://localhost:6080/ on your browser to access the container."
fi

# ---------------------------------------------------------------------------- #
#                                   CODE DUMP                                  #
# ---------------------------------------------------------------------------- #

# check if we have access to an NVIDIA GPU
# if [[ "$(command -v nvidia-smi)" ]]; then
#     IMAGE_TAG="ubuntu-nvidia"
# else
#     IMAGE_TAG="ubuntu"
# fi

# # check if we're on Ubuntu or not
# DISTRO=$( ( lsb_release -ds || cat /etc/*release || uname -om ) 2>/dev/null | head -n1 )
# # if we are, check if we have access to an NVIDIA GPU
# if [[ "$DISTRO" == *"Ubuntu"* ]]; then
#     GPU=$(lspci | grep -i '.* vga .* nvidia .*')
#     # if we do have access to an NVIDIA GPU, use the nvidia-docker image
#     if [[ $GPU == *' nvidia '* ]]; then
#         IMAGE_TAG="ubuntu_nvidia"
#     # otherwise, use the regular (Intel) image
#     else
#         IMAGE_TAG="latest"
#     fi
# # if we're not on Ubuntu, yell bloody murder and exit
# else
#     echo "Unsupported Linux distro: $DISTRO"
#     exit 1
# fi
