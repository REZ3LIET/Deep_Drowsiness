import os
import random

from tqdm import tqdm

path = "./Data/Dataset/"
train = "./Data/Dataset/data/train/"
val = "./Data/Dataset/data/val/"

dirs = sorted(os.listdir(path))
for dir in tqdm(dirs):
    if dir == "data":
        continue
    img_dir = os.path.join(path, dir)
    ret = os.path.exists(img_dir)
    if not ret:
        print(img_dir)
    imgs = os.listdir(img_dir)
    
    ## 20 images for training and 10 for validation
    ids = random.sample(range(1, len(imgs)), 30)
    # 20 train images
    for i in ids[:20]:
        src_path = os.path.join(img_dir, imgs[i])
        dest_path = os.path.join(train, imgs[i])
        os.system(f"cp {src_path} {dest_path}")
    # 10 val images
    for i in ids[-10:]:
        src_path = os.path.join(img_dir, imgs[i])
        dest_path = os.path.join(val, imgs[i])
        os.system(f"cp {src_path} {dest_path}")
print("Dataset Created!!!")
