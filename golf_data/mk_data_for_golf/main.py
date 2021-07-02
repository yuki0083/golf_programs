import dir_utils, opencv
import shutil, os

image_dir_path ="./images"#画像の保存先
#video_dir_path = "../raw_data"#動画があるディレクトリ
video_dir_path = input("動画ディレクトリのパスを入力:")

dir_utils.make_dir(image_dir_path)

#動画ディレクトリから動画のパスのリストを取得
video_list = dir_utils.video_list(video_dir_path)
#動画からフレームを作成し保存
opencv.save_frames(video_list, image_dir_path)

