# Sign Language Translator App

A real-time, cross-lingual sign language translator built using Convolutional Neural Networks (CNNs), MediaPipe hand detection, and mobile-friendly deployment tools.

## Project Overview

This project aims to make sign language communication more accessible through a real-time mobile app that recognizes and translates sign language gestures using the device’s camera.

I currently support static hand gesture recognition (fingerspelling) and am working toward full dynamic gesture recognition (continuous signs).

## Current Progress

- Static Sign Language Recognition
  - Trained on an ASL dataset with hand images preprocessed using MediaPipe for precise hand detection and cropping.
  - Achieves high accuracy in classifying static signs (e.g., alphabet).
  - Trained using PyTorch, with plans for TorchScript or ONNX export for mobile and cloud deployment.

- Preprocessing Pipeline
  - Uses MediaPipe Hands to detect and crop hands from raw images.
  - Augmentation pipeline includes rotation, brightness shifts, and flipping to improve generalization.

## Work In Progress

- Dynamic Gesture Training
  - Currently working with the WLASL (Word-Level American Sign Language) dataset to train models for continuous gesture recognition.
  - Exploring CNN + LSTM architectures for modeling gesture sequences over time.
  - Video frames are being preprocessed with MediaPipe to extract consistent landmarks for temporal modeling.

## Multilingual Focus

I plan to support the following sign languages for now:
- ASL (American Sign Language)
- BSL (British Sign Language)


Each language will have its own dataset and model trained independently. Users will be able to download specific language models as needed, similar to offline language packs in translation apps.

## Planned Features

- Live camera translation
- Downloadable language modules (modular model loading)
- Dynamic gesture tracking using frame sequences
- Real-time on-device text translation and voice output
- Optional cloud-based model inference (for larger models)

## Tech Stack

- Model Training: PyTorch, Jupyter Notebooks
- Preprocessing: MediaPipe (hands)
- Mobile Deployment: TorchScript / ONNX / TFLite (still evaluating)
- App Framework: TBD (potentially Flutter, React Native, or native Android)

## Acknowledgements

This project is inspired by the need for inclusive communication tools. I acknowledge the open-source community for datasets such as ASL and WLASL, and tools like MediaPipe that made this work possible.

## What's Next

I'm actively working on model optimization, dynamic gesture training, and app integration. The app codebase will be published once the models are production-ready.
