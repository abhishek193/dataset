from fast import my_model

def predict(model, image):
    out = model.predict(image)
    return out

out = predict(my_model, 'badminton.30.jpg')
print(out)