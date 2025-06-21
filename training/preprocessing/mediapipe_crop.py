# This file will contain the MediaPipe-based hand cropper for preprocessing images for ASL dataset.
# Implementation will be added in the next steps.

import cv2
import mediapipe as mp

def extract_hand_crop(image):
    mp_hands = mp.solutions.hands.Hands(static_image_mode=True)
    results = mp_hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if results.multi_hand_landmarks:
        h, w, _ = image.shape
        bbox = get_bbox_from_landmarks(results.multi_hand_landmarks[0], w, h)
        return image[bbox[1]:bbox[3], bbox[0]:bbox[2]]
    else:
        return None

def get_bbox_from_landmarks(landmarks, img_w, img_h):
    x = [l.x for l in landmarks.landmark]
    y = [l.y for l in landmarks.landmark]
    x_min, x_max = int(min(x) * img_w), int(max(x) * img_w)
    y_min, y_max = int(min(y) * img_h), int(max(y) * img_h)
    return (x_min, y_min, x_max, y_max)
