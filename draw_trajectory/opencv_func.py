import cv2
import sys


def get_video_prop(video_path):
    video = cv2.VideoCapture(video_path)
    """
    if not video.isOpend():
        sys.exit()
    """
    #幅
    W = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 高さ
    H = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 総フレーム数
    count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    # fps
    fps = int(video.get(cv2.CAP_PROP_FPS))

    video_prop = [W, H, count, fps]
    
    video.release()
    return video_prop

def write_circle(frame, x, y, w, h):
    radius = int((w + h) / 8)
    cv2.circle(frame, (x, y), radius, (255, 0, 0), thickness = -1)

