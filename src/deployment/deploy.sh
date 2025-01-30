#!/bin/bash
SERVER="ubuntu@147.189.202.22"
KEY=""
PASSWORD=""
REMOTE_DIR="/home/ubuntu/eliza-python-deploy"
IMAGE_NAME=$(basename "$PWD")  # Get the current directory name (used as image name)
# Get the full path of the current directory
CURRENT_PATH=$(pwd)



# Ensure a deployment method is provided
if [ -z "$1" ]; then
    echo "Error: No deployment method specified. Use '--docker' or provide a Python file."
    exit 1
fi

sshpass -p $PASSWORD rsync -avz -e "ssh -i $KEY" ./ $SERVER:$REMOTE_DIR/$IMAGE_NAME




# Check deployment method
if [ "$1" == "--docker" ]; then
    ssh -i $KEY $SERVER << EOF
        cd $REMOTE_DIR/$IMAGE_NAME

        mkdir -p logs output

        docker build -t $IMAGE_NAME .
        docker stop $IMAGE_NAME || true
        docker rm $IMAGE_NAME || true

        docker run -d --name $IMAGE_NAME -p 8080:8080 \
            -v $REMOTE_DIR/$IMAGE_NAME/output:/app/output \
            $IMAGE_NAME \
            &> logs/${IMAGE_NAME}_container.log &

        echo "Docker deployment successful!"
EOF

elif [[ "$1" == *.py ]]; then
    FILE_NAME="$1"
    ssh -i $KEY $SERVER << EOF
        cd $REMOTE_DIR/$IMAGE_NAME
        mkdir -p logs
        nohup python3 $FILE_NAME &> logs/python_script.log &
        echo "Python script '$FILE_NAME' is running in the background."
EOF

else
    echo "Error: Invalid deployment option. Use '--docker' or provide a Python script filename."
    exit 1
fi