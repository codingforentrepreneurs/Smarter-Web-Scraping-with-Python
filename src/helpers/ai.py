from openai import OpenAI
import json
from .env import config

OPENAI_BASE_URL = config('OPENAI_BASE_URL', default=None)
OPENAI_API_KEY = config('OPENAI_API_KEY', default=None)
OPENAI_COMPLETION_MODEL = config('OPENAI_COMPLETION_MODEL', default=None)

def get_openai_client():
    if not OPENAI_BASE_URL:
        return OpenAI(api_key=OPENAI_API_KEY)
    return OpenAI(
        base_url =OPENAI_BASE_URL,
        api_key=OPENAI_API_KEY, # required, but unused
    )

def perform_completion(messages=[], client=None, raw=None):
    if not isinstance(client, OpenAI):
        client = get_openai_client()
    response = client.chat.completions.create(
      model=OPENAI_COMPLETION_MODEL,
      messages=messages,
      response_format={ "type" : "json_object" }
    )
    if raw:
        return response
    try:
        return json.loads(response.choices[0].message.content), True
    except:
        return response.choices[0].message.content, False


def guess_language(content="", client=None, raw=None):
    system_prompt = "".join([
        "You are an expert at deciphering the type of language of text.",
    ])
    prompt_start = "".join([
        "Repond only with your best guess of what the language is of the input text. Use real human languages.",
        "Use the following:"
    ])
    prompt_end="Using format of \"{'language': <generated-answer>}\" return a response with json"
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user", 
            "content": f"{prompt_start} {content} {prompt_end}",
        }
    ]
    return perform_completion(messages, client=client, raw=raw)
    

def extract_summary_and_keywords(content="", client=None, raw=None):
    system_prompt = "".join([
        "You are an expert web scraper and researcher.",
        "When you get data, you perform expert-level summarization and keyword extraction.",
    ])
    prompt_start = "".join([
        "Extract a 1-word subject of the text as the top ranked keyword.",
        "Extract and rank top keywords based on the subject matter of only of the text.",
        "Rank each keyword based on the keyword's importance to the subject matter of the text.",
        "Provide a concise summary of the contents of the text",
        "The summary should not include anything related to the discussion nature of the text.",
        "The summary should not include anything related to the conversation nature of the text.",
        "The summary should be a minimum 3 paragraphs.",
        "Use the following text: "
    ])
    prompt_end="Using format of \"{'summary': <generated-summary>, 'keywords': [{value: 'a', rank: 1}, {value: 'b', rank: 2}, {value: 'c', rank: 3}, {value: 'd', rank: 4}, {value: 'e', rank: 5}]}\" return a response with json"
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user", 
            "content": f"{prompt_start} {content} {prompt_end}",
        }
    ]
    return perform_completion(messages, client=client, raw=raw)
    