import os
import click
import yaml
from ultralytics import YOLO


@click.command()
@click.option('--model_name', required=True, help='Model name as listed in models.yaml')
@click.option('--size', type=click.Choice(['nano', 'small', 'medium', 'large', 'xlarge']), required=True, help='Model size category')
@click.option('--models_yaml', type=click.Path(exists=True), required=True, help='Path to models.yaml')
@click.option('--data_yaml', type=click.Path(exists=True), required=True, help='Path to dataset YAML file')
@click.option('--epochs', default=10, show_default=True, help='Number of training epochs')
@click.option('--batch_size', default=32, show_default=True, help='Batch size for training')
@click.option('--img_size', default=640, show_default=True, help='Input image size')
def fine_tune(model_name, size, models_yaml, data_yaml, epochs, batch_size, img_size):
    # Load models.yaml config
    with open(models_yaml, 'r') as file:
        config = yaml.safe_load(file)
    
    model_type = None
    for t, model_names in config.items():
        if model_name in model_names:
            model_type = t
            break
    assert model_type is not None, 'Did not find the model, specify one from models.yaml'

    # Resolve full model path
    model_path = os.path.join(config['DATA_PATH'], model_name)

    # Load the model
    model = YOLO(model_path)

    # Train the model
    model.train(
        data=data_yaml,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size,
        cache=True,
        seed=42,
        single_cls=True,
        cos_lr=True,
        optimizer='Adam',
        lr0=0.001,
        name=f'{model_type}_{model_name}_finetune_{epochs}'
    )

if __name__ == '__main__':
    fine_tune()
