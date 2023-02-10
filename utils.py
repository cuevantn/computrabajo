def checkLastPage(text):
    return "¡Ups! Lo sentimos pero no hemos encontrado ofertas de trabajo para esta búsqueda." in text

def checkIsCivilEngineeringJob(text):
    civil = [
        "civil",
        "civiles",
    ]
    
    engineering = [
        "ingeniero",
        "ingeniera",
        "ingenieria",
        "ingeniería",
    ]

    isCivil = False
    isEngineering = False

    for word in civil:
        if word in text:
            isCivil = True
            break
    
    for word in engineering:
        if word in text:
            isEngineering = True
            break
    
    return isCivil and isEngineering
    
