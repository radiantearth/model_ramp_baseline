#!/usr/bin/env bash

set -e

if [[ -z "${INPUT_DATA}" ]]; then
    echo "INPUT_DATA environment variable is not defined"
    exit 1
fi

if [[ -z "${OUTPUT_DATA}" ]]; then
    echo "OUTPUT_DATA environment variable is not defined"
    exit 1
fi

python model_ramp_bootstrap/get_model_predictions.py \
    --model_dir=${INPUT_DATA}/checkpoint.tf \
    --images_dir=${INPUT_DATA}/chips \
    --output_dir=${OUTPUT_DATA}
