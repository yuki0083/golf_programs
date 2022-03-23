from ast import arg
import cv2
import pandas as pd
import argparse


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
#dfにしてcsvファイルに保存
def mk_video_prop_csv(video_prop, video_dir, video_prop_columns=["W", "H", "Frame_num", "Fps"]):
    video_prop =[video_prop]
    df = pd.DataFrame(video_prop, columns=video_prop_columns)
    df.to_csv(video_dir + 'video_property.csv')
    print("finish writing csv in {}".format(video_dir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_dir',required=True)
    parser.add_argument('--video_path', required=True)
    args =parser.parse_args()
    """
    video_path = 'runs/detect/exp/IMG_9733.mp4'
    video_dir= "runs/detect/exp/"
    video_prop = get_video_prop(video_path)
    mk_video_prop_csv(video_prop, video_dir)
    """
    video_prop = get_video_prop(args.video_path)
    mk_video_prop_csv(video_prop, args.video_dir)

if __name__ == '__main__':
    main()