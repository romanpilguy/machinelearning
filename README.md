# machinelearning
<h2>Сравнение глубокой сверточной сети и многослойного перцептрона</h2>
Сети создаются на языке python с использованием библиотек Tensorflow и Keras на платформе Google Colaborations с использованием GPU (1xTesla K80 , compute 3.7, having 2496 CUDA cores , 12GB GDDR5 VRAM)
Модели сравниваются на датасете EMNIST - наборе рукописных букв латинского алфавита

<h2>Многослойный перцептрон</h2>
<h3>Первоначальная структура</h3>
Вход - 784 нейрона,
3 скрытых слоя: 1500, 2000, 1000, 26 выходных нейрона
<pre>Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 1500)              1177500   
_________________________________________________________________
dense_2 (Dense)              (None, 2000)              3002000   
_________________________________________________________________
dropout_1 (Dropout)          (None, 2000)              0         
_________________________________________________________________
dense_3 (Dense)              (None, 1000)              2001000   
_________________________________________________________________
dense_4 (Dense)              (None, 26)                26026     
=================================================================
Total params: 6,206,526
Trainable params: 6,206,526
Non-trainable params: 0</pre>

<h4>Первая попытка обучения</h4>
  Используются следующие параметры обучения:
  batch_size = 128
  epochs = 15
  
  Применяется дропаут 0,25 между вторым и третьим скрытыми слоями, во всех слоях используется функция активации ReLU, за исключением выходного, в котором используется Softmax. Функция потерь - перекрестная энтропия, оптимизация - adadelta 
 <p> Лог обучения:</p>
 <pre>Train on 93600 samples, validate on 31200 samples
