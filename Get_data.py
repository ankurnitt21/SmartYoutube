import requests
from urllib.parse import urlparse, parse_qs
from xml.etree import ElementTree
from pytube import YouTube


OK = 200


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
    """ Search for keyword in a YouTube video.

    Args:
        youtube_url (str): YouTube URL.

    Returns:
        list of timestamp in second(s).
    """

    timestamps = list()

    if not keyword or not youtube_url:
        return timestamps

    #status_code, content = transcribe_video(youtube_url)
    status_code=200
    source = YouTube(youtube_url)
    en_caption = source.captions.get_by_language_code('en')
    content = en_caption.xml_captions

    if not content:
        print("NO CONTENT")
        return timestamps

    if status_code == OK:
        tree = ElementTree.fromstring(content)
        for node in tree:
            if keyword in node.text:
                print(node.text)
                print(node.attrib)
                timestamps.append(float(node.attrib["start"]))

    return timestamps


if __name__ == '__main__':
    url = "https://www.youtube.com/watch?v=EeQ8pwjQxTM"
    keyword = "sort"
    timestamps = search_keywords(url, keyword)
    print(timestamps)
