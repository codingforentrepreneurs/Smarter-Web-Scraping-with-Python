import json

detail_pattern = "https://news.ycombinator.com/item?id={item_id}"

def save_json_data(data, path=None):
    id = data.get('id')
    json_data = json.dumps(data, indent=4)
    if path:
        path.write_text(json_data)


def scrape_link(url=None, driver=None):
    if url is None:
        return ""
    if not f"{url}".startswith("http"):
        return ""
    if not driver:
        return ""
    driver.get(url)
    return driver.page_source


def scrape_and_save(data, key, driver=None, path=None):
    if path is None:
        return 
    try:
        data = scrape_link(data.get(key), driver=driver)
    except:
        data = None
    if data is not None:
        path.write_text(data)