#!/bin/bash

  to=$1
  msg=$2

  tgpath=/home/pi/tg

  cd ${tgpath}
##  (echo "msg $to $msg"; echo "safe_quit")|sleep 10 | ${tgpath}/bin/telegram-cli -k tg-server.pub -W
  (sleep 3 ; echo "get_self"; sleep 2; echo "msg $to $msg") | ${tgpath}/bin/telegram-cli -k tg-server.pub -W