Epoch 1/15
93600/93600 [==============================] - 144s 2ms/step - loss: 0.7004 - acc: 0.7833 - val_loss: 0.4943 - val_acc: 0.8452
Epoch 2/15
93600/93600 [==============================] - 144s 2ms/step - loss: 0.3338 - acc: 0.8904 - val_loss: 0.4010 - val_acc: 0.8719
Epoch 3/15
93600/93600 [==============================] - 147s 2ms/step - loss: 0.2566 - acc: 0.9121 - val_loss: 0.3490 - val_acc: 0.8871
Epoch 4/15
93600/93600 [==============================] - 148s 2ms/step - loss: 0.2114 - acc: 0.9256 - val_loss: 0.3098 - val_acc: 0.8997
Epoch 5/15
93600/93600 [==============================] - 144s 2ms/step - loss: 0.1816 - acc: 0.9353 - val_loss: 0.2699 - val_acc: 0.9179
Epoch 6/15
93600/93600 [==============================] - 143s 2ms/step - loss: 0.1555 - acc: 0.9431 - val_loss: 0.2860 - val_acc: 0.9135
Epoch 7/15
93600/93600 [==============================] - 143s 2ms/step - loss: 0.1364 - acc: 0.9494 - val_loss: 0.2921 - val_acc: 0.9157
Epoch 8/15
93600/93600 [==============================] - 143s 2ms/step - loss: 0.1219 - acc: 0.9538 - val_loss: 0.2913 - val_acc: 0.9136
Epoch 9/15
93600/93600 [==============================] - 143s 2ms/step - loss: 0.1092 - acc: 0.9572 - val_loss: 0.3035 - val_acc: 0.9157
Epoch 10/15
93600/93600 [==============================] - 144s 2ms/step - loss: 0.1003 - acc: 0.9602 - val_loss: 0.3171 - val_acc: 0.9153
Epoch 11/15
93600/93600 [==============================] - 145s 2ms/step - loss: 0.0937 - acc: 0.9628 - val_loss: 0.3395 - val_acc: 0.9138
Epoch 12/15
93600/93600 [==============================] - 144s 2ms/step - loss: 0.0872 - acc: 0.9650 - val_loss: 0.3262 - val_acc: 0.9180
Epoch 13/15
93600/93600 [==============================] - 145s 2ms/step - loss: 0.0806 - acc: 0.9675 - val_loss: 0.3309 - val_acc: 0.9194
Epoch 14/15
93600/93600 [==============================] - 144s 2ms/step - loss: 0.0747 - acc: 0.9692 - val_loss: 0.3309 - val_acc: 0.9211
Epoch 15/15
93600/93600 [==============================] - 143s 2ms/step - loss: 0.0726 - acc: 0.9702 - val_loss: 0.3436 - val_acc: 0.9204
Test loss: 0.34356227772925285
Test accuracy: 0.920352564102564</pre>
![](https://github.com/romanpilguy/machinelearning/raw/master/graphics/perc1.png)
<h3>Вторая попытка</h3>
Оптимизация методом градиентного спуска
batch_size = 128, epochs = 25,
<pre>
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 5000)              3925000   
_________________________________________________________________
dense_2 (Dense)              (None, 7000)              35007000  
_________________________________________________________________
dropout_1 (Dropout)          (None, 7000)              0         
_________________________________________________________________
dense_3 (Dense)              (None, 2000)              14002000  
_________________________________________________________________
dense_4 (Dense)              (None, 26)                52026     
=================================================================
Total params: 52,986,026
Trainable params: 52,986,026
Non-trainable params: 0
_________________________________________________________________
None
</pre>
<h5>Логи:</h5>
<pre>
Train on 93600 samples, validate on 31200 samples
Epoch 1/25
93600/93600 [==============================] - 80s 850us/step - loss: 0.6566 - acc: 0.8023 - val_loss: 0.4019 - val_acc: 0.8722
Epoch 2/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.2891 - acc: 0.9037 - val_loss: 0.3617 - val_acc: 0.8844
Epoch 3/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.2086 - acc: 0.9268 - val_loss: 0.3776 - val_acc: 0.8822
Epoch 4/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.1650 - acc: 0.9400 - val_loss: 0.2826 - val_acc: 0.9137
Epoch 5/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.1326 - acc: 0.9495 - val_loss: 0.3488 - val_acc: 0.8964
Epoch 6/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.1100 - acc: 0.9570 - val_loss: 0.2897 - val_acc: 0.9132
Epoch 7/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.0956 - acc: 0.9621 - val_loss: 0.3391 - val_acc: 0.9069
Epoch 8/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0866 - acc: 0.9654 - val_loss: 0.3200 - val_acc: 0.9142
Epoch 9/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.0753 - acc: 0.9692 - val_loss: 0.3389 - val_acc: 0.9152
Epoch 10/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0674 - acc: 0.9721 - val_loss: 0.3223 - val_acc: 0.9206
Epoch 11/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0619 - acc: 0.9737 - val_loss: 0.3635 - val_acc: 0.9190
Epoch 12/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0593 - acc: 0.9749 - val_loss: 0.3679 - val_acc: 0.9099
Epoch 13/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0556 - acc: 0.9764 - val_loss: 0.3475 - val_acc: 0.9230
Epoch 14/25
93600/93600 [==============================] - 77s 824us/step - loss: 0.0526 - acc: 0.9779 - val_loss: 0.3708 - val_acc: 0.9190
Epoch 15/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0514 - acc: 0.9780 - val_loss: 0.3670 - val_acc: 0.9197
Epoch 16/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.0463 - acc: 0.9798 - val_loss: 0.3701 - val_acc: 0.9207
Epoch 17/25
93600/93600 [==============================] - 91s 972us/step - loss: 0.0448 - acc: 0.9805 - val_loss: 0.3926 - val_acc: 0.9193
Epoch 18/25
93600/93600 [==============================] - 108s 1ms/step - loss: 0.0445 - acc: 0.9809 - val_loss: 0.4034 - val_acc: 0.9204
Epoch 19/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0410 - acc: 0.9822 - val_loss: 0.3983 - val_acc: 0.9206
Epoch 20/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0414 - acc: 0.9822 - val_loss: 0.4060 - val_acc: 0.9213
Epoch 21/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0400 - acc: 0.9827 - val_loss: 0.4278 - val_acc: 0.9197
Epoch 22/25
93600/93600 [==============================] - 108s 1ms/step - loss: 0.0381 - acc: 0.9836 - val_loss: 0.4064 - val_acc: 0.9200
Epoch 23/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0383 - acc: 0.9835 - val_loss: 0.4303 - val_acc: 0.9209
Epoch 24/25
93600/93600 [==============================] - 108s 1ms/step - loss: 0.0359 - acc: 0.9840 - val_loss: 0.4501 - val_acc: 0.9141
Epoch 25/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0342 - acc: 0.9851 - val_loss: 0.4486 - val_acc: 0.9191
Test loss: 0.44857419048877767
Test accuracy: 0.9191025641025641
</pre>
![](https://github.com/romanpilguy/machinelearning/raw/master/graphics/percep2.png))
<h2>Глубокая сверточная сеть</h2>
<h3>Первоначальная структура</h3>
<pre>Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_11 (Conv2D)           (None, 26, 26, 32)        320       
_________________________________________________________________
conv2d_12 (Conv2D)           (None, 24, 24, 64)        18496     
_________________________________________________________________
max_pooling2d_6 (MaxPooling2 (None, 12, 12, 64)        0         
_________________________________________________________________
dropout_11 (Dropout)         (None, 12, 12, 64)        0         
_________________________________________________________________
flatten_6 (Flatten)          (None, 9216)              0         
_________________________________________________________________
dense_11 (Dense)             (None, 128)               1179776   
_________________________________________________________________
dropout_12 (Dropout)         (None, 128)               0         
_________________________________________________________________
dense_12 (Dense)             (None, 26)                3354      
=================================================================
Total params: 1,201,946
Trainable params: 1,201,946
Non-trainable params: 0
_________________________________________________________________
None</pre>
<h4>Первая попытка обучения</h4>
 batch_size = 128
  epochs = 15
  Функции активации - ReLU, на выходном - Softmax
  <p>Логи:</p>
  <pre>
  Train on 93600 samples, validate on 31200 samples
Epoch 1/15
93600/93600 [==============================] - 15s 158us/step - loss: 0.8795 - acc: 0.7347 - val_loss: 0.3704 - val_acc: 0.8835
Epoch 2/15
93600/93600 [==============================] - 14s 151us/step - loss: 0.4541 - acc: 0.8590 - val_loss: 0.2716 - val_acc: 0.9119
Epoch 3/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.3755 - acc: 0.8824 - val_loss: 0.2590 - val_acc: 0.9171
Epoch 4/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.3348 - acc: 0.8931 - val_loss: 0.2462 - val_acc: 0.9197
Epoch 5/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.3091 - acc: 0.9009 - val_loss: 0.2432 - val_acc: 0.9235
Epoch 6/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.2922 - acc: 0.9056 - val_loss: 0.2222 - val_acc: 0.9304
Epoch 7/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.2753 - acc: 0.9110 - val_loss: 0.2195 - val_acc: 0.9305
Epoch 8/15
93600/93600 [==============================] - 14s 151us/step - loss: 0.2682 - acc: 0.9136 - val_loss: 0.2164 - val_acc: 0.9304
Epoch 9/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.2552 - acc: 0.9183 - val_loss: 0.2196 - val_acc: 0.9318
Epoch 10/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.2505 - acc: 0.9188 - val_loss: 0.2054 - val_acc: 0.9346
Epoch 11/15
93600/93600 [==============================] - 14s 151us/step - loss: 0.2439 - acc: 0.9216 - val_loss: 0.2135 - val_acc: 0.9339
Epoch 12/15
93600/93600 [==============================] - 14s 151us/step - loss: 0.2414 - acc: 0.9224 - val_loss: 0.2196 - val_acc: 0.9316
Epoch 13/15
93600/93600 [==============================] - 14s 151us/step - loss: 0.2362 - acc: 0.9245 - val_loss: 0.2046 - val_acc: 0.9346
Epoch 14/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.2309 - acc: 0.9251 - val_loss: 0.2093 - val_acc: 0.9342
Epoch 15/15
93600/93600 [==============================] - 14s 152us/step - loss: 0.2310 - acc: 0.9253 - val_loss: 0.2130 - val_acc: 0.9339
Test loss: 0.21300901203535688
Test accuracy: 0.9338782051282051
![](https://github.com/romanpilguy/machinelearning/raw/master/graphics/cnn1.png)
  </pre>
  <h4>Вторая попытка</h4>
  epochs = 25, batch_size = 128
  <pre>
  Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_13 (Conv2D)           (None, 26, 26, 32)        320       
_________________________________________________________________
conv2d_14 (Conv2D)           (None, 24, 24, 64)        18496     
_________________________________________________________________
max_pooling2d_7 (MaxPooling2 (None, 12, 12, 64)        0         
_________________________________________________________________
dropout_13 (Dropout)         (None, 12, 12, 64)        0         
_________________________________________________________________
flatten_7 (Flatten)          (None, 9216)              0         
_________________________________________________________________
dense_13 (Dense)             (None, 128)               1179776   
_________________________________________________________________
dropout_14 (Dropout)         (None, 128)               0         
_________________________________________________________________
dense_14 (Dense)             (None, 26)                3354      
=================================================================
Total params: 1,201,946
Trainable params: 1,201,946
Non-trainable params: 0
_________________________________________________________________
None
  </pre>
  <pre>
<h5>Логи:</h5>
  Train on 93600 samples, validate on 31200 samples
Epoch 1/25
93600/93600 [==============================] - 80s 850us/step - loss: 0.6566 - acc: 0.8023 - val_loss: 0.4019 - val_acc: 0.8722
Epoch 2/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.2891 - acc: 0.9037 - val_loss: 0.3617 - val_acc: 0.8844
Epoch 3/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.2086 - acc: 0.9268 - val_loss: 0.3776 - val_acc: 0.8822
Epoch 4/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.1650 - acc: 0.9400 - val_loss: 0.2826 - val_acc: 0.9137
Epoch 5/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.1326 - acc: 0.9495 - val_loss: 0.3488 - val_acc: 0.8964
Epoch 6/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.1100 - acc: 0.9570 - val_loss: 0.2897 - val_acc: 0.9132
Epoch 7/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.0956 - acc: 0.9621 - val_loss: 0.3391 - val_acc: 0.9069
Epoch 8/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0866 - acc: 0.9654 - val_loss: 0.3200 - val_acc: 0.9142
Epoch 9/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.0753 - acc: 0.9692 - val_loss: 0.3389 - val_acc: 0.9152
Epoch 10/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0674 - acc: 0.9721 - val_loss: 0.3223 - val_acc: 0.9206
Epoch 11/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0619 - acc: 0.9737 - val_loss: 0.3635 - val_acc: 0.9190
Epoch 12/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0593 - acc: 0.9749 - val_loss: 0.3679 - val_acc: 0.9099
Epoch 13/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0556 - acc: 0.9764 - val_loss: 0.3475 - val_acc: 0.9230
Epoch 14/25
93600/93600 [==============================] - 77s 824us/step - loss: 0.0526 - acc: 0.9779 - val_loss: 0.3708 - val_acc: 0.9190
Epoch 15/25
93600/93600 [==============================] - 77s 825us/step - loss: 0.0514 - acc: 0.9780 - val_loss: 0.3670 - val_acc: 0.9197
Epoch 16/25
93600/93600 [==============================] - 77s 826us/step - loss: 0.0463 - acc: 0.9798 - val_loss: 0.3701 - val_acc: 0.9207
Epoch 17/25
93600/93600 [==============================] - 91s 972us/step - loss: 0.0448 - acc: 0.9805 - val_loss: 0.3926 - val_acc: 0.9193
Epoch 18/25
93600/93600 [==============================] - 108s 1ms/step - loss: 0.0445 - acc: 0.9809 - val_loss: 0.4034 - val_acc: 0.9204
Epoch 19/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0410 - acc: 0.9822 - val_loss: 0.3983 - val_acc: 0.9206
Epoch 20/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0414 - acc: 0.9822 - val_loss: 0.4060 - val_acc: 0.9213
Epoch 21/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0400 - acc: 0.9827 - val_loss: 0.4278 - val_acc: 0.9197
Epoch 22/25
93600/93600 [==============================] - 108s 1ms/step - loss: 0.0381 - acc: 0.9836 - val_loss: 0.4064 - val_acc: 0.9200
Epoch 23/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0383 - acc: 0.9835 - val_loss: 0.4303 - val_acc: 0.9209
Epoch 24/25
93600/93600 [==============================] - 108s 1ms/step - loss: 0.0359 - acc: 0.9840 - val_loss: 0.4501 - val_acc: 0.9141
Epoch 25/25
93600/93600 [==============================] - 107s 1ms/step - loss: 0.0342 - acc: 0.9851 - val_loss: 0.4486 - val_acc: 0.9191
Test loss: 0.44857419048877767
Test accuracy: 0.9191025641025641
  </pre>
  ![](https://github.com/romanpilguy/machinelearning/raw/master/graphics/cnn2.png)
  <h2>Третья попытка</h2>
  Используется оптимизатор adadelta (https://habr.com/ru/post/318970/) ,
  batch_size = 128, epochs = 25,  топология неизменна
  <h4>Логи:</h4>
  <pre>
  Train on 93600 samples, validate on 31200 samples
Epoch 1/25
93600/93600 [==============================] - 41s 438us/step - loss: 1.2416 - acc: 0.6258 - val_loss: 0.4907 - val_acc: 0.8493
Epoch 2/25
93600/93600 [==============================] - 40s 426us/step - loss: 0.6312 - acc: 0.8022 - val_loss: 0.3568 - val_acc: 0.8841
Epoch 3/25
93600/93600 [==============================] - 40s 428us/step - loss: 0.5060 - acc: 0.8397 - val_loss: 0.2976 - val_acc: 0.9042
Epoch 4/25
93600/93600 [==============================] - 40s 430us/step - loss: 0.4418 - acc: 0.8593 - val_loss: 0.2784 - val_acc: 0.9101
Epoch 5/25
93600/93600 [==============================] - 40s 422us/step - loss: 0.4081 - acc: 0.8686 - val_loss: 0.2690 - val_acc: 0.9115
Epoch 6/25
93600/93600 [==============================] - 40s 427us/step - loss: 0.3725 - acc: 0.8789 - val_loss: 0.2537 - val_acc: 0.9167
Epoch 7/25
93600/93600 [==============================] - 41s 434us/step - loss: 0.3501 - acc: 0.8861 - val_loss: 0.2416 - val_acc: 0.9213
Epoch 8/25
93600/93600 [==============================] - 40s 427us/step - loss: 0.3325 - acc: 0.8913 - val_loss: 0.2344 - val_acc: 0.9245
Epoch 9/25
93600/93600 [==============================] - 40s 423us/step - loss: 0.3157 - acc: 0.8953 - val_loss: 0.2279 - val_acc: 0.9266
Epoch 10/25
93600/93600 [==============================] - 40s 432us/step - loss: 0.3036 - acc: 0.8996 - val_loss: 0.2362 - val_acc: 0.9230
Epoch 11/25
93600/93600 [==============================] - 40s 428us/step - loss: 0.2874 - acc: 0.9033 - val_loss: 0.2208 - val_acc: 0.9284
Epoch 12/25
93600/93600 [==============================] - 40s 424us/step - loss: 0.2792 - acc: 0.9065 - val_loss: 0.2136 - val_acc: 0.9296
Epoch 13/25
93600/93600 [==============================] - 41s 435us/step - loss: 0.2708 - acc: 0.9085 - val_loss: 0.2127 - val_acc: 0.9302
Epoch 14/25
93600/93600 [==============================] - 40s 423us/step - loss: 0.2629 - acc: 0.9110 - val_loss: 0.2108 - val_acc: 0.9309
Epoch 15/25
93600/93600 [==============================] - 40s 426us/step - loss: 0.2557 - acc: 0.9129 - val_loss: 0.2112 - val_acc: 0.9315
Epoch 16/25
93600/93600 [==============================] - 41s 433us/step - loss: 0.2456 - acc: 0.9164 - val_loss: 0.2099 - val_acc: 0.9330
Epoch 17/25
93600/93600 [==============================] - 40s 430us/step - loss: 0.2432 - acc: 0.9160 - val_loss: 0.2025 - val_acc: 0.9336
Epoch 18/25
93600/93600 [==============================] - 40s 430us/step - loss: 0.2328 - acc: 0.9193 - val_loss: 0.2165 - val_acc: 0.9301
Epoch 19/25
93600/93600 [==============================] - 40s 429us/step - loss: 0.2290 - acc: 0.9212 - val_loss: 0.2078 - val_acc: 0.9331
Epoch 20/25
93600/93600 [==============================] - 40s 429us/step - loss: 0.2246 - acc: 0.9214 - val_loss: 0.2083 - val_acc: 0.9343
Epoch 21/25
93600/93600 [==============================] - 40s 427us/step - loss: 0.2164 - acc: 0.9243 - val_loss: 0.2076 - val_acc: 0.9332
Epoch 22/25
93600/93600 [==============================] - 40s 426us/step - loss: 0.2142 - acc: 0.9250 - val_loss: 0.2068 - val_acc: 0.9333
Epoch 23/25
93600/93600 [==============================] - 41s 435us/step - loss: 0.2101 - acc: 0.9263 - val_loss: 0.2057 - val_acc: 0.9340
Epoch 24/25
93600/93600 [==============================] - 40s 427us/step - loss: 0.2043 - acc: 0.9285 - val_loss: 0.2020 - val_acc: 0.9342
Epoch 25/25
93600/93600 [==============================] - 40s 425us/step - loss: 0.2038 - acc: 0.9286 - val_loss: 0.2028 - val_acc: 0.9340
Test loss: 0.20282957774467575
Test accuracy: 0.933974358974359
  </pre>
  ![](https://github.com/romanpilguy/machinelearning/raw/master/graphics/cnn3.png)
  
