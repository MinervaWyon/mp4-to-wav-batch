import os
import subprocess

video_root = r'D:\uni\数学建模\Raw\ch-simsv2s\Raw'  # 修改为您的实际路径

for root, dirs, files in os.walk(video_root):
    for file in files:
        if file.endswith('.mp4'):
            video_path = os.path.join(root, file)
            wav_path = video_path.replace('.mp4', '.wav')
            # 如果 wav 已存在，跳过（可选）
            if os.path.exists(wav_path):
                print(f"Skip existing: {wav_path}")
                continue
            cmd = [
                'ffmpeg', '-i', video_path,
                '-ar', '16000',      # 采样率 16kHz
                '-ac', '1',          # 单声道
                '-y',                # 覆盖输出
                wav_path
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"Converted: {video_path} -> {wav_path}")