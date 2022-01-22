import pandas as pd

#video_propertyからvideo_property(W,H,Frame_count,FPS)を取得
def get_video_prop(video_property_path):
    df = pd.read_csv(video_property_path)
    df = df.drop('Unnamed: 0', axis=1)
    video_property_dic =df.to_dict(orient='records')[0]
    return video_property_dic

def read_csv_to_df(detected_df_csv_path):
    df = pd.read_csv(detected_df_csv_path)
    df = df.drop('Unnamed: 0', axis=1)
    return df
