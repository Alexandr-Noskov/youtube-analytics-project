import json
import os
from distutils.command.build import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str, channel_name, chanel_description, channel_link, number_of_subscribers,
                 number_of_videos, total_views) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.chanel_description = chanel_description
        self.channel_link = channel_link
        self.number_of_subscribers = number_of_subscribers
        self.number_of_videos = number_of_videos
        self.total_views = total_views

    def print_info(self, dict_to_print, indent, ensure_asci) -> None:
        """Выводит в консоль информацию о канале."""
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

    @classmethod
    def get_service(cls):
        return Channel

    def to_json(title,video_count, url):
        file = open("file.json", "w")
        file.write(title,video_count, url)
        return file

