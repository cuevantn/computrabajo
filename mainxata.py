import os

from xata.client import XataClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

XATA_API_KEY = os.getenv('XATA_API_KEY')
XATA_FALLBACK_BRANCH = os.getenv('XATA_FALLBACK_BRANCH')

dbClient = XataClient(XATA_API_KEY, branch_name=XATA_FALLBACK_BRANCH)