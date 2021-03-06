# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3Syhab2tjOv4Q_0mETNZBKjb6BlFcEc
"""

!pip install python-mnist

from __future__ import print_function
import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from mnist import MNIST
from sklearn.model_selection import train_test_split
from keras.utils import np_utils
from keras.preprocessing import image
import matplotlib.pyplot as plt
from scipy.misc import toimage
# %matplotlib inline 
import numpy as np

img_rows, img_cols = 28, 28

emnist_data = MNIST(path='sample_data', return_type='numpy')
emnist_data.select_emnist('letters')
X, y = emnist_data.load_training()

X = X.reshape(124800, 28, 28)
y = y.reshape(124800, 1)

y = y-1

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=111)

index=6
plt.imshow(toimage(x_test[index].reshape(28,28)))
plt.show()
print(x_test[index][14])

num_classes = 26
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')


x_train /= 255
x_test /= 255


y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

batch_size = 128

epochs = 25


model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))


model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True),
              metrics=['accuracy'])
print(model.summary())


history = model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

history_dict = history.history
acc_values = history_dict['acc']
val_acc_values = history_dict['val_acc']
epochs = range(1, len(acc_values) + 1)
plt.plot(epochs, acc_values, 'bo', label='Training acc')
plt.plot(epochs, val_acc_values, 'b', label='Validation acc')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

"""Сохраняем модель"""

model_json = model.to_json()
json_file = open("dcnn_model2.json", "w")
json_file.write(model_json)
json_file.close()
model.save_weights("dcnn_model2.h5")

from google.colab import files
files.download("dcnn_model2.json")
files.download("dcnn_model2.h5")

"""Тесты"""

import PIL

img = PIL.Image.open("sample_data/avatar.png").convert("L")
img = np.array(img)/255
plt.imshow(toimage(img))
plt.show
img = img.reshape(1,28,28,1)

prediction0 = model.predict(img)[0]
prediction0 = np.argmax(prediction0)


letters = { 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: '-'}
print(str(letters[int(prediction0)+1]))

index=616
plt.imshow(toimage(x_test[index].reshape(28,28)))
plt.show()
prediction = model.predict(x_test[index].reshape(1, img_rows, img_cols, 1))[0]
prediction = np.argmax(prediction)


letters = { 1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z', 27: '-'}
print(str(letters[int(prediction)+1]))