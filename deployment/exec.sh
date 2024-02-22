#!/usr/bin/env bash
export $(cat .env | xargs)

poetry run python pipeline/src/exec_pipeline.py \
    --project="${PROJECT_ID}" \
    --location="${LOCATION}" \
    --pipeline_root="${PIPELINE_ROOT}" \
    --registry_template_path="${REGISTRY_PATH}/${PIPELINE_NAME}/${TAG_NAME}" \
    --table_id="${TABLE_ID}"