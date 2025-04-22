# cv_yolo_assignment

P7. Recognition of Persons with YOLO vX

The objective of this project is to conduct a comprehensive evaluation of the various versions of YOLO (You Only Look Once), a popular real-time object detection system, specifically for the task of person detection in images. This project involves comparing the performance of different (at least 4) YOLO versions from YOLOv5. Key aspects of the evaluation will include training and inference times, accuracy, and the model's ability to generalize across diverse datasets. A significant part of this project will involve fine-tuning the chosen YOLO models with a dataset focused solely on person detection to ensure the models are well-adapted to the specific task.

---

Downloading and setup COCO data for training. We use a simple yaml config file. To customize your data / ckpts paths copy the `config_default.yaml` as `config.yaml` and change it. It will be automatically loaded by the scripts.

In order to download the coco data and labels (once you have setup your custom paths if needed) simply run (IT will take a while as COCO data is >15gbs)
```bash
python download_coco.py
```

Last but not least you need to add a `coco.yaml` config provided by ultralytics. In current folder you will find a version with correct modifications already applied for our usecase. Copy it to the root path of the COCO dataset you just downloaded.

We need to create the subset of data that will be used for training the person-only object detector, in order to do so simply run
```bash
python subset_coco_data.py
```

You are done, training scripts should run correctly out of the box now!

---

**Nano Models (n):**

| Model      | Parameters (M) | FLOPs (GFLOPs) |
|------------|----------------|----------------|
| YOLOv5n    | 1.9            | 4.5            |
| YOLOv3tiny | —              | 5.6            |
| YOLOv6n    | 4.7            | 11.4           |
| YOLOv8n    | 3.2            | 8.7            |
| YOLOv9t    | 2.0            | 7.7            |
| YOLOv10n   | 2.3            | 6.7            |
| YOLOv11n   | 2.6            | 6.5            |
| **YOLOv12n** | 2.6          | 6.5            |

---

**Small Models (s):**

| Model      | Parameters (M) | FLOPs (GFLOPs) |
|------------|----------------|----------------|
| YOLOv5s    | 7.2            | 16.5           |
| YOLOv6s    | 18.5           | 44.2           |
| YOLOv8s    | 11.2           | 28.6           |
| YOLOv9s    | 7.2            | 26.7           |
| YOLOv10s   | 7.2            | 21.6           |
| YOLOv11s   | 9.4            | 21.5           |
| **YOLOv12s** | 9.3          | 21.4           |

---

**Medium Models (m):**

| Model      | Parameters (M) | FLOPs (GFLOPs) |
|------------|----------------|----------------|
| YOLOv3     | —              | 65.8           |
| YOLOv5m    | 21.2           | 49.0           |
| YOLOv6m    | 34.9           | 85.8           |
| YOLOv8m    | 25.9           | 78.9           |
| YOLOv9m    | 20.1           | 76.8           |
| YOLOv10m   | 15.4           | 59.1           |
| YOLOv11m   | 20.1           | 68.0           |
| **YOLOv12m** | 20.2         | 67.5           |

---

**Large Models (l):**

| Model      | Parameters (M) | FLOPs (GFLOPs) |
|------------|----------------|----------------|
| YOLOv5l    | 46.5           | 109.1          |
| YOLOv6l    | 59.6           | 150.7          |
| YOLOv8l    | 43.7           | 165.2          |
| YOLOv9c    | 25.5           | 102.8          |
| YOLOv10l   | 24.4           | 120.3          |
| YOLOv11l   | 25.3           | 86.9           |
| **YOLOv12l** | 26.4         | 88.9           |

---

**Extra Large Models (x):**

| Model      | Parameters (M) | FLOPs (GFLOPs) |
|------------|----------------|----------------|
| YOLOv5x    | 86.7           | 205.7          |
| YOLOv8x    | 68.2           | 257.8          |
| YOLOv9e    | 58.1           | 192.5          |
| YOLOv10x   | 29.5           | 160.4          |
| YOLOv11x   | 56.9           | 194.9          |
| **YOLOv12x** | 56.9         | 199.0          |

---

Let me know if you need more adjustments or details!
