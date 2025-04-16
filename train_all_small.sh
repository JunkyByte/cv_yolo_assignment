#!/bin/bash

YAML_FILE=models.yaml
MODELS=$(yq '.small[]' "$YAML_FILE")

for MODEL in $MODELS; do
  echo "Training with model: $MODEL"
  python train.py \
    --model_name "$MODEL" \
    --models_yaml models.yaml \
    --data_yaml /home/adryw/dataset/coco_cv/coco/coco.yaml \
    --epochs 30 \
    --img_size 640
done