#!/bin/bash

clear
echo "Here we go!"

echo "wait for 20s to connect to wifi..."
sleep 20

echo "Checking wifi connection..."

web="www.google.com"
/bin/ping -q -c1 $web > /dev/null

if [ $? -eq 0 ]
then
  echo "Network is active!"

else
  echo "Network is NOT active. Please check connection."
fi

sleep 2

sudo python /home/pi/SmokeDetector/connect_to_Arduino.py
