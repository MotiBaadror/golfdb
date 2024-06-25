import os.path

from dir_configs import add_rootpath
from test_video import process_video, Handler
from config import Config
if __name__=='__main__':
    base_path = add_rootpath('data/other_videos')
    output_path = os.path.join(add_rootpath('data/output'))
    os.makedirs(output_path, exist_ok= True)
    config = Config(
        input_path= base_path,
        output_path= output_path,
        video_name = ''
    )
    handler = Handler()
    for file in os.listdir(base_path):
        if file =="output (online-video-cutter.com).mp4":
            config.video_name = file
            process_video(config= config, handler= handler)