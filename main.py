import requests
from bs4 import BeautifulSoup
import json

from constants import URL, PAYLOAD, HEADERS, KEYWORDS,DATA_PATH,REVALIDATE_DATA_PATH
from detail import getJobDetail
from utils import checkLastPage, checkIsCivilEngineeringJob

import os
import csv


def update_data():
    page = 1

    with open(REVALIDATE_DATA_PATH, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['id', 'title', 'published','detail', 'keywords', ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        while True:
            url = URL + "?p=" + str(page)
            response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
            soup = BeautifulSoup(response.content, "html.parser")

            isLastPage = checkLastPage(soup.text)
            if isLastPage:
                break
            
            job_elements = soup.find_all("article", class_="box_offer")

            for job_element in job_elements:
                id = job_element["data-id"]
                title = job_element.find("h1").find("a").text
                published = job_element.find("p", class_="fs13 fc_aux").text
                detail = getJobDetail(id)

                isCivilEnginneringJob = checkIsCivilEngineeringJob(detail)

                if not isCivilEnginneringJob:
                    continue

                keywords = []

                for key, value in KEYWORDS.items():
                    for keyword in value:
                        if keyword in detail:
                            keywords.append(key)
                            break
                
                keywords = "/".join(keywords)
                

                job = {
                    "id": id,
                    "title": title,
                    "published": published,
                    "detail": detail,
                    "keywords": keywords
                }

                writer.writerow(job)
            
            print(f'Page {page} saved')
            page += 1

    
    os.remove(DATA_PATH)
    os.rename(REVALIDATE_DATA_PATH, DATA_PATH)

    with open(REVALIDATE_DATA_PATH, "w") as f:
        pass
