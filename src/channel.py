import json
import os

from googleapiclient.discovery import build


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
        """Возвращает объект для работы с API youtube."""
        return cls.youtube

    def to_json(self, filename: str) -> None:
        """Сохраняет данные экземпляра класса в файл."""
        channel_data = {
            'channel_id': self.channel_id,
            'title': self.channel_name,
            'description': self.chanel_description,
            'url': self.channel_link,
            'subscriber_count': self.number_of_subscribers,
            'video_count': self.number_of_videos,
            'view_count': self.total_views,
        }
        with open(filename, 'w') as fp:
            json.dump(channel_data, fp)

    def __str__(self):
        """Выведение названия канала и ссылки"""
        return f'{self.channel_name}, {self.channel_link}'

    def __add__(self, other):
        """Метод для сложения количества подписчиков каналов"""
        return self.number_of_subscribers + other.number_of_subscribers

    def __sub__(self, other):
        """Метод для операции вычитания"""
        return self.number_of_subscribers - other.number_of_subscribers

    def __lt__(self, other):
        """Для операции сравнения «меньше»"""
        return self.number_of_subscribers < other.number_of_subscribers

    def __le__(self, other):
        """Для сравнения «меньше» или «равно»"""
        return self.number_of_subscribers <= other.number_of_subscribers

    def __gt__(self, other):
        """Метод для операции сравнения «больше»"""
        return self.number_of_subscribers > other.number_of_subscribers

    def __ge__(self, other):
        """Метод для операции сравнения «больше» или «равно»"""
        return self.number_of_subscribers >= other.number_of_subscribers
