#!/usr/bin/env bash

# Start the X server
Xvfb $DISPLAY -screen 0 1920x1080x16 &

# Start the XFCE4 desktop environment
startxfce4 &

# Set a password for x11vnc (you can customize this)
x11vnc -storepasswd "myrobotsim" /tmp/vncpass

# Start the VNC server (connecting it to the X server)
x11vnc -xkb -noxrecord -noxfixes -noxdamage -display $DISPLAY -forever -bg -rfbport $VNC_PORT -rfbauth /tmp/vncpass -localhost

# Start noVNC
/opt/novnc/utils/novnc_proxy --vnc localhost:$VNC_PORT &

# Keep the container running
tail -f /dev/null
