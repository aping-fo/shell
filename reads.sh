#!/bin/bash
# 控制等待输入的时间 -t Second
if read -t 5 -p "please input your name" name;
then
  echo "${name} ,welcome"
else
  echo "sorry"
exit 0

# 控制输入字符长度 -nNumber Number表示控制字符的长度,超过则read命令立即接受输入并将其传给变量。无需按回车键。
read -n1 -p "do you agree with me [Y/N]" ans
case $ans in
Y/y )
  echo "Y"
N|n)
  echo "N"
*)
  echo "other"
esac;

# 读取文件,通过cat file 配合管道处理,如 cat file | while read line
count=1
if read -p "choice ou file:" yourfile; then
  cat $yourfile | while read line
  do
    echo "line $count:$line"
    let count++
  done 
  exit 0
else
  echo "none"
  exit 0
