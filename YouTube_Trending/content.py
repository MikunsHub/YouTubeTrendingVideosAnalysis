from googleapiclient.discovery import build
import pandas as pd
import json
api_key = "AIzaSyCAiYaB8B3lmhDbD4QIsUjpgIXXK1fexdM"

youtube = build("youtube","v3",developerKey=api_key)

#request for trending videos
request = youtube.videos().list(
    part="snippet,statistics,contentDetails",
    chart="mostPopular",
    maxResults=1,
    regionCode="NG"
    )

#Api response
response = request.execute()
# content_json = json.dumps(response,indent=2)
vid_snippet = {
    "publishedAt":[],
    "channelId":[],
    "title":[],
    "description":[],
    "thumbnails":[],
    "channelTitle":[],
    "tags":[],
    "categoryId":[],
    "liveBroadcastContent":[],
    "defaultLanguage":[],
    "localized":[],
    "defaultAudioLanguage":[]
}

for item in response["items"]:
    # print(item["contentDetails"]["regionRestriction"]["allowed"])
    print()
    #print(item["snippet"]["thumbnails"]["default"]["url"])

    for i,v in enumerate(item["snippet"]):
        vid_snippet[v].append(item["snippet"][v])
        #print( item["snippet"][v])


print()   

#print(vid_snippet)     
trnd_vid_snippet = pd.DataFrame.from_dict(vid_snippet,orient="index")
trnd_vid_snippet.to_csv("C:/Users/HP PC/Documents/PersonalProjects/YouTube_Trending/temptables/vid_snippet.csv")





#print(contentdetails)

    
