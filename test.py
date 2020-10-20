import fastai
print(fastai.__version__)

from fastai.vision.all import *
import sys

def predict(model, image):
    out = model.predict(image)
    return out

my_model = learn.load_learner('my_model')

out = predict(my_model, '/test10/test/1.jpg')
print(out)