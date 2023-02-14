#!/bin/bash

pip install --use-deprecated=legacy-resolver tflite-model-maker --default-timeout=500
pip install pycocotools
pip install opencv-python-headless==4.1.2.30 --default-timeout=500
pip uninstall -y tensorflow && pip install tensorflow==2.8.0 --default-timeout=500

