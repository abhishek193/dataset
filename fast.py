import fastai
print(fastai.__version__)

from fastai.vision.all import *

classes = ['badminton', 'tennis']
path = Path('fast')

def getdata():
    for class_name in classes:
        folder = class_name
        file = 'download_tennis'
        dest = path/folder
        dest.mkdir(parents=True, exist_ok=True)
        download_images(path/file, dest, max_pics=200)

def label_func(f): 
  return f[0] == 't'

cd train/

import os
files = os.listdir(os.getcwd())

def train(files):
    dls = ImageDataLoaders.from_path_func(os.getcwd(), files, label_func, item_tfms=Resize(100))
    learn = cnn_learner(dls, resnet34, metrics=error_rate)
    learn.fine_tune(1)
    return learn



#getdata()
my_model = train(files)


