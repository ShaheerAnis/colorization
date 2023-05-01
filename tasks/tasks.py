#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np
import os
import tensorflow as tf
from PIL import Image


class ImageGenerator:
    def __init__(self, model_path):
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
        os.environ["KMP_SETTINGS"] = "false"

        self.generator = tf.keras.models.load_model(model_path, compile=False)
        optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
        self.generator.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['accuracy'])

    def read_png(self, path):
        img = tf.io.read_file(path)
        img = tf.image.decode_png(img, channels=3)
        return img

    def split_image(self, image):
        w = tf.shape(image)[1]
        sketch_image = image[:, :w, :]
        sketch_image = tf.image.resize(sketch_image, (256, 256))
        return sketch_image

    def normalize(self, sketch_image):
        sketch_image = tf.cast(sketch_image, tf.float32) / 127.5 - 1
        return sketch_image

    def load_image_test(self, image_path):
        image = self.read_png(image_path)
        sketch_image = self.split_image(image)
        sketch_image = self.normalize(sketch_image)
        return sketch_image

    def generate_img(self, test_input):
        prediction = self.generator(test_input)
        test = prediction[0] / np.max(prediction[0])
        data = np.int8((test * 255) % 255)
        imgg = Image.fromarray(data, 'RGB')
        return imgg

    def generate_images(self, images_path, batch_size=5000):
        test_dataset = tf.data.Dataset.from_tensor_slices(images_path)
        test_dataset = test_dataset.map(self.load_image_test, num_parallel_calls=tf.data.AUTOTUNE)
        test_dataset = test_dataset.batch(batch_size)
        for n, data in enumerate(test_dataset):
            if (n >= 0 and n < 5):
                sketch_image = data
                imgg2 = Image.fromarray(np.int8((sketch_image[0] * 255)), 'RGB')
                # display(imgg2)
                generated_image = self.generate_img(sketch_image)
                # display(generated_image)
            elif (n >= 5):
                break
