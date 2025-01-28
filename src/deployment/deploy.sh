#!/bin/bash
SERVER="ubuntu@147.189.202.22"
KEY="RatAnseela_JohnQ1"
PASSWORD="RatAnseela_JohnQ1"
REMOTE_DIR="/home/ubuntu/eliza-python-deploy"



# Accept the program name as a command-line argument
PROGRAM=$1
if [ -z "$PROGRAM" ]; then
  echo "Error: Please provide the Python program name (e.g., ./deploy.sh program.py)"
  exit 1
fi
PID_FILE="${PROGRAM}.pid"

# Copy the Python program to the server
sshpass -p $PASSWORD scp -i $KEY $PROGRAM $SERVER:$REMOTE_DIR




# SSH into the server, navigate to the directory, and run the program
sshpass -p $PASSWORD ssh -i $KEY $SERVER "
cd $REMOTE_DIR && nohup python3 $PROGRAM > program.log 2>&1 &
echo \$! > $PID_FILE
"




