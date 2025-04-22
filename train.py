import os
import click
from utils import load_config
from ultralytics import YOLO


@click.command()
@click.option('--model_name', required=True, help='Model name as listed in models.yaml')
@click.option('--data_yaml', type=click.Path(exists=True), required=True, help='Path to dataset YAML file')
@click.option('--epochs', default=10, show_default=True, help='Number of training epochs')
@click.option('--batch_size', default=None, show_default=True, help='Batch size for training')
@click.option('--img_size', default=640, show_default=True, help='Input image size')
def fine_tune(model_name, data_yaml, epochs, batch_size, img_size):
    config = load_config()
    
    model_type = None
    for t, model_names in config.items():
        if model_name in model_names:
            model_type = t
            break
    assert model_type is not None, 'Did not find the model, specify one from models.yaml'

    model_path = os.path.join(config['DATA_PATH'], model_name)

    # Force download if it does not exist or load
    model = YOLO(model_path)

    # Train the model
    model.train(
        data=data_yaml,
        epochs=epochs,
        imgsz=img_size,
        cache=True,
        seed=42,
        single_cls=True,
        cos_lr=True,
        batch=0.65 if batch_size is None else int(batch_size),
        project=f'runs/{model_type}',
        name=f'{model_type}_{model_name}_finetune_{epochs}',
        warmup_epochs=2,
    )

if __name__ == '__main__':
    fine_tune()
