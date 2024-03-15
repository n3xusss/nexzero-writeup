#!/bin/sh

EXEC="./run.sh"
PORT=3000

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr
