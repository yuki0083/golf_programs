from video_processing_class import video_processing
import mk_head_df_func


def main():
    video_path = "runs/detect/exp/IMG_9733.MP4"
    video_dir = "runs/detect/exp/"
    detected_df_csv_path = "runs/detect/exp/detected_df.csv"
    video_property_path = "runs/detect/exp/video_property.csv"
    #headの検出結果のdfを作成
    head_df = mk_head_df_func.mk_head_df(detected_df_csv_path)
    #軌道を描画
    video = video_processing(head_df, video_path, video_dir, video_property_path )
    video.write_trajectory()

if __name__ == '__main__':
    main()