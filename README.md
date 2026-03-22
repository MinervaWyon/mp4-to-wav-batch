# Video to WAV Batch Converter

This Python script recursively traverses a directory, finds all `.mp4` files, and converts them to 16 kHz mono WAV audio files using `ffmpeg`. Existing `.wav` files are skipped to avoid redundant conversions.

## Features

- Recursively scans a root directory for `.mp4` files.
- Converts each video to a WAV audio file with:
  - Sample rate: 16 kHz
  - Channels: 1 (mono)
- Overwrites output files if they already exist (controlled by `-y` flag).
- Skips conversion if the WAV file already exists (optional).

## Requirements

- Python 3.x
- `ffmpeg` installed and available in the system PATH.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/video2wav-converter.git
   cd video2wav-converter
Ensure ffmpeg is installed:

Windows: Download from ffmpeg.org and add to PATH.

macOS: brew install ffmpeg

Linux: sudo apt install ffmpeg (or equivalent).

Usage
Edit the script and set the video_root variable to the directory containing your .mp4 files:

python
video_root = r'D:\uni\数学建模\Raw\ch-simsv2s\Raw'  # change this
Run the script:

bash
python convert.py
The script will print progress messages for each conversion or skipped file.

Customization
You can modify the ffmpeg command parameters inside the script to change the audio format, sample rate, or channels. For example:

python
cmd = [
    'ffmpeg', '-i', video_path,
    '-ar', '16000',      # sample rate (Hz)
    '-ac', '1',          # mono
    '-y',                # overwrite output
    wav_path
]
Notes
The script assumes that the input files have the .mp4 extension.

Output WAV files are saved in the same folder as the original MP4, with the same base name but .wav extension.

If you want to re-convert all files, delete the existing .wav files or remove the skip check.

License
This project is open-source and available under the MIT License.


# 视频批量转 WAV 音频工具

本 Python 脚本递归遍历指定目录，查找所有 `.mp4` 视频文件，并利用 `ffmpeg` 将其转换为 16 kHz 单声道 WAV 音频文件。已存在的 `.wav` 文件会被跳过，避免重复转换。

## 功能特点

- 递归扫描根目录下的所有 `.mp4` 文件。
- 将每个视频转换为 WAV 音频文件，参数如下：
  - 采样率：16 kHz
  - 声道数：1（单声道）
- 如果输出文件已存在，默认覆盖（由 `-y` 参数控制）。
- 可选：如果 WAV 文件已存在则跳过转换（脚本中已包含此逻辑）。

## 环境要求

- Python 3.x
- `ffmpeg` 已安装，并添加至系统环境变量（PATH）中。

## 安装步骤

1. 克隆本仓库：
   ```bash
   git clone https://github.com/yourusername/video2wav-converter.git
   cd video2wav-converter
确保 ffmpeg 已安装：

Windows：从 ffmpeg.org 下载并添加到 PATH。

macOS：brew install ffmpeg

Linux：sudo apt install ffmpeg（或相应包管理器命令）

使用方法
编辑脚本，将 video_root 变量设置为存放 .mp4 文件的目录路径：

python
video_root = r'D:\uni\数学建模\Raw\ch-simsv2s\Raw'  # 请修改为实际路径
运行脚本：

bash
python convert.py
脚本会输出转换进度信息，或提示已存在的文件被跳过。

自定义参数
你可以根据需要修改脚本中的 ffmpeg 命令参数，例如调整采样率、声道数等：

python
cmd = [
    'ffmpeg', '-i', video_path,
    '-ar', '16000',      # 采样率（Hz）
    '-ac', '1',          # 单声道
    '-y',                # 覆盖输出文件
    wav_path
]
注意事项
脚本默认仅处理扩展名为 .mp4 的文件。

输出 WAV 文件与原始视频保存在同一文件夹下，文件名相同但扩展名为 .wav。

如需强制重新转换所有文件，可删除已有的 .wav 文件，或注释掉跳过检查的代码。

许可证
本项目采用 MIT 许可证，开源免费使用。
