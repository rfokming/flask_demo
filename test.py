print("hello")
import os
import json
#f = open(os.environ["HOME"] + "/data.json", "r", encoding="utf-8")
f = open("data.json", "r", encoding="utf-8")
data = json.load(f)
f.close()
#print(data)

print(data["dsp_apim_create_test"])
print(data["dsp_apim_create_test"]["story"])