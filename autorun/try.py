import json
import autochat.config as config
from openai import OpenAI

client = OpenAI(
    api_key=config.api_key,  # 在这里将 MOONSHOT_API_KEY 替换为你从 Kimi 开放平台申请的 API Key
    base_url="https://api.moonshot.cn/v1",
)

system_prompt = """
你是月之暗面（Kimi）的智能客服，你负责回答用户提出的各种问题。请参考文档内容回复用户的问题，你的回答是地址和文件名。

请使用如下 JSON 格式输出你的回复：

{
    "path": "地址信息",
    "name": "文件名称",
}

"""

completion = client.chat.completions.create(
    model="moonshot-v1-8k",
    messages=[
        {"role": "system",
         "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
        {"role": "system", "content": system_prompt},  # <-- 将附带输出格式的 system prompt 提交给 Kimi
        {"role": "user", "content": "帮我在C:\\Users\\cheng\\PycharmProjects\\pythonProject\\autorun创建一个one.py文件"}
    ],
    temperature=0.3,
    response_format={"type": "json_object"},  # <-- 使用 response_format 参数指定输出格式为 json_object
)

# 由于我们设置了 JSON Mode，Kimi 大模型返回的 message.content 为序列化后的 JSON Object 字符串，
# 我们使用 json.loads 解析其内容，将其反序列化为 python 中的字典 dict。
content = json.loads(completion.choices[0].message.content)
print(content)