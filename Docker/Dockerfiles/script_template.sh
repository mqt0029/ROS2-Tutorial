#!/usr/bin/env bash

IMAGE_NAME="mqt0029/ros2-tutorial"
CONTAINER_NAME="rvl-ros2-tutorial-container"
CONTAINER_ID=`docker ps -aqf "name=^/${CONTAINER_NAME}$"`

#@@@@@ EXPORT_PLACEHOLDER

if [ -z "${CONTAINER_ID}" ]; then
#@@@@@ IF_PLACEHOLDER
else
#@@@@@ ELSE_PLACEHOLDER
fi
