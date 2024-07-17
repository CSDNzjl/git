import requests
#正式环境https://api.sgroup.qq.com/
# 你的 API 端点
url = 'https://sandbox.api.sgroup.qq.com/users/@me'

# 你的鉴权令牌
token = 'm38DWSgK2GCJkqSVpYhr9mCUaY3r0xHr'

# 设置请求头
n=1
if(n==1):
    headers = {
        'Authorization': 'Bot 102150060.m38DWSgK2GCJkqSVpYhr9mCUaY3r0xHr'
    }
else:
    headers = {
        'Authorization': 'Bearer AzoeUKA0qgXOF6xofWOG80skcVOHA3wp'
    }
# 发送 GET 请求
response = requests.get(url, headers=headers)

# 打印响应
print(response.status_code)
print(response.json())
