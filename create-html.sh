#!/bin/bash

path=$1

echo "<html>"

while IFS= read -r line; do
  if [[ $line == found:* ]] ;
  then
    file_path=${line:7}
    echo "<a href=\"file://$file_path\">"
    echo "   <img src=\"file://$file_path\" width=250 />"
    echo "</a>"
  fi
done <<< $(python ./is-pic-with-person.py --recursive "$path")

echo "</body></html>"
