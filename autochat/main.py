from chatbot_stream import ChatBot
import config

def main():
    bot = ChatBot(config.api_key, config.base_url)

    while True:
        user_input = input("\n请输入一句话（输入'退出'结束程序）：")
        if user_input.lower() == '退出':
            print("程序已退出。")
            break
        else:
            bot.chat(user_input)

if __name__ == '__main__':
    main()