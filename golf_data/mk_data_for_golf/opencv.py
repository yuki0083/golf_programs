import cv2
import os
import glob
import sys

def save_first_frame(video_path, dir_path, ext='jpg'):
    # video_pathは元の動画のパス
    # dir_pathはフレームを保存するディレクトリ
    # extのデフォルトはjpg

    video_name = os.path.basename(video_path).split('.')[0]  # 10588044(video_name)を取り出す

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("cap")
        sys.exit()

    
    base_path = os.path.join(dir_path, video_name)  # 画像保存用のパスを作成

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))  # フレーム数の桁数を取得 int型はstr()で文字列にできる
    n=0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            cap.release()
            return

def save_frames(filelist, dir_path):
    for video_path in filelist:
        save_first_frame(video_path, dir_path)
