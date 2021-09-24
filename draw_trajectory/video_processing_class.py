import cv2
from pandas.core import frame
from opencv_func import get_video_prop,  write_circle
import sys

class video_processing:
    def __init__(self,df):
        self.detected_df = df.df
        self.video_path = df.video_path
        self.video_dir = df.video_dir
        self.video_W , self.video_H, self.video_count, self.video_fps = get_video_prop(self.video_path)
        
        

    def write_trajectory(self):
        
        #動画の保存方法を指定(#TODO　動画の名前にtrajectoryをつける)
        fmt = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')#MP4
        writer = cv2.VideoWriter(self.video_dir + 'trajectory.mp4', fmt, self.video_fps, (self.video_W, self.video_H))

        video = cv2.VideoCapture(self.video_path)
        """
        if not video.isOpend():
            sys.exit()
        """
        
        row_num=0
        frame_num = 0
        delay = 1
        while True:
            detected_frame_num = self.detected_df.iloc[row_num]['frame_num']
            ret, frame = video.read()
            if ret:
                frame_num += 1
                if frame_num == detected_frame_num:
                    X = int(self.detected_df.iloc[row_num]['x'] * self.video_W)
                    Y = int(self.detected_df.iloc[row_num]['y'] * self.video_H)
                    W = self.detected_df.iloc[row_num]['w'] * self.video_W
                    H = self.detected_df.iloc[row_num]['h'] * self.video_H
                    write_circle(frame, X, Y, W, H )
                    if row_num < len(self.detected_df)-1:
                        row_num += 1
                else:
                    continue
                writer.write(frame)
                print('{}フレーム目書き込み中'.format(frame_num))
            else:
                break
            #qを押すと停止
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break
        writer.release()
        video.release()
                



