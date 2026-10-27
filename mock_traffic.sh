#!/bin/bash

while true; do
    curl -s http://localhost:8080 > /dev/null

    # random sleep time to simulate mock traffic
    random_sleep=$(awk 'BEGIN {print rand() * 2}')
    sleep "$random_sleep"
done
