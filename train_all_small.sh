#!/bin/bash

YAML_FILE=models.yaml

# Determine config file to use
CONFIG_FILE="./config.yaml"
[[ ! -f "$CONFIG_FILE" ]] && CONFIG_FILE="config_default.yaml"

# Extract the data path
DATA_PATH=$(yq '.COCO_PATH' "$CONFIG_FILE")
DATA_YAML="${DATA_PATH%/}/coco.yaml"

MODELS=$(yq '.small[]' "$YAML_FILE")

for MODEL in $MODELS; do
  echo "Training with model: $MODEL"
  python train.py \
    --model_name "$MODEL" \
    --data_yaml "$DATA_YAML" \
    --epochs 15 \
    --img_size 640
done