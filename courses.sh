#!/bin/bash

# Author: Saksham Sharma
# 12th March, 2016

# Usage:
# ./courses.sh <roll_num>
roll=$1

# Send CURL request to doaa scheduler
# Keep it as close to the browser request as possible to prevent detection.
output=$(curl -s "http://172.26.142.68/examscheduler2/personal_schedule.php?rollno=$roll" -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: en-US,en;q=0.8' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.8 Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' -H 'Referer: http://172.26.142.68/examscheduler2/personal.html' --compressed)

# Parse the single line output with a large incomprehensible RegEx I wrote today and will forget tomorrow.
echo $output | grep -E "<tr><td>([^<]*)</td>" -o | grep -E ">([^<]+)<" -o | grep -E "[^><]*" -o
