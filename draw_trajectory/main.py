from mk_df_func import  not_trajectory_path
from detected_df_class import detected_df
from video_processing_class import video_processing


def main():
    #推論データの保存場所
    project = 'runs/detect'
    name = 'exp'

    video_dir_list = not_trajectory_path(project)

    for video_dir  in video_dir_list:
        detect = detected_df(video_dir)
        detect.sort_frame_num()
        
        video = video_processing(detect)
        video.write_trajectory()

if __name__ == '__main__':
    main()