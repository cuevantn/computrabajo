import requests
from bs4 import BeautifulSoup
import re

from constants import DETAIL_URL, HEADERS
from utils import remove_before_regex

def remove_after_substring(text, sub_str):
    pattern = rf".*{sub_str}.*?(\n|\r\n|\r)"
    return re.sub(pattern, '', text, flags=re.DOTALL)

def remove_sentences(text, startStr,endStr = ""):
    pattern = rf"{startStr}.*?{endStr}"
    return re.sub(pattern, '', text, flags=re.DOTALL, count=1)

def replace_newlines(text):
    pattern = r"\n{2,}"
    return re.sub(pattern, '\n', text)

def format_string(text):
    pattern1 = r"([a-z])([A-Z])"
    pattern2 = r"-\s*"
    pattern3 = r":\s*"
    pattern4 = r"([a-z])([0-9])"
    pattern5 = r"\n"

    text = re.sub(pattern1, r"\1\n\2", text)
    text = re.sub(pattern2, '\n    - ', text)
    text = re.sub(pattern3, ':\n    ', text)
    text = re.sub(pattern4, r"\1 \2", text)
    text = re.sub(pattern5, r'\r\n', text)

    return text


def getJobDetail(id, title):
    payload = {"oi":id}
    response = requests.request("POST", DETAIL_URL, headers=HEADERS, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")

    raw = soup.text
    
    parsed = remove_before_regex(raw, "Postularme\s*Imprimir", start_from="end")
    parsed = remove_before_regex(parsed, "Imprimir\s*Denunciar", start_from="start")

    parsed = parsed.replace(title, "")

    parsed = replace_newlines(parsed)
    parsed = format_string(parsed)
    parsed = parsed.strip()

    parsed = '\n'.join(parsed.split("\n")[5:-3])

    return parsed