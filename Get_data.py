import requests
from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    """ Get YouTube video ID from YouTube URL
    Args:
        url (str): YouTube URL.
    Returns:
        YouTube id
    """

    if not url:
        return ""

    # If URL is embedded
    if "embed" in url:
        return url.split("/")[-1]

    parse_result = urlparse(url)
    query = parse_qs(parse_result.query)
    return query["v"][0]

def search_keywords(youtube_url, keyword):
    id = get_video_id(youtube_url)
    transcript = YouTubeTranscriptApi.get_transcript(id)
    """ Search for keyword in a YouTube video.
    Args:
        youtube_url (str): YouTube URL.
    Returns:
        list of timestamp in second(s).
    """
    
    timestamps = list()

    if not keyword or not youtube_url:
        return timestamps

    if not transcript:
        print("NO CONTENT")
        return timestamps


    for i in transcript:
        if keyword in i["text"]:
            timestamps.append(float(i["start"]))
    return timestamps


if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=EeQ8pwjQxTM"
    keyword = "sort"
    timestamps = search_keywords(url, keyword)
    print(timestamps)
