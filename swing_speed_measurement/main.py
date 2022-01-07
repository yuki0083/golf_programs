from numpy import heaviside
import pandas as pd
import math 

golf_club_length_inch = 45.7 #ドライバー141モデルの長さの平均値:45.7インチ
golf_club_length_meter = golf_club_length_inch / 39.37 #インチをメートルに変換
w_pixel = 1080
h_pixel= 1920

#gripとheadが両方検出出来ているフレームのみ取り出し
def df_remove_missing(df):
    both_detect_raw_num_list = []
    frame_num_array = df['frame_num']
    previous_frame_num = None
    for raw_num, frame_num in enumerate(frame_num_array):
        if frame_num == previous_frame_num:
            both_detect_raw_num_list.append(raw_num -1)
            both_detect_raw_num_list.append(raw_num)
        previous_frame_num = frame_num
    df = df.iloc[both_detect_raw_num_list]
    return df

def mk_frame_df(df):
    frame_data_columns = ['frame_num', 'grip_position_x', 'grip_positon_y', 'head_posiion_x', 'head_position_y', 'grip_head_distance'] 
    frame_data_list = []
    frame_num_list = df['frame_num'].values.tolist()
    unique_frame_num_list = list(dict.fromkeys(frame_num_list))
    for frame_num in unique_frame_num_list:
        
        df_one_frame = df[df['frame_num']== frame_num]
        grip_index = df_one_frame.index[df_one_frame['class']== 0].tolist()[0]
        head_index = df_one_frame.index[df_one_frame['class']== 1].tolist()[0]

        grip_position_x = float(df_one_frame.at[grip_index, 'x']) * w_pixel
        grip_position_y = float(df_one_frame.at[grip_index, 'y']) * h_pixel
        head_posiion_x = float(df_one_frame.at[head_index, 'x']) * w_pixel
        head_position_y = float(df_one_frame.at[head_index, 'y']) * h_pixel

        grip_head_distance = math.sqrt((grip_position_x - head_posiion_x)**2+(grip_position_y-head_position_y)**2)
        frame_data_list.append([frame_num, grip_position_x, grip_position_y, head_posiion_x, head_position_y, grip_head_distance])
        
    df_frame_data = pd.DataFrame(frame_data_list, columns=frame_data_columns)
    return df_frame_data

def cal_meter_per_pixel(df_frame_data,golf_club_length_meter):
    #外れ値を除去
    q1 = df_frame_data['grip_head_distance'].quantile(0.25)
    q3 = df_frame_data['grip_head_distance'].quantile(0.75)
    iqr = q3-q1
    max = q3 + iqr*1.5
    min = q1 - iqr*1.5
    #外れ値を除去した平均
    golf_club_length_pixel = df_frame_data[(df_frame_data["grip_head_distance"] > min) & (df_frame_data["grip_head_distance"] < max)]["grip_head_distance"].mean()
    #1pixelの大きさ
    meter_per_pixel = golf_club_length_meter/golf_club_length_pixel
    return meter_per_pixel

df = pd.read_csv('runs/detect/exp/detected_df.csv')
df = df.drop('Unnamed: 0', axis=1)
df = df_remove_missing(df)
df_frame_data = mk_frame_df(df)
meter_per_pixel = cal_meter_per_pixel(df_frame_data, golf_club_length_meter)
print('meter_per_mixel:{}.'.format(meter_per_pixel))

