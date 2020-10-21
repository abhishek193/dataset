import fastai
print(fastai.__version__)

from fastai.vision.all import *
import sys
import fast

def predict(model, image):
    out = model.predict(image)
    return out


out = predict(my_model, '/test10/test/1.jpg')
print(out)