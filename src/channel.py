import json
import os

class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        return json.dumps(dict_to_print, indent=2, ensure_ascii=False)

        @classmethod
        def get_service(cls):
            return Channel

    def to_json(title,video_count, url):
        file = open("file.json", "w")
        file.write(title,video_count, url)
        return file