from googleapiclient.discovery import build
import json
api_key = "AIzaSyCAiYaB8B3lmhDbD4QIsUjpgIXXK1fexdM"

youtube = build("youtube","v3",developerKey=api_key)

#request for trending videos
request = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    chart="mostPopular",
    maxResults=200,
    regionCode="NG"
    )

#Api response
response = request.execute()

vid_snippet = json.dumps(response,indent=2)
writeFile = open("vid_snippet.json", "w")
writeFile.write(vid_snippet)
writeFile.close()


"""for item in response["items"]:
    print()
    #print(item["snippet"]["title"])
    for i,v in enumerate(item["snippet"]):
        vid_snippet[v].append(item["snippet"][v])
    
    for j,v in enumerate(item["statistics"]):
        stats[v].append(item["statistics"][v])
    
    for k,v in enumerate(item["contentDetails"]):
        contentdetails[v].append(item["contentDetails"][v])
    print()
    print("completed")"""






