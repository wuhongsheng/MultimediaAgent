from outlines.models import openai
from swarm import Swarm, Agent
from openai import OpenAI
from run import run_demo_loop
import os
from minicpm import llama_cpp_inference
import subprocess
model = "deepseek-chat"

def transfer_to_agent_video():
    return video_agent

def transfer_to_agent_audio():
    return audio_agent

def transfer_back_to_triage():
    """Call this function if a user is asking about a topic that is not handled by the current agent."""
    return triage_agent

def create_swarm():
    client = OpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("API_BASE")
    )
    # swarm = Swarm(client=client)
    return Swarm(client=client)

def create_client():
    client = OpenAI(
        api_key=os.getenv("API_KEY"),
        base_url=os.getenv("API_BASE")
    )
    return client

def init():
    """初始化"""

def asr(url):
    """语音识别"""
    from funasr import AutoModel
    # paraformer-zh is a multi-functional asr model
    # use vad, punc, spk or not as you need
    model = AutoModel(model="paraformer-zh", vad_model="fsmn-vad", punc_model="ct-punc")
    res = model.generate(input=url,
                         batch_size_s=300,
                         hotword='')
    return res

def file_process_by_ffmpeg(command):
    try:
        process = subprocess.run(command,shell=True, capture_output=True, text=True)
        print(f"命令输出：\n{process.stdout}")
        print(f"命令错误输出：\n{process.stderr}")
        return f'处理完成'
    except Exception as e:
        return f"出现错误：" + str(e)

def video_question_answer(prompt, url):
    """视觉问答"""
    return llama_cpp_inference(prompt,url)


triage_agent = Agent(
    name="Triage Agent",
    instructions="确定哪个代理最适合处理用户的请求，并将对话转交给该代理。",
    functions=[transfer_to_agent_video, transfer_to_agent_audio],
    model=model,
)

video_agent = Agent(
    name="Video Agent",
    instructions="负责处理视频或图像相关任务，并回复相关结果。会话完成或者出错返回triage_agent",
    functions=[video_question_answer, transfer_back_to_triage],
    model=model,
)

audio_agent = Agent(
    name="Audio Agent",
    instructions="负责处理音频相关任务，并回复相关结果，会话完成或者出错返回triage_agent",
    functions=[asr, transfer_back_to_triage],
    model=model,
)

def test():
    client = create_client()
    response = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "请总结下这段视频的内容仅返回文本 /Users/whs/Downloads/section_6_011.55_013.96.mp4"},
        ],
        stream=False
    )
    print(response)
    print(response.choices[0].message.content)



if __name__ == "__main__":
    # test()
    run_demo_loop(triage_agent,client=create_client(), debug=True)

