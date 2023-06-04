import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API youtube."""
        return cls.youtube

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
        if not isinstance(other, Channel):
            raise ValueError("Складывать можно только два объекта Channel.")
        else:
            return int(self.subscriber_count) + int(other.subscriber_count)

    def __sub__(self, other):
        """Метод для операции вычитания"""
        return int(self.subscriber_count) - int(other.subscriber_count)

    def __lt__(self, other):
        """Для операции сравнения «меньше»"""
        return int(self.subscriber_count) < int(other.subscriber_count)

    def __le__(self, other):
        """Для сравнения «меньше» или «равно»"""
        return int(self.subscriber_count) <= int(other.subscriber_count)

    def __gt__(self, other):
        """Метод для операции сравнения «больше»"""
        return int(self.subscriber_count) > int(other.subscriber_count)

    def __ge__(self, other):
        """Метод для операции сравнения «больше» или «равно»"""
        return int(self.subscriber_count) >= int(other.subscriber_count)

    def print_info(self) -> None:
        """Выводит информацию о канале"""
        channel = Channel.get_service().channels().list(id=self.__channel_id, part='snippet,statistics').execute()
        info = json.dumps(channel, indent=2, ensure_ascii=False)
        print(info)

    def to_json(self, file_name):
        yt_dict = {}
        yt_dict["id"] = self.__channel_id
        yt_dict["title"] = self.title
        yt_dict["description"] = self.description
        yt_dict["url"] = self.url
        yt_dict["subscriber_count"] = self.subscriber_count
        yt_dict["video_count"] = self.video_count
        yt_dict["view_count"] = self.view_count
        with open(file_name, 'w', encoding="UTF-8") as file:
            json.dump(yt_dict, file, indent=2, ensure_ascii=False)