from urllib.parse import urlparse, parse_qs


def get_video_id(url):
    parsed_url = urlparse(url)
    video_id = parse_qs(parsed_url.query)["v"][0]

    return video_id
