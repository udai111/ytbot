import os
import subprocess

def gpu_watermark(input_path, output_path, text="Subscribe!"):
    """
    Uses ffmpeg with NVENC to overlay text quickly.
    Requires NVIDIA Docker or a local environment with GPU + drivers.
    """
    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-vf", f"drawtext=text='{text}':fontcolor=white:fontsize=24:x=10:y=10",
        "-c:v", "h264_nvenc",
        "-preset", "fast",
        "-c:a", "copy",
        output_path
    ]
    subprocess.run(command)

def process_video_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for f in os.listdir(input_folder):
        if f.endswith(".mp4"):
            in_path = os.path.join(input_folder, f)
            out_path = os.path.join(output_folder, f"wm_{f}")
            gpu_watermark(in_path, out_path)
