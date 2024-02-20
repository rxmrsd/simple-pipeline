#!/usr/bin/env bash

COMPONENT_LIST=(
    "bq-component"
    "display-component"
)

# 各コンポーネントごとにdocker build
for COMPONENT in "${COMPONENT_LIST[@]}"
do
    COMPONENT_DIR=$(pwd)/components/${COMPONENT}
    # build docker image
    docker build -t ${COMPONENT}:latest -f ${COMPONENT_DIR}/Dockerfile .

    # component image name
    IMAGE_NAME=asia-northeast1-docker.pkg.dev/${GCP_PROJECT_ID}/soloban/${COMPONENT}

    # push image to Artifact Registory
    docker tag ${COMPONENT}:latest ${IMAGE_NAME}:${TAG}
    docker push ${IMAGE_NAME}:${TAG}

    # exit if failed to build or deploy image
    if [ $? -ne 0 ]; then
        echo "ERROR: ["${IMAGE_NAME}:${TAG}"] docker push was failed!!"
        exit 1
    fi
done