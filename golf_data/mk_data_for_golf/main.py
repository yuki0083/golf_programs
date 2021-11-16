import dir_utils, opencv
import shutil, os
import argparse


#image_dir_path ="./images"#画像の保存先
#video_dir_path = "../raw_data"#動画があるディレクトリ

def run(image_dir_path, video_dir_path,frame_space):
    #video_dir_path = input("動画ディレクトリのパスを入力:")

    dir_utils.make_dir(image_dir_path)

    #動画ディレクトリから動画のパスのリストを取得
    video_list = dir_utils.video_list(video_dir_path)
    #動画からフレームを作成し保存
    frame_space = int(frame_space)
    opencv.save_frames(video_list, image_dir_path, frame_space)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_dir_path',default="./images", help='画像を保存するディレクトリパス' )
    parser.add_argument('--video_dir_path', required=True, help='動画のディレクトリパス')
    parser.add_argument('--frame_space', default=1, help='画像として保存するフレームの間隔')
    args = parser.parse_args()
    return args

def main(args):
    run(args.img_dir_path, args.video_dir_path, args.frame_space)

if __name__ == "__main__":
    args = parse_opt()
    main(args)
