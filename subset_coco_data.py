import os
import random
import yaml

# Load configuration
with open('./models.yaml', 'r') as file:
    config = yaml.safe_load(file)

COCO_PATH = config['COCO_PATH']
TRAIN_TXT = os.path.join(COCO_PATH, 'train2017.txt')
VAL_TXT = os.path.join(COCO_PATH, 'val2017.txt')
IMAGES_PATH = os.path.join(COCO_PATH, 'images')
LABELS_PATH = os.path.join(COCO_PATH, 'labels')

# Helper function to read image filenames from txt files
def read_image_list(txt_file):
    with open(txt_file, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Helper function to check if label file contains person class (ID 0)
def has_person_label(image_path):
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    label_file = os.path.join(LABELS_PATH, f'{image_name}.txt')
    if not os.path.isfile(label_file):
        return False
    with open(label_file, 'r') as f:
        return any(line.startswith('0') for line in f)

# Function to create subset file
def create_subset_file(image_list, output_file):
    people_images = []
    no_people_images = []

    for image_path in image_list:
        if has_person_label(image_path):
            people_images.append(image_path)
        else:
            no_people_images.append(image_path)

    # Randomly select 20% of no_people_images
    selected_no_people = random.sample(no_people_images, int(0.2 * len(no_people_images)))

    # Combine and sort the final list
    final_list = sorted(people_images + selected_no_people)

    # Write to output file
    with open(output_file, 'w') as f:
        for image_path in final_list:
            f.write(f"{image_path}\n")

    print(f"Created subset file: {output_file} with {len(final_list)} entries.")

# Main function
def main():
    random.seed(42)  # For reproducibility

    train_images = read_image_list(TRAIN_TXT)
    val_images = read_image_list(VAL_TXT)

    create_subset_file(train_images, os.path.join(COCO_PATH, 'train2017_subset.txt'))
    create_subset_file(val_images, os.path.join(COCO_PATH, 'val2017_subset.txt'))

if __name__ == '__main__':
    main()