import numpy as np
import os

from tflite_model_maker.config import QuantizationConfig
from tflite_model_maker.config import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import object_detector

import tensorflow as tf
assert tf.__version__.startswith('2')

tf.get_logger().setLevel('ERROR')
from absl import logging
logging.set_verbosity(logging.ERROR)



labels = ['Monnalisa',"L'urlo di Munch",'Notte Stellata','Bacio','Venere','Persistenza','Ragazza con Turbante','Guernica','L\'ultima cena']
spec = model_spec.get("efficientdet_lite0")

spec.config.autoaugment_policy = 'v0'

train_data = object_detector.DataLoader.from_pascal_voc("dataset/train/images","dataset/train/Annotations",labels)

validation_data = object_detector.DataLoader.from_pascal_voc("dataset/validation/images","dataset/validation/Annotations",labels)

test_data = object_detector.DataLoader.from_pascal_voc("dataset/test/images","dataset/test/Annotations",labels)

#Train the model
model = object_detector.create(train_data, model_spec=spec, epochs=50, batch_size=8, train_whole_model=True, validation_data=validation_data,)


print("\n\n Evaluating trained model\n")
#Test the model
ev = model.evaluate(test_data)
print(ev)

model.export(export_dir='.')

print("\n\nEvaluating tflite model")

ev = model.evaluate('model.tfite',test_data)
print(ev)

###
# modello di object detection cos'è l'object detection come è stata usata
# cosa è il transfer learning
# efficientdet e efficientdet0
# tensorflow lite model maker
###

