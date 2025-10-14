#!/bin/zsh
source ../.env
ROO_FILE="$1"
roo run $ROO_FILE --api-key $ROO_API_KEY
