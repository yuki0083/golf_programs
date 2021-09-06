import shutil
import os
#ディレクトリ作成
def make_dir(data_temp_path='data_temp'):
    if not os.path.exists(data_temp_path):
        os.makedirs(data_temp_path)

#ディレクトリから動画ファイルパスのリストを取得
def video_list(video_directory):
    video_list = os.listdir(video_directory)
    
    for i in range(len(video_list)):
        video_list[i] = video_directory+ '/' + video_list[i]

    return video_list