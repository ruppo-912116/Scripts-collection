#!/bin/bash

# Send desktop notification (requires proper DISPLAY and user session)
USER_ID=$(id -u)
export DISPLAY=:0
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$USER_ID/bus

/usr/bin/notify-send "Docker Cleanup" "cleaning up dangling objects and cache"

# Cleanup Docker resources
echo "$(date): Starting Docker cleanup..."

# Remove dangling images, containers, networks, and build cache
docker system prune -f --volume

# Optional: Remove all unused images (not just dangling)
# docker image prune -a -f

echo "$(date): Docker cleanup completed."
