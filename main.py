import requests

from bs4 import BeautifulSoup
from constants import URL, PAYLOAD, HEADERS,PAGE_START
from utils import checkLastPage, checkIsCivilEngineeringJob,checkIsTraineeJob, checkIsAdHonoremJob
from mainxata import dbClient
from singlejob import checkIsOldJob, getDataFromCard

def update_data():
    page = PAGE_START
    while True:
        url = URL + "?p=" + str(page)
        response = requests.request("GET", url, headers=HEADERS, data=PAYLOAD)
        soup = BeautifulSoup(response.content, "html.parser")

        isLastPage = checkLastPage(soup.text)
        if isLastPage:
            break
        
        job_elements = soup.find_all("article", class_="box_offer")

        for job_element in job_elements:
            isOldJob = checkIsOldJob(job_element)
            if isOldJob:
                continue
            
            job = getDataFromCard(job_element)
            
            title_lower = job["title"].lower()
            detail_lower = job["detail"].lower()

            isCivilEnginneringJob = checkIsCivilEngineeringJob(title_lower, detail_lower)
            if not isCivilEnginneringJob:
                continue

            isTraineeJob = checkIsTraineeJob(title_lower, detail_lower)
            if not isTraineeJob:
                continue

            id = job["id"]
            del job["id"]
            
            record = dbClient.get_by_id('JobOffer', id=id)
            if record is not None:
                print(f'Job {id} already exists in database')
                continue

            isAdHonorem = checkIsAdHonoremJob(title_lower, detail_lower)
            job["isAdHonorem"] = isAdHonorem

            dbClient.create('JobOffer', id=id, record=job)

            print(f'Job {id} added to database')
        
        print(f'Page {page} processed')
        page += 1

update_data()