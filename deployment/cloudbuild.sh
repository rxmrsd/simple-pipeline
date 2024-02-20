#!/usr/bin/env bash
export $(cat .env | xargs)

gcloud builds submit . \
	--config .cloudbuild/deployment_component.yaml \
	--substitutions="_TAG"="latest",\
"_BUILD_ACCOUNT"="${BUILD_ACCOUNT}"

gcloud builds submit . \
	--config .cloudbuild/deployment_pipeline.yaml \
	--substitutions="_PROJECT_ID"="${PROJECT_ID}",\
"_LOCATION"="${LOCATION}",\
"_PIPELINE_ROOT"="${PIPELINE_ROOT}",\
"_SERVICE_ACCOUNT"="${SERVICE_ACCOUNT}",\
"_BUILD_ACCOUNT"="${BUILD_ACCOUNT}",\
"_REGISTRY_PATH"="${REGISTRY_PATH}"