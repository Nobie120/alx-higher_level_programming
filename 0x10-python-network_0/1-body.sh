#!/bin/bash
# GET method
curl -s -w "%{http_code}%" "$1" | awk '/^200$/{getline;print}'
