#!/usr/bin/env bash

IMAGE_NAME=mqt0029/ros2-tutorial
IMAGE_TAG=ubuntu
CONTAINER_NAME=ros2-tutorial-container
CONTAINER_ID=`docker ps -aqf "name=^/${CONTAINER_NAME}$"`

# if container does not exist, create it
if [ -z "${CONTAINER_ID}" ]; then

    docker run \
    --tty \
    --detach \
    --name ${CONTAINER_NAME} \
    --privileged \
    --gpus all \
    --env DISPLAY=$DISPLAY \
    --env WAYLAND_DISPLAY=$WAYLAND_DISPLAY \
    --env XDG_RUNTIME_DIR=$XDG_RUNTIME_DIR \
    --env PULSE_SERVER=$PULSE_SERVER \
    --volume /tmp/.X11-unix:/tmp/.X11-unix \
    --volume /mnt/wslg:/mnt/wslg \
    --volume /usr/lib/wsl:/usr/lib/wsl \
    ${IMAGE_NAME}:${IMAGE_TAG}

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
