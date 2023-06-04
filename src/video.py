import datetime
from googleapiclient.discovery import build

from datetime import timedelta

from helper.youtube_api_manual import api_key


class Video:
    def __init__(self, video_id):
        self.video_id = video_id
        video_response = Video.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()
        self.video_title: str = video_response['items'][0]['snippet']['title']
        self.view_count: int = video_response['items'][0]['statistics']['viewCount']
        self.like_count: int = video_response['items'][0]['statistics']['likeCount']
        self.comment_count: int = video_response['items'][0]['statistics']['commentCount']

    def __str__(self):
        return f'{self.video_title}'

class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    @property
    def total_duration(self):
        """Возвращает объект класса datetime.timedelta с суммарной длительность плейлиста"""
        self.timedelta = timedelta
        datetime.timedelta = Video.timedelta()
        return datetime.timedelta

    def show_best_video(self):
        return max(Video.like_count)
