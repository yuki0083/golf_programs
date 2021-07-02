import dir_utils, opencv
import shutil, os


"""
data_temp_dir_path = 'data_temp'
data_check_dir_path = "data_check"
data_archive_dir_path = "data_archive"

if os.path.exists(data_check_dir_path):#data_checkディレクトリを削除
    shutil.rmtree(data_check_dir_path)
"""
image_dir_path ="./images"#画像の保存先
video_dir_path = "../raw_data"#動画があるディレクトリ
#video_path = input("動画ディレクトリのパスを入力")

dir_utils.make_dir(image_dir_path)
"""
nwcam_selected_list = move_files.move_nwcam(nwcam_path = 'C:\\nwcam', abst_num=30)
#nwcam_pathはダウンロードしたデータのあるディレクトリ
"""
#動画ディレクトリから動画のパスのリストを取得
video_list = dir_utils.video_list(video_dir_path)
#動画からフレームを作成し保存
opencv.save_frames(video_list, image_dir_path)
"""
shutil.rmtree(data_temp_dir_path)#data_tempを削除

#data_checkの中身をdata_archiveにコピー
move_files.make_dir(data_archive_dir_path)#data_archiveディレクトリを作成
frame_list = os.listdir(data_check_dir_path)

for i in range(len(frame_list)):
    frame_list[i] = os.path.join(data_check_dir_path, frame_list[i])

for i in range(len(frame_list)):
    frame_list[i] = shutil.copy2(frame_list[i], data_archive_dir_path)
"""




