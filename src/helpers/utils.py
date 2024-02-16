import pathlib
import requests
import shutil
from urllib.parse import unquote

def convert_encoded_url(encoded_url):
    """
    Decode any encoded URL strings for
    episdoe downloading
    """
    decoded_url = unquote(encoded_url)
    return decoded_url


def clean_filename(filename):
    """
    Remove any query parameters 
    that may be included in the file name
    """
    if not isinstance(filename, str):
        return None
    if '?' in filename:
        cleaned_filename = filename.split('?', 1)[0]
    else:
        cleaned_filename = filename
    return cleaned_filename


def get_fname(url):
    fname = pathlib.Path(url).name 
    fname = clean_filename(fname)
    suffix = pathlib.Path(fname).suffix
    if suffix == ".mp3":
        return "audio.mp3"
    elif suffix == ".mp4":
        return "video.mp4"
    else:
        return

def download_file(url, destination_path="."):
    fname = get_fname(url)
    outpath = pathlib.Path(destination_path).resolve() / fname
    with requests.get(url,  stream=True) as r:
        with open(str(outpath), 'wb') as f:
            shutil.copyfileobj(r.raw, f)
    return fname