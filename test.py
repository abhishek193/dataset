from fast import my_model
import sys

def predict(model, image):
    out = model.predict(image)
    return out

out = predict(my_model, sys.argv[1])
print(out)