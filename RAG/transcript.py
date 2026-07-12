from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    NoTranscriptFound,
    TranscriptsDisabled,
)


def get_transcript(video_id):
    api = YouTubeTranscriptApi()

    try:
        transcript = api.fetch(video_id, languages=["en"])
        return transcript, "en"

    except NoTranscriptFound:
        transcript = api.fetch(video_id, languages=["hi"])
        return transcript, "hi"

    except TranscriptsDisabled:
        raise Exception(
            "This video does not have subtitles/captions enabled."
        )