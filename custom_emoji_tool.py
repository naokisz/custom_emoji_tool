import requests
import json
import sys

toot = "@kirishimalab21 "
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

if "--no-br" in args:
	print("\n", end="")
	for i in emoji_data:
		print(":" + i["shortcode"] + ": ", end="")
	print("\n")
#elif "--custom-emoji-add-request-for-astarte" in args:
#	ret_astarte = requests.get("https://kirishima.cloud/api/vi/custom_emojis")
#	astarte_emoji_data = ret_astarte.json()
#	for i in emoji_data:
#		for j in astarte_emoji_data:
#			if i["shortcode"] in j["shortcode"]:
#
#        if len(toot) + len(i["shortcode"]) + 3 + len("@kirishimalab21 ") < 500:
#        	toot = toot + ":" + i["shortcode"] + ": "
#	print("toot")
#	
else:
	for i in emoji_data:
            print(":" + i["shortcode"] + ":")
            #pass
