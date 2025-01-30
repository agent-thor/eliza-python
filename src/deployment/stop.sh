#!/bin/bash

SERVER="ubuntu@147.189.202.22"
KEY=""
PASSWORD=""
REMOTE_DIR="/home/ubuntu/eliza-python-deploy"
IMAGE_NAME=$(basename "$PWD")  # Get the current directory name (used as image name)

# Ensure an action is provided
if [ -z "$1" ]; then
    echo "Error: No action specified. Use '--docker' to stop the container or provide a Python file to stop the script."
    exit 1
fi

if [ "$1" == "--docker" ]; then
    ssh -i $KEY $SERVER << EOF
        docker stop $IMAGE_NAME || true
        docker rm $IMAGE_NAME || true
        echo "Docker container '$IMAGE_NAME' stopped and removed."
EOF

elif [[ "$1" == *.py ]]; then
    FILE_NAME="$1"
    ssh -i $KEY $SERVER << EOF
        pkill -f "python3 $FILE_NAME"
        echo "Python script '$FILE_NAME' stopped."
EOF

else
    echo "Error: Invalid stop option. Use '--docker' or provide a Python script filename."
    exit 1
fi
