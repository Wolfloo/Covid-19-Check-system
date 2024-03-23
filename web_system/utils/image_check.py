# -*- coding: utf-8 -*-
# FileName  : image_check.py
import tensorflow as tf
from .conf import model_path
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.resnet import preprocess_input
from tensorflow.keras.models import load_model

model = tf.keras.models.load_model(model_path)

class_names = ["Covid", "Normal", "Viral Pneumonia"]


def load_and_preprocess_image(path):
    image = tf.io.read_file(path)
    image = load_img(path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = preprocess_input(image)
    return image


def check_handle(img_path):
    test_img = img_path
    test_tensor = load_and_preprocess_image(test_img)
    pred = model.predict(test_tensor)
    pred_num = np.argmax(pred[0])
    result = class_names[pred_num]
    return result
