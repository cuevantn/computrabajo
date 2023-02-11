from detail import getJobDetail
from utils import parsePublicationDate


def getCompanyLocation(raw_element):
    company = "Importante empresa del sector"
    if raw_element.find("a") is not None:
        company = raw_element.find("a").text

    location = raw_element.text.replace(company, "").replace('"','').strip()

    if company == "Importante empresa del sector":
        company = None
    
    return [company, location]

def checkIsOldJob(job_element):
    publishedAtRaw = job_element.find("p", class_="fs13 fc_aux").text
    return publishedAtRaw == "Más de 30 días"


def getDataFromCard(job_element):
    id = job_element["data-id"]
    title = job_element.find("h1").find("a").text
    [company, location] = getCompanyLocation(job_element.find("p", class_="fs16 fc_base mt5 mb5"))
    publishedAt = parsePublicationDate(job_element.find("p", class_="fs13 fc_aux").text)
    detail = getJobDetail(id, title)

    return {
        "id": id,
        "title": title,
        "company": company,
        "location": location,
        "publishedAt": publishedAt.isoformat() + 'Z',
        "detail": detail
    }