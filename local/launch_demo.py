import os.path

from dir_configs import add_rootpath
from test_video import process_video
from config import Config
if __name__=='__main__':
    base_path = add_rootpath('data')
    output_path = os.path.join(base_path, 'output')
    os.makedirs(output_path, exist_ok= True)
    config = Config(
        input_path= base_path,
        output_path= output_path,
        video_name = 'test_video.mp4'
    )

    process_video(config= config)