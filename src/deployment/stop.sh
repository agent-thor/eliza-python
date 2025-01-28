#!/bin/bash
SERVER="ubuntu@147.189.202.22"
KEY="RatAnseela_JohnQ1"
PASSWORD="RatAnseela_JohnQ1"
REMOTE_DIR="/home/ubuntu/eliza-python-deploy"

# Accept the program name as a command-line argument
PROGRAM=$1
if [ -z "$PROGRAM" ]; then
  echo "Error: Please provide the Python program name (e.g., ./stop.sh program.py)"
  exit 1
fi
PID_FILE="${PROGRAM}.pid"




# SSH into the server, navigate to the directory, and kill the process using the PID
sshpass -p $PASSWORD ssh -i $KEY $SERVER "
cd $REMOTE_DIR && 
if [ -f $PID_FILE ]; then 
  kill \$(cat $PID_FILE) && rm $PID_FILE; 
  echo 'Process stopped successfully.'; 
else 
  echo 'PID file not found. Process may not be running.'; 
fi
"
