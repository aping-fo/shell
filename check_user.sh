#!/bin/bash

if [ $EUID -ne 0 ]; then
  echo "please run as root"
else
  echo "go work"
fi
