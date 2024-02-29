# Smater Web Scraping with Python Selenium and Llama2
Generate podcast clips related to daily top submissions on Hacker News via web scraping with Python & Selenium, generative ai with Ollama and LLama2, Transcript generation OpenAI Whisper, iTunes Podcast Search, and more.

Coming soon


## Requirements
- Python 3.10 and up
- A [Bright Data Account](https://brdta.com/justin) (includes $25 credit)
- ffmpeg (required for transcribing audio with OpenAI Whisper)


### A Proxy-based Web Scraping approach
In this repo, we use a web scraping proxy service from Bright Data. Using a proxy service makes our requests more reliable. You can see the actual code for the Selenium-based remote connection here [src/helpers/brightdata.py](./src/helpers/brightdata.py).

#### With Remote Proxy
our computer -> request -> proxy -> web server -> proxy -> response -> our computer

#### Without Remote Proxy
our computer -> request -> web server -> response -> our computer

### Usage
```python
# from 'src/2 - Connection Sample.ipynb'
from selenium.webdriver import Remote, ChromeOptions

# import this function
from helpers.brightdata import get_sbr_connection

options = ChromeOptions()

# options.headless = True # old method
options.add_argument("--headless=new") # new method

url = 'https://news.ycombinator.com'

with Remote(sbr_connection, options=options) as driver:
    driver.get(url)
    print(driver.page_source)
```



## Getting Started

### Clone project
```
mkdir -p ~/dev/smarter-scraping
cd ~/dev/smarter-scraping
git clone https://github.com/codingforentrepreneurs/Smarter-Web-Scraping-with-Python .
```

### (Optional) Working through the course?
Use the `course_start` branch with:

mac/linux
```bash
git checkout course_start
rm -rf .git 
git init
```

windows
```powershell
git checkout course_start
Remove-Item .git -Recurse -Force
git init
```
## Create a Python Virtual Environment

```bash
cd ~/dev/smarter-scraping # or where you cloned the repo
```

mac/linux
```bash
python3 -m venv venv
```

windows
```powershell
c:\Python311\python.exe -m venv venv
```

### Activate the virtual enviornment
Always activate your environment!

```bash
cd ~/dev/smarter-scraping # or where you cloned the repo
```

mac/linux
```bash
source venv/bin/activate
```

windows
```powershell
.\venv\Scripts\activate
```

If done correctly, your command line should start with `(venv)`


### Install requirements
With virtual envionoment activated (e.g. `(venv)`), run:

```bash
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

### Implement Environment Variables with `dotenv`

mac/linux
```bash
cp sample-env-file .env
```

windows
```powershell
Copy-Item .env.sample -Destination .env
```

Be sure to add your Bright Data proxy information:
- `BRIGHT_DATA_USERNAME`
- `BRIGHT_DATA_PASSWORD`
- `BRIGHT_DATA_HOST`

Add Ollama data too (for Running the OpenAI drop-in replacement Llama2)
- `OPENAI_BASE_URL=http://localhost:11434/v1`
- `OPENAI_API_KEY=ollama`
- `OPENAI_COMPLETION_MODEL=llama2`

### Loading Environment Variables

With code that lives inside the `src/` directory, you can import the `helpers` module to load your environment variables. 

We created a simple function to extend the incredible [python-decouple](https://pypi.org/project/python-decouple/) package (it's in [src/helpers/env.py](./src/helpers/env.py)):

```python
import helpers

MY_VAR = helpers.config('MY_VAR', default="Not set", cast=str)
```


### Run Jupyter
Explore the notebooks!
```
jupyter notebook
```

