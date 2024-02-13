# Smater Web Scraping with Python Selenium and Llama2
Generate podcast clips related to daily top submissions on Hacker News via web scraping with Python & Selenium, generative ai with Ollama and LLama2, Transcript generation OpenAI Whisper, iTunes Podcast Search, and more.

Coming soon

## Requirements
- Python 3.10 and up
- ffmpeg (required for transcribing audio with OpenAI Whisper)

## Getting Started

Clone project
```
mkdir -p ~/dev/smarter-scraping
cd ~/dev/smarter-scraping
git clone https://github.com/codingforentrepreneurs/Smarter-Web-Scraping-with-Python .
```

Create a Python Virtual Environment:
- run `cd ~/dev/smarter-scraping` then...
- mac/linux: `python3 -m venv venv`
- windows: `c:\Python311\python.exe -m venv venv`

Activate the virtual enviornment:
- run `cd ~/dev/smarter-scraping` then...
- mac/linux: `source venv/bin/activate`
- windows: `.\venv\Scripts\activate`

Install requirements
```bash
(venv) python -m pip install pip --upgrade
(venv) python -m pip install -r requirements.txt
```

Run Jupyter
```
jupyter notebook
```

