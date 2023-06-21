import os
from googleapiclient.discovery import build
import json

from helper.youtube_api_manual import youtube


class Video:
    def __init__(self, video_id: str):
        self.id_video = video_id
        try:

            self.video_info = youtube.get_video(video_id)
            self.video_id = self.video_info['items'][0]['id']
            self.video_title = self.video_info['items'][0]['snippet']['title']
            self.viewCount = self.video_info['items'][0]['statistics']['viewCount']
            self.likeCount = self.video_info['items'][0]['statistics']['likeCount']
        except IndexError:
            self.video_id = video_id
            self.video_info = None
            self.video_title = None
            self.viewCount = None
            self.likeCount = None
            print(f"Видеоролик с id {self.video_id} не найден/не существует")

    def __str__(self):
        return self.title

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=os.getenv('YT_API_KEY'))

    @staticmethod
    def __printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id: str):
        super().__init__(video_id)
        self.playlist_id = playlist_id