#!/bin/bash

  to=$1
  msg=$2
  tgpath=/home/pi/tg
  result = 0 

#  sudo python connect_to_arduino.py
#  while True:
#  if  result > 100,
	 cd ${tgpath}
	(sleep 3;echo "get_self";sleep 2 ; echo "msg $to $msg"; echo "safe_quit") | ${tgpath}/bin/telegram-cli -k tg-server.pub -W



##  ${tgpath}/bin/telegram-cli -k tg-server.pub -W | (echo "msg $to $msg"; echo "safe_quit")

#if smoke dector detect the smoke "people smoking"
#else dont send message

