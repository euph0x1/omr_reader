import cv2
import numpy as np

def preprocess_image(image_path):
    """Read and preprocess OMR image"""
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    thresh = cv2.threshold(blur, 0, 255,
                           cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    return img, thresh

def detect_bubbles(thresh, num_questions=100, choices=4):
    """Detect bubbles (returns marked answers A-D or None if blank)"""
    # Find contours
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                               cv2.CHAIN_APPROX_SIMPLE)
    # Sort top-to-bottom, then left-to-right
    cnts = sorted(cnts, key=lambda c: cv2.boundingRect(c)[1])
    
    questions = []
    for i in range(0, len(cnts), choices):
        cnts_row = sorted(cnts[i:i+choices], key=lambda c: cv2.boundingRect(c)[0])
        bubbled = None
        max_val = 0
        for j, c in enumerate(cnts_row):
            mask = np.zeros(thresh.shape, dtype="uint8")
            cv2.drawContours(mask, [c], -1, 255, -1)
            total = cv2.countNonZero(cv2.bitwise_and(thresh, thresh, mask=mask))
            if total > max_val:
                max_val = total
                bubbled = j
        if max_val > 200:  # threshold to detect if marked
            questions.append(chr(97 + bubbled))  # 'a','b','c','d'
        else:
            questions.append(None)
    return questions
