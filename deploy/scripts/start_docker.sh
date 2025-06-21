#!/bin/bash
# Login to AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 869935088600.dkr.ecr.us-east-1.amazonaws.com
docker pull 869935088600.dkr.ecr.us-east-1.amazonaws.com/skyx-ecr:v4

if [ "$(docker ps -q -f name=skyx-app)" ]; then
    docker stop my-container || true
fi

if [ "$(docker ps -aq -f name=skyx-app)" ]; then
    docker rm my-container || true
fi

docker run -d -p 80:5000 -e DAGSHUB_PAT=eac8585ad4083e279c466bd0514fffdf07054e30 --name skyx-app 869935088600.dkr.ecr.us-east-1.amazonaws.com/skyx-ecr:v4