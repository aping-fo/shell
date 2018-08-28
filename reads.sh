#!/bin/bash
# 控制等待输入的时间 -t Second
if read -t 5 -p "please input your name" name;
then
  echo "${name} ,welcome"
else
  echo "sorry"
exit 0
