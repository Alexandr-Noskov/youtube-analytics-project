import datetime

from datetime import timedelta

from src.video import Video


class PlayList(Video):
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
        """Возвращает ссылку на самое популярное видео"""
        return max(Video.like_count)