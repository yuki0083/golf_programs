import pandas as pd
import math
import utils

#iphone のスローモーション撮影は1080pの場合120fps
video_fps = 120


#meter_per_pixel.txtに結果を保存
def read_meter_per_pixel_from_txt(video_dir_path):
    with open(video_dir_path + 'meter_per_pixel.txt') as f:
        meter_per_pixel = float(f.read())
    return meter_per_pixel

def cal_head_velocity(df, video_property_dic, meter_per_pixel, conf_thres=0.5):
    #video propertyの取得
    video_W = video_property_dic["W"]
    video_H = video_property_dic["H"]
    #video_fps = video_property_dic["Fps"]
    #iphone のスローモーション撮影に依存

    #head(class 1)&conf>0.5 のdfを取り出し
    #copy()をつけることでsettingWithCopyWarningを回避
    df_head_speed = df[(df["class"] == 1) & (df["conf"] > conf_thres)].copy()
    #df_head_positonにmoving_distance,frame_space, swing_speedを追加
    moving_distance_list = []
    frame_space_list = []
    swing_speed_list = []
    i = 0
    for index, row in df_head_speed.iterrows():
        head_x = row["x"]
        head_y = row["y"]
        frame_num = row["frame_num"]
        if i == 0:
            moving_distance = 0
            frame_space = 0
            swing_speed = 0
        else:
            frame_space = frame_num - previous_frame_num
            moving_distance = math.sqrt((video_W*(head_x - previous_head_x))**2+\
                (video_H*(head_y - previous_head_y))**2) * meter_per_pixel

            swing_speed = moving_distance / (frame_space / video_fps)
        moving_distance_list.append(moving_distance)
        frame_space_list.append(frame_space)
        swing_speed_list.append(swing_speed)

        previous_head_x = head_x
        previous_head_y = head_y
        previous_frame_num = frame_num

        i+=1
    df_head_speed.loc[:, 'moving_distance'] = moving_distance_list
    df_head_speed.loc[:, 'frame_space'] = frame_space_list
    df_head_speed.loc[:, 'swing_speed'] = swing_speed_list
    return df_head_speed

def main():
    video_dir_path = "runs/detect/exp/"    
    video_property_csv_path =video_dir_path + "video_property.csv"
    detected_df_csv_path = video_dir_path + "detected_df.csv"

    video_property_dic = utils.get_video_prop(video_property_csv_path)
    meter_per_pixel = read_meter_per_pixel_from_txt(video_dir_path)
    df = utils.read_csv_to_df(detected_df_csv_path)
    meter_per_pixel = read_meter_per_pixel_from_txt(video_dir_path)
    df_head_speed = cal_head_velocity(df, video_property_dic, meter_per_pixel)
    utils.df_to_csv(df_head_speed, video_dir_path)

if __name__ == "__main__":
    main()