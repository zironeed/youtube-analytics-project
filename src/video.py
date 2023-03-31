import os
from googleapiclient.discovery import build


class Video:
    """Класс видео"""
    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, id: str) -> None:
        """Инициализация ID видео, остальные данные берем через API"""
        self.id = id
        self.video = self.__youtube.videos().list(id=id, part='snippet,statistics').execute()

        self.__title = self.video['items'][0]['snippet']['title']
        self.__url = f"https://www.youtube.com/watch?v={id}"
        self.__view_count = self.video['items'][0]['statistics']['viewCount']
        self.__like_count = self.video['items'][0]['statistics']['likeCount']

    def __str__(self) -> str:
        """Вывод названия видео"""
        return f"{self.__title}"


class PLVideo(Video):
    """Второй класс видео"""

    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Инициализация ID плейлиста, в плейлисте производим поиск нужного видео, далее инициализируем сам видосик"""
        self.__playlist_id = playlist_id
        self.__playlist = self.__youtube.playlistItems().list(playlistId=playlist_id,
                                                              part='contentDetails',
                                                              maxResults=50).execute()

        video_id_list = [video['contentDetails']['videoId'] for video in self.__playlist['items']]

        if video_id in video_id_list:
            super().__init__(video_id)
