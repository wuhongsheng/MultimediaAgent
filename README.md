# Multimedia Agent: Agentic Multimedia File Process using Aulti Agent cooperation

This is a Python demonstration of a multi agent cooperate for multimedia file process. The main steps are:
1. Prompt an LLM to triage agent;
2. Triage agent transfer the conversation to that agent;
3. Specific agent calls the tool to obtain the model and then processes it to reply to the user with relevant results


## Getting Started

To get started with `MultimediaAgent`, follow these steps:

### Installation:

```bash
git clone https://github.com/wuhongsheng/MultimediaAgent.git
pip install -r requirements
```

### Usage:

```bash
huggingface-cli download --resume-download openbmb/MiniCPM-V-2_6-gguf ggml-model-Q4_K_M.gguf --local-dir ./models/
huggingface-cli download --resume-download openbmb/MiniCPM-V-2_6-gguf mmproj-model-f16.gguf --local-dir ./models/
export API_KEY="your api key"
export API_BASE="your api server url"
python agents.py
```

## License

Multimedia Agent is released under the **MIT License**. You are free to use, modify, and distribute the code
for both commercial and non-commercial purposes.


