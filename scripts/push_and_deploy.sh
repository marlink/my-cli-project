#!/bin/zsh
source ../.env
MSG="$1"
git add .
git commit -m "$MSG"
git push origin main
gcloud config set project $GCLOUD_PROJECT
