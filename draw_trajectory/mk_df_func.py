import pandas as pd
import os
import glob




#指定したディレクトリ内に軌道描画済みのビデオが存在するかを確認
def check_trafectory_video_exist(exp_n_path):
    result = glob.glob(exp_n_path + '*' + '_trajectory.mp4')
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
        with open(txt_path) as f:
            l = f.read().split()
            l = [int(s) if i == 0 else float(s) for i, s  in enumerate(l)]
            l.insert(0, frame_num)
            detcte_data_list.append(l)
    return detcte_data_list

#txtファイルからpandasデータフレームを作成　
def mk_df(video_dir): #video_dir: runs/detect/expn/
    detected_data_list = mk_detected_data_list(video_dir)
    #2次元リストからデータフレームを作成
    df = pd.DataFrame(detected_data_list,columns=['frame_num', 'class', 'x', 'y', 'w', 'h', 'conf'] )
    return df







def main():
    #推論データの保存場所
    project = 'runs/detect'
    name = 'exp'

    video_dir_list = not_trajectory_path(project)

    for video_dir  in video_dir_list:
        detected_data = mk_df(video_dir)

if __name__ == '__main__':
    main()