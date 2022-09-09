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

echo "generate raster (.tif) building masks..."
python model_ramp_baseline/get_model_predictions.py \
    --model_dir=${INPUT_DATA}/checkpoint.tf \
    --images_dir=${INPUT_DATA}/chips \
    --output_dir=${OUTPUT_DATA}

echo "generate polygon (.geojson) building masks from raster masks..."
python model_ramp_baseline/polygonize_multimasks.py \
    --input_dir=${OUTPUT_DATA} \
    --output_dir=${OUTPUT_DATA}/raw_polygonized_buildings/

echo "remove small slivers (<2m^2) from polygons..."
python model_ramp_baseline/remove_slivers.py \
    --label_file_dir=${OUTPUT_DATA}/raw_polygonized_buildings/ \
    --filtered_file_dir=${OUTPUT_DATA}/ \
    --min_sqmeters=2

echo "cleanup..."
rm -rf ${OUTPUT_DATA}/raw_polygonized_buildings
