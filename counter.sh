#!/bin/bash

count=0
for item in /etc/* /etc/.*; do
    if [ -f "$item" ] && [ ! -L "$item" ]; then
        count=$((count + 1))
    fi
done

echo "Number of regular files in /etc: $count"
