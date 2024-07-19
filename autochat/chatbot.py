import json
import os
import config
from openai import OpenAI

class ChatBot:
    def __init__(self, api_key, base_url):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.history_user_path = config.history_user_path
        self.history_system_path = config.history_system_path
        self.load_history()

    def load_history(self):
        if os.path.exists(self.history_user_path):
            with open(self.history_user_path, 'r', encoding='utf-8') as file:
                self.history_user = json.load(file)
        else:
            self.history_user = []

        if os.path.exists(self.history_system_path):
            with open(self.history_system_path, 'r', encoding='utf-8') as file:
                self.history_system = json.load(file)
        else:
            self.history_system = []

    def save_history(self):
        with open(self.history_user_path, 'w', encoding='utf-8') as file:
            json.dump(self.history_user, file, ensure_ascii=False, indent=4)

        with open(self.history_system_path, 'w', encoding='utf-8') as file:
            json.dump(self.history_system, file, ensure_ascii=False, indent=4)

    def chat(self, query):
        self.history_user.append({"role": "user", "content": query})
        completion = self.client.chat.completions.create(
            model="moonshot-v1-8k",
            messages=self.history_user[-5:] + self.history_system+[{"role": "assistant", "content": "同学你好", "partial": True}],
            temperature=0.2,
        )
        result = "同学你好"+completion.choices[0].message.content
        self.history_user.append({"role": "assistant", "content": result})
        self.save_history()
        print(result)
        return 0