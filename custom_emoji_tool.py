import requests
import json

print("インスタンスのURLを入力して下さい。＞")
instance_url = input()
print("https://" + instance_url + "/api/v1/custom_emojis")
ret = requests.get("https://" + instance_url + "/api/v1/custom_emojis")
emoji_data = ret.json()
#print(emoji_data)
for i in emoji_data:
    print(" :" + i["shortcode"] + ": ")
