import os
import random
from utils import load_config


# Load configuration
config = load_config()
COCO_PATH = config['COCO_PATH']
TRAIN_TXT = os.path.join(COCO_PATH, 'train2017.txt')
VAL_TXT = os.path.join(COCO_PATH, 'val2017.txt')
IMAGES_PATH = os.path.join(COCO_PATH, 'images')
LABELS_PATH = os.path.join(COCO_PATH, 'labels')
ORIGINAL_LABELS_PATH = os.path.join(COCO_PATH, 'original_labels')
NEW_LABELS_PATH = LABELS_PATH

# Structure paths for train and val
ORIGINAL_TRAIN_LABELS = os.path.join(ORIGINAL_LABELS_PATH, 'train2017')
ORIGINAL_VAL_LABELS = os.path.join(ORIGINAL_LABELS_PATH, 'val2017')
NEW_TRAIN_LABELS = os.path.join(NEW_LABELS_PATH, 'train2017')
NEW_VAL_LABELS = os.path.join(NEW_LABELS_PATH, 'val2017')

# Helper function to read image filenames from txt files
def read_image_list(txt_file):
    with open(txt_file, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Helper function to check if label file contains person class (ID 0)
def has_person_label(image_path):
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    # Determine if it's from train or val set based on image path
    if 'train2017' in image_path:
        label_file = os.path.join(ORIGINAL_TRAIN_LABELS, f'{image_name}.txt')
    else:
        label_file = os.path.join(ORIGINAL_VAL_LABELS, f'{image_name}.txt')
    
    if not os.path.isfile(label_file):
        return False
    with open(label_file, 'r') as f:
        return any(line.startswith('0') for line in f)

# Function to create subset file and people-only labels
def create_subset_file(image_list, output_file, is_train=True):
    people_images = []
    no_people_images = []
    
    for image_path in image_list:
        if has_person_label(image_path):
            people_images.append(image_path)
        else:
            no_people_images.append(image_path)
    
    # Randomly select 20% of no_people_images
    selected_no_people = random.sample(no_people_images, int(0.05 * len(no_people_images)))
    
    # Combine and sort the final list
    final_list = sorted(people_images + selected_no_people)
    
    # Determine correct source and destination folders
    if is_train:
        original_labels_dir = ORIGINAL_TRAIN_LABELS
        new_labels_dir = NEW_TRAIN_LABELS
    else:
        original_labels_dir = ORIGINAL_VAL_LABELS
        new_labels_dir = NEW_VAL_LABELS
    
    # Create people-only labels for each image in the final list
    os.makedirs(new_labels_dir, exist_ok=True)
    
    for image_path in final_list:
        image_name = os.path.splitext(os.path.basename(image_path))[0]
        original_label_file = os.path.join(original_labels_dir, f'{image_name}.txt')
        new_label_file = os.path.join(new_labels_dir, f'{image_name}.txt')
        
        # If the original label file exists
        if os.path.isfile(original_label_file):
            with open(original_label_file, 'r') as f:
                lines = f.readlines()
            
            # Filter only person class (ID 0) entries
            person_lines = [line for line in lines if line.startswith('0')]
            
            # Write only person entries to the new label file
            with open(new_label_file, 'w') as f:
                for line in person_lines:
                    f.write(line)
        else:
            # Create an empty label file if no original exists
            with open(new_label_file, 'w') as f:
                pass
    
    # Write to output file
    with open(output_file, 'w') as f:
        for image_path in final_list:
            f.write(f"{image_path}\n")
    
    print(f"Created subset file: {output_file} with {len(final_list)} entries.")
    print(f"Created people-only labels in: {new_labels_dir}")
    
    # Write to output file
    with open(output_file, 'w') as f:
        for image_path in final_list:
            f.write(f"{image_path}\n")

# Main function
def main():
    random.seed(42)  # For reproducibility
    
    # Rename original labels folder to original_labels
    if os.path.exists(LABELS_PATH) and not os.path.exists(ORIGINAL_LABELS_PATH):
        print(f"Renaming {LABELS_PATH} to {ORIGINAL_LABELS_PATH}")
        os.rename(LABELS_PATH, ORIGINAL_LABELS_PATH)
    
    # Create new labels directory structure
    os.makedirs(NEW_TRAIN_LABELS, exist_ok=True)
    os.makedirs(NEW_VAL_LABELS, exist_ok=True)
    print(f"Created new labels directories: {NEW_TRAIN_LABELS} and {NEW_VAL_LABELS}")
    
    train_images = read_image_list(TRAIN_TXT)
    val_images = read_image_list(VAL_TXT)
    
    create_subset_file(train_images, os.path.join(COCO_PATH, 'train2017_subset.txt'), is_train=True)
    create_subset_file(val_images, os.path.join(COCO_PATH, 'val2017_subset.txt'), is_train=False)

if __name__ == '__main__':
    main()