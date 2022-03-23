#!/usr/bin/bash
<< COMMENTOUT
ゴルフヘッドの軌道描画
スイングスピードの計算
$shell_script/video_processing.sh runs/detect/exp/
COMMENTOUT
video_dir=$1
video_path=runs/detect/exp/IMG_9733.mp4

python3 ./mk_df/mk_df.py
python mk_df/video_property.py --video_dir $video_dir --video_path $video_path
python3 ./draw_trajectory/main.py --video_dir $video_dir --video_path $video_path
python3 swing_speed_measurement/cal_length_per_pixel.py
python3 swing_speed_measurement/cal_head_velocity.py