import os
from googleapiclient.discovery import build
from src.utils import get_statistic
from googleapiclient.errors import HttpError


class Video:
    """Класс видео"""
    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, id: str) -> None:
        """Инициализация ID видео, остальные данные берем через API"""
        self.id, self.__title, self.__url, self.__view_count, self.__like_count = get_statistic(id)

    def __str__(self) -> str:
        """Вывод названия видео"""
        return f"{self.__title}"

    @property
    def title(self):
        return self.__title

    @property
    def like_count(self):
        return self.__like_count


class PLVideo(Video):
    """Второй класс видео"""

    __api_key: str = os.getenv('API_KEY')
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, video_id: str, playlist_id: str) -> None:
        """Инициализация ID плейлиста, в плейлисте выполняем поиск нужного видео, далее инициализируем сам видосик"""
        self.__playlist_id = playlist_id
        self.__playlist = self.__youtube.playlistItems().list(playlistId=playlist_id,
                                                              part='contentDetails',
                                                              maxResults=50).execute()

        video_id_list = [video['contentDetails']['videoId'] for video in self.__playlist['items']]

        if video_id in video_id_list:
            super().__init__(video_id)
