import cv2
import numpy as np
import random  # For dummy data

def analyze_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return {'tags': [], 'vibe': 'unknown', 'quality': 'low'}
    
    # Quality: Average brightness
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    brightness = np.mean(gray)
    quality = 'high' if brightness > 100 else 'low'
    
    # Vibe: Based on color (simple HSV)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mean_hue = np.mean(hsv[:,:,0])
    vibe = 'energetic' if mean_hue > 100 else 'casual'  # Dummy logic
    
    # Tags: Dummy
    tags = random.choice([['food', 'travel'], ['fashion', 'aesthetic']])
    
    return {'tags': tags, 'vibe': vibe, 'quality': quality}

def analyze_video(video_path):
    # For simplicity, analyze thumbnail as image
    # In real: Use cv2.VideoCapture for frames
    return {
        'tags': random.choice([['outdoor', 'nightlife'], ['food review', 'party']]),
        'vibe': random.choice(['party', 'travel luxury', 'casual daily life']),
        'events': random.choice([['person dancing', 'beach'], ['car', 'dance']])
    }