#!/bin/bash
cat $1 | tr ' ' '\n' | sort | uniq -c | awk '{if($1 > 1) {print $2}}'
