import json
import os
import time
from openai import OpenAI

# 频繁请求报错的异常处理
# 用户输入有选择性地加入json文件中
class ChatBot:
    def __init__(self, api_key, base_url):
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.history_user_path = "data/history_user_assistant.json"
        self.history_system_path = "data/history_system.json"
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
            messages=self.history_user + self.history_system,
            temperature=0.2,
        )
        result = completion.choices[0].message.content
        self.history_user.append({"role": "assistant", "content": result})
        self.save_history()
        return result

def main():
    api_key = "sk-ZaBn9vmW67ToxLxzWxGOWPa0OgGkfyR4bmrOlmKJSWYXgHX3"
    base_url = "https://api.moonshot.cn/v1"
    bot = ChatBot(api_key, base_url)

    while True:
        user_input = input("请输入一句话（输入'退出'结束程序）：")
        if user_input.lower() == '退出':
            print("程序已退出。")
            break
        else:
            print("正在处理您的请求...")
            print(bot.chat(user_input))

            # # 等待两秒钟
            # start_time = time.time()
            # while time.time() - start_time < 5:
            #     if input():  # 如果用户输入，则提醒稍等
            #         print("稍等...")
            # print("可以继续谈话啦")

if __name__ == '__main__':
    main()