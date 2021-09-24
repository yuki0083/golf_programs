
from mk_df_func import mk_df
import glob


class detected_df:
    def __init__(self,video_dir):
        self.df = mk_df(video_dir)
        self.video_dir = video_dir
        self.video_path = glob.glob(video_dir + '*.MP4')[0]
        
    #フレーム番号の順に並べる
    def sort_frame_num(self):
        self.df.sort_values('frame_num', inplace=True)
        self.df.reset_index(inplace=True)
        self.df.drop('index', axis=1, inplace=True)




