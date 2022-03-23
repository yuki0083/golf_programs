import cv2

def write_circle(frame, x, y, w, h):
    radius = int((w + h) / 8)
    cv2.circle(frame, (x, y), radius, (255, 0, 0), thickness = -1)
