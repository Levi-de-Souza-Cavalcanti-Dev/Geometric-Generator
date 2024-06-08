import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.optimizers import Adam

img_height, img_width = 150, 150
batch_size = 32

train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_generator = train_datagen.flow_from_directory(
    'C:\\Users\\User\\Desktop\\casas',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',  # ou 'categorical' se tiver mais de duas classes
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    'C:\\Users\\User\\Desktop\\casas',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='binary',  # ou 'categorical'
    subset='validation')

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(img_height, img_width, 3)),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')  # ou 'softmax' para múltiplas classes
])

model.compile(optimizer=Adam(),
              loss='binary_crossentropy',  # ou 'categorical_crossentropy'
              metrics=['accuracy'])

model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    epochs=10)

model.evaluate(validation_generator)

model.save('meu_modelo.h5')
