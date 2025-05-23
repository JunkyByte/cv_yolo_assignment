import click
from ultralytics import YOLO

@click.command()
@click.option('--model-path', required=True, help='Path to the YOLO model file')
@click.option('--image-path', required=True, help='Path to the image file')
def run_inference(model_path, image_path):
    model = YOLO(model_path)
    results = model.predict(image_path, imgsz=640, conf=0.2)
    results[0].show()

if __name__ == '__main__':
    run_inference()