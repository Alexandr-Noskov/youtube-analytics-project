import self

from helper.youtube_api_manual import video_id

video_response = self.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails', id=video_id).execute()