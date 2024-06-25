from dataclasses import dataclass


@dataclass
class Config:
    input_path: str
    output_path: str
    seq_length:int = 64
    video_name: str = None