from video_processing_class import video_processing
import mk_head_df_func
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--video_dir',required=True)
    parser.add_argument('--video_path', required=True)
    args =parser.parse_args()
    """
    video_path = "runs/detect/exp/IMG_9733.mp4"
    video_dir = "runs/detect/exp/"
    detected_df_csv_path = "runs/detect/exp/detected_df.csv"
    video_property_path = "runs/detect/exp/video_property.csv"
    """
    video_path = args.video_path
    video_dir = args.video_dir
    detected_df_csv_path = video_dir + "detected_df.csv"
    video_property_path = video_dir + "video_property.csv"
    #headの検出結果のdfを作成
    head_df = mk_head_df_func.mk_head_df(detected_df_csv_path)
    #軌道を描画
    video = video_processing(head_df, video_path, video_dir, video_property_path )
    video.write_trajectory()

if __name__ == '__main__':
    main()