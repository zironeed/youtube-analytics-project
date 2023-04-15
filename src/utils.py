from helper.youtube_api_manual import youtube


def get_statistic(video_id: str):
    try:
        id = video_id
        video = youtube.videos().list(id=id, part='snippet,statistics').execute()

        title = video['items'][0]['snippet']['title']
        url = f"https://www.youtube.com/watch?v={id}"
        view_count = video['items'][0]['statistics']['viewCount']
        like_count = video['items'][0]['statistics']['likeCount']

        return id, title, url, view_count, like_count

    except IndexError:
        return video_id, None, None, None, None
