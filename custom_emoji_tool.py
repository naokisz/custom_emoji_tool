import requests
import json
import sys

args = sys.argv
if "--url" in args:
	instance_url = args[args.index("--url") + 1]
else:
	print("インスタンスのURLを入力して下さい。＞")
	instance_url = input()
#print("https://" + instance_url + "/api/v1/custom_emojis")
ret = requests.get("https://" + instance_url + "/api/v1/custom_emojis")
emoji_data = ret.json()

if "--count" in args:
	print("\n" + str(len(emoji_data)))

if "--no_br" in args:
	print("\n", end="")
	for i in emoji_data:
		print(":" + i["shortcode"] + ": ", end="")
	print("\n")
else:
	for i in emoji_data:
	    print(":" + i["shortcode"] + ":")
