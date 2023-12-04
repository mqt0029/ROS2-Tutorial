#!/usr/bin/env bash

docker run \
--interactive \
--tty \
--rm \
--detach \
--publish 6080:6080 \
mqt0029/ros2-tutorial:macos
