#!/usr/bin/env bash
export $(cat .env | xargs)

gcloud builds submit \
    --config .cloudbuild/deployment.yaml\
    --region=asia-northeast1\
	--substitutions=TAG_NAME="${TAG_NAME}",\
_COMPILE_FILE="${COMPILE_FILE}",\
_PIPELINE_NAME="${PIPELINE_NAME}",\
_REGISTRY_PATH="${REGISTRY_PATH}"