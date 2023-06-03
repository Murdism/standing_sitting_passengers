import os
import random
import shutil

def split_dataset(image_folder, label_folder,split_folder, train_ratio, test_ratio, val_ratio):
    assert train_ratio + test_ratio + val_ratio == 1.0, "The sum of train_ratio, test_ratio, and val_ratio must equal 1.0"

    # Create directories for train, test, and validation sets
    train_dir_imgs = split_folder + "train/" +"images"
    test_dir_imgs = split_folder + "test/" +"images"
    val_dir_imgs = split_folder + "validation/" +"images"

    os.makedirs(train_dir_imgs, exist_ok=True)
    os.makedirs(test_dir_imgs, exist_ok=True)
    os.makedirs(val_dir_imgs, exist_ok=True)

    train_dir_lbs = split_folder + "train/" +"labels"
    test_dir_lbs = split_folder + "test/" +"labels"
    val_dir_lbs= split_folder + "validation/" +"labels"

    os.makedirs(train_dir_lbs, exist_ok=True)
    os.makedirs(test_dir_lbs, exist_ok=True)
    os.makedirs(val_dir_lbs, exist_ok=True)



    # Get the list of image files
    label_files = os.listdir(label_folder)

    # Randomly shuffle the file list
    random.shuffle(label_files)

    # Compute the number of files for each set based on the ratios
    num_files = len(label_files)
    num_train = int(num_files * train_ratio)
    num_test = int(num_files * test_ratio)
    num_val = num_files - num_train - num_test

    # Split image files into train, test, and validation sets
    train_files = label_files[:num_train]
    test_files = label_files[num_train:num_train+num_test]
    val_files = label_files[num_train+num_test:]

    # Move image files to their respective directories
    move_files(train_files,image_folder , train_dir_imgs,label_folder,train_dir_lbs)
    move_files(test_files, image_folder, test_dir_imgs,label_folder,test_dir_lbs)
    move_files(val_files, image_folder, val_dir_imgs,label_folder,val_dir_lbs)

    # # Move corresponding label files to their respective directories
    # move_files(train_files, train_dir+"/"+label_folder, train_dir)
    # move_files(test_files, test_dir+"/"+label_folder, test_dir)
    # move_files(val_files, val_dir+"/"+label_folder, val_dir)

def move_files(file_list, source_dir_image, destination_dir_image, source_dir_label, destination_dir_label):
    for label_name in file_list:
        file = label_name.split(".")[0]+".jpg"
        source_path_image = os.path.join(source_dir_image, file)
        source_path_label = os.path.join(source_dir_label, label_name)
        destination_image = os.path.join(destination_dir_image, file)
        destination__label = os.path.join(destination_dir_label, label_name)
        # print("source_path: ", file)
        print("source_path_image: ", source_path_image)
        print("destination_image: ", destination_image)
        print("source_path_label: ", source_path_label)
        print("destination__label: ", destination__label)
        shutil.move(source_path_image, destination_image)
        shutil.move(source_path_label, destination__label)

# Example usage
image_folder = "all_images/"
label_folder = "all_labels/"
split_folder = "split_dataset_sec/"
train_ratio = 0.8  # 80% of the data for training
test_ratio = 0.1   # 10% of the data for testing
val_ratio = 0.1    # 10% of the data for validation

split_dataset(image_folder, label_folder,split_folder, train_ratio, test_ratio, val_ratio)
