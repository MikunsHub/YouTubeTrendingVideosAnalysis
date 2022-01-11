import json

with open("vid_snippet.json") as f:
    data = json.load(f)

for item in data["items"]:
    for v in item["snippet"]["thumbnails"]:
        #print(item["snippet"]["thumbnails"][v])
        print(v)
        print()
        for w in item["snippet"]["thumbnails"][v]:
            print(w)
    
   