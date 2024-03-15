#!/bin/sh

EXEC="./chall"
PORT=1337

socat -dd -T300 tcp-l:$PORT,reuseaddr,fork,keepalive exec:"$EXEC",stderr,su="nobody"
