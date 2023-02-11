import re
import datetime
from constants import SPANISH_MONTS

def checkLastPage(text):
    return "¡Ups! Lo sentimos pero no hemos encontrado ofertas de trabajo para esta búsqueda." in text

def checkIsCivilEngineeringJob(title_lower,text_lower):
    civil = [
        "civil",
        "civiles",
    ]
    
    engineering = [
        "ing."
        "ingeniero",
        "ingeniera",
        "ingenieria",
        "ingeniería",
    ]

    isCivil = False
    isEngineering = False

    for word in civil:
        if word in text_lower:
            isCivil = True
            break
        if word in title_lower:
            isCivil = True
            break
    
    for word in engineering:
        if word in text_lower:
            isEngineering = True
            break
        if word in title_lower:
            isEngineering = True
            break
    
    return isCivil and isEngineering

def checkIsTraineeJob(title_lower, text_lower):
    trainee = [
        "pre-profesional",
        "pre profesional",
        "sin experiencia",
        "c/s experiencia",
        "preprofesional",
        "s experiencia",
        "pre-práctica",
        "pre práctica",
        "prepráctica",
        "estudiante",
        "pasantia",
        "pasantía",
        "práctica",
        "practica",
        "trainee",
        "pasante",
        "becario",
        "becaria",
        "alumno",
        "alumna",
        "ultimo",
        "último",
        "ciclo",
    ]
    
    for word in trainee:
        if word in text_lower:
            return True
        if word in title_lower:
            return True

    return False

def checkIsAdHonoremJob(title_lower,text_lower):
    ad_honorem = [
        "ad honorem",
        "ad-honorem",
        "sin remuneración",
        "sin remuneracion",
        "sin pago",
        "no remunerado",
        "no remunerada",
    ]
    
    for word in ad_honorem:
        if word in text_lower:
            return True
        if word in title_lower:
            return True
    
    return False


def remove_before_regex(text, keyword_regex, start_from="end"):
    if start_from == "end":
        result = re.sub(rf"(.*{keyword_regex}.*?)[\r\n]+.*$", r'\1', text, flags=re.DOTALL|re.MULTILINE)
    else:
        result = re.sub(rf"^.*?(?={keyword_regex})", '', text, flags=re.DOTALL|re.MULTILINE)
    return result

def parsePublicationDate(text):
    current_date = datetime.datetime.now()
    hours = 0
    if text == "Ayer":
        hours = 24

    elif "Hace" in text:
        try:
            minutes = int(re.sub(r"Hace (\d+) minuto[s]?", r"\1", text))
            return current_date - datetime.timedelta(minutes=minutes)

        except:
            try:
                hours = int(re.sub(r"Hace (\d+) hora[s]?", r"\1", text))
                return current_date - datetime.timedelta(hours=hours)
            
            except:
                try:
                    days = int(re.sub(r"Hace (\d+) día[s]?", r"\1", text))
                    return current_date - datetime.timedelta(days=days)
                except:
                    print(text)
                    print("Incorrect date format")
                    return None

    else:
        try:
            # Split the date string into day and month
            day, month_string = text.split(" de ")
            day = int(day)
            month = SPANISH_MONTS[month_string.lower()]

            # Create a datetime object using the year, month, and day
            date_object = datetime.datetime(year=datetime.datetime.now().year, month=month, day=day)
            return date_object
        except (ValueError, KeyError):
            print(text)
            print("Incorrect date format")
            return None

    #get the current date

    #subtract the number of hours
    date = current_date - datetime.timedelta(hours=hours)

    #return the date
    return date