URL = "https://pe.computrabajo.com/trabajo-de-civil"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
PAYLOAD={}

DETAIL_URL = "https://pe.computrabajo.com/offersgrid/getofferdetail"

KEYWORDS = {
    "for_students": ["estudiante", "alumno", "becario", "becaria", "becarios", "becarias", "practica", "práctica", "practicas", "prácticas", "practicante", "practicantes", "prácticante", "prácticantes"],
    "for_graduates": ["egresado", "titul", "bachiller"],
    "ad_honerem": ["ad honorem", "no remunerado", "sin remunerar", "sin remuneración", "sin remuneracion"],
}

DATA_PATH = "data.csv"
REVALIDATE_DATA_PATH = "revalidate_data.csv"