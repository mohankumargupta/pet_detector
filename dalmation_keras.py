import keras
import numpy as np
from keras.applications import mobilenet
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import time

#Load the MobileNet model
mobilenet_model = mobilenet.MobileNet(weights='imagenet')


filename = 'test.jpg'
original = load_img(filename, target_size=(224, 224))
print('PIL image size',original.size)

numpy_image = img_to_array(original)
#plt.imshow(np.uint8(numpy_image))
#plt.show()
print('numpy array size',numpy_image.shape)

image_batch = np.expand_dims(numpy_image, axis=0)
print('image batch size', image_batch.shape)
#plt.imshow(np.uint8(image_batch[0]))

processed_image = mobilenet.preprocess_input(image_batch.copy())
for _ in range(10):
  start = time.time()
  predictions = mobilenet_model.predict(processed_image)
  label = decode_predictions(predictions)
  print(time.time() - start)
  print(label)
