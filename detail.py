import requests
from bs4 import BeautifulSoup
import json
import re

from constants import DETAIL_URL, HEADERS

_RE_COMBINE_WHITESPACE = re.compile(r"\s+")

def getJobDetail(id):
    payload = {"oi":id}
    response = requests.request("POST", DETAIL_URL, headers=HEADERS, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")

    raw = soup.text

    parsed = _RE_COMBINE_WHITESPACE.sub(" ", raw).strip()

    return parsed