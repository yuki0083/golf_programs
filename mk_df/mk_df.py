import pandas as pd
import os
import glob




#check the exisiting of the csv file
def check_trafectory_video_exist(exp_n_path):
    result = glob.glob(exp_n_path + '*' + 'csv')
    if result == []:
        return False
    else:
        return True

#project(/runs/detect/)/の中で軌道描画済みのビデオが存在しないexp_n/のパスを返す
def not_trajectory_path(project):
    #pythonプログラムのあるディレクトリパス
    program_dir_path = os.path.dirname(__file__)

    exp_n_path_list = glob.glob(program_dir_path + '/../'+ project + '/*/')#runs/detect/exp_n_/のパスを取得
    result = []
    for exp_n_path in exp_n_path_list:
        exist = check_trafectory_video_exist(exp_n_path)
        if exist == False:
            result.append(exp_n_path)
    return result

#txtのデータを２次元リストに変換[[フレーム番号, クラス, x, y, w, h, conf]]
def mk_detected_data_list(video_dir):    
    detcte_data_list = []
    detected_txt_list = glob.glob(video_dir+'labels/*.txt')
    for txt_path in detected_txt_list:
        frame_num = int((os.path.basename(txt_path).split('.')[0]).split('_')[-1])#txtファイルの名前からフレーム番号を取得
        with open(txt_path) as f: #txtデータ[クラス, x, y, w, h, conf] 
        #各クラスで確信度の最も高いものだけdfに保存
            detected_cls_dic = {}
            l = f.read().split("\n")
            for one_detect in l:
                tmp_detect_data = one_detect.split()
                if tmp_detect_data == []:
                    continue
                tmp_detect_data = [int(s) if i == 0 else float(s) for i, s  in enumerate(tmp_detect_data)]
                cls = str(tmp_detect_data[0])
                conf = tmp_detect_data[5]
                if (cls not in detected_cls_dic) or (detected_cls_dic[cls][5] < conf) :
                    detected_cls_dic[cls] = tmp_detect_data

            for detected_data in list(detected_cls_dic.values()):
                detected_data.insert(0, frame_num)
                detcte_data_list.append(detected_data)
    return detcte_data_list

#txtファイルからpandasデータフレームを作成　
def mk_df(video_dir): #video_dir: runs/detect/expn/
    detected_data_list = mk_detected_data_list(video_dir)
    #2次元リストからデータフレームを作成
    df = pd.DataFrame(detected_data_list,columns=['frame_num', 'class', 'x', 'y', 'w', 'h', 'conf'] )
    return df
#dfをフレーム番号（クラス)の順に並び替える
def sort_df(df):
    df = df.sort_values(['frame_num', 'class'])
    df = df.reset_index(drop=True)
    return df

def df_to_csv(df, video_dir):
    df.to_csv(video_dir + 'detected_df.csv')
    print("finish writing csv in {}".format(video_dir))





def main():
    #推論データの保存場所
    project = 'runs/detect'
    name = 'exp'

    video_dir_list = not_trajectory_path(project)

    for video_dir  in video_dir_list:
        df = mk_df(video_dir)
        df = sort_df(df)
        df_to_csv(df, video_dir)


if __name__ == '__main__':
    main()