gcloud builds submit \
    --config .cloudbuild/deployment.yaml\
    --region=asia-northeast1\
    --substitutions=TAG_NAME="test",\
_COMPILE_FILE="src/compile_pipeline.py",\
_PIPELINE_ROOT="gs://ml-development-temp/pipeline_job",\
_PIPELINE_NAME="message-publisher",\
_REGISTRY_PATH="https://asia-northeast1-kfp.pkg.dev/ml-guild-sandbox/sample-pipelines",\