import os
from googleapiclient.discovery import build
import json

class Video:
    def __init__(self, video_id: str):
        self.id_video = video_id
        try:
            video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                      id=video_id).execute()
            self.title: str = video_response['items'][0]['snippet']['title']
            self.view_count: int = video_response['items'][0]['statistics']['viewCount']
            self.like_count: int = video_response['items'][0]['statistics']['likeCount']
            self.comment_count: int = video_response['items'][0]['statistics']['commentCount']
        except IndexError:
            self.title = None
            self.view_count = None
            self.like_count = None
            self.comment_count = None

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