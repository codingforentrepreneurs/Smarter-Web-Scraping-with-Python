import requests
import urllib.parse

from . import ai

PODCAST_IGNORED_LANGUAGES = ['German', 'Russian', 'Japanese', 'Chinese', "Spanish"]

def url_encode(params):
  return urllib.parse.urlencode(params, quote_via=urllib.parse.quote_plus)

def get_url(search_term="Python programming", max_results=10):
  params = {
      'lang': 'en_us',
      'media': 'podcast',
      'entity': 'podcastEpisode',
      'limit': max_results,
      'term': search_term
  }
  encoded_params = url_encode(params)
  return f"https://itunes.apple.com/search?{encoded_params}"


def perform_search(search_term="Python programming", max_results=10):
    url = get_url(search_term=search_term, max_results=max_results)
    r = requests.get(url, headers={"Content-Type": "application/json"})
    # if r.status_code != 200:
    #    return []
    data = r.json()
    results = data.get('results')
    results = sorted(results, key=lambda x: x['releaseDate'], reverse=True)
    ignore_langs = [x.lower() for x in PODCAST_IGNORED_LANGUAGES]
    final_results = []
    for result in results:
        kind = result.get('kind')
        if kind != "podcast-episode":
            continue
        title = result['trackName']
        pred_lang, is_json = ai.guess_language(title)
        lang = None
        if is_json:
            lang = pred_lang.get("language")
        if f"{lang}".lower() in ignore_langs:
            continue
        result['_predicted_lang'] = lang
        result['_search_term'] = search_term
        final_results.append(result)
    return final_results