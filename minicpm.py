import time
import subprocess
import os

# 常见的视频文件扩展名
VIDEO_EXTENSIONS = ['.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.webm', '.m4v']
def is_video_file(file_path):
    # 获取文件的扩展名并转换为小写
    ext = os.path.splitext(file_path)[1].lower()
    # 判断扩展名是否在视频扩展名列表中
    return ext in VIDEO_EXTENSIONS

def llama_cpp_inference(prompt,file_path):
    # 使用 subprocess 调用 llama.cpp
    print(prompt)
    print(file_path)
    start = time.time()
    try:
        if is_video_file(os.path.split(file_path)[1]):
            video = file_path
            command = f'./llama-minicpmv-cli -m ./models/ggml-model-Q4_K_M.gguf --mmproj ./mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --video "{video}" -p "{prompt}"'
        else:
            img = file_path
            command = f'./llama-minicpmv-cli -m ./models/ggml-model-Q4_K_M.gguf --mmproj ./mmproj-model-f16.gguf -c 4096 --temp 0.7 --top-p 0.8 --top-k 100 --repeat-penalty 1.05 --image "{img}" -p "{prompt}"'

        print(command)

        # 使用 subprocess 运行命令并捕获输出
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout)
        output = result.stdout
        print("cost time{:.2f}".format(time.time() - start))
        return output.strip()
    except Exception as e:
        return f"出现错误："+str(e)