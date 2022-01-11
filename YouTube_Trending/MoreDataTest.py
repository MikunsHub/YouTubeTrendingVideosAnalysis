from googleapiclient.discovery import build
import pandas as pd
api_key = "AIzaSyCAiYaB8B3lmhDbD4QIsUjpgIXXK1fexdM"

youtube = build("youtube","v3",developerKey=api_key)

#request for trending videos
nextPageToken = None
while True:
    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        chart="mostPopular",
        maxResults=50,
        pageToken =nextPageToken,
        regionCode="NG"
        )

    #Api response
    response = request.execute()

    #formatting responses
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
    stats = {"viewCount":[],"likeCount":[],"dislikeCount":[],"favoriteCount":[],"commentCount":[]}
    contentdetails = {"duration":[],"dimension":[],"definition":[],"caption":[],"licensedContent":[],"regionRestriction":[],"contentRating":[],"projection":[]}

    for item in response["items"]:
        print()
        #print(item["snippet"]["title"])
        for i,v in enumerate(item["snippet"]):
            vid_snippet[v].append(item["snippet"][v])
        
        for j,v in enumerate(item["statistics"]):
            stats[v].append(item["statistics"][v])
        
        for k,v in enumerate(item["contentDetails"]):
            contentdetails[v].append(item["contentDetails"][v])
        print()
        print("completed")

    nextPageToken = response.get("nextPageToken")

    if not nextPageToken:
        break

#converting API responses to flatfiles
trnd_vid_snippet = pd.DataFrame.from_dict(vid_snippet,orient="index")
trnd_vid_stats = pd.DataFrame.from_dict(stats,orient="index")
trnd_content_details = pd.DataFrame.from_dict(contentdetails,orient="index")

#saving the responses to my local machine
trnd_vid_snippet.to_csv("C:/Users/HP PC/Documents/PersonalProjects/YouTube_Trending/temptables/vid_snippet.csv")
trnd_vid_stats.to_csv("C:/Users/HP PC/Documents/PersonalProjects/YouTube_Trending/temptables/video_stats.csv")
trnd_content_details.to_csv("C:/Users/HP PC/Documents/PersonalProjects/YouTube_Trending/temptables/contentdetails.csv")


