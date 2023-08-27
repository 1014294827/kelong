import requests
url="www.baidu.com"
response = requests.get(url)
print(response.status_code)
# 我是远程修改的内容
# 在分支上开发内容