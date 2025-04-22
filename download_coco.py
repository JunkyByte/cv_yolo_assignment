from pathlib import Path
from ultralytics.utils.downloads import download
import click
from utils import load_config


@click.command()
@click.option('--only_labels', is_flag=True, help='Download only labels, skip images')
def main(only_labels):
    config = load_config()

    segments = True
    dir = Path(config["COCO_PATH"])
    url = "https://github.com/ultralytics/assets/releases/download/v0.0.0/"
    label_url = url + ("coco2017labels-segments.zip" if segments else "coco2017labels.zip")
    download([label_url], dir=dir.parent)

    if not only_labels:
        urls = [
            "http://images.cocodataset.org/zips/train2017.zip",
            "http://images.cocodataset.org/zips/val2017.zip",
            "http://images.cocodataset.org/zips/test2017.zip",
        ]
        download(urls, dir=dir / "images", threads=3)


if __name__ == '__main__':
    main()