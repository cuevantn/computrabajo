from utils import checkIsTraineeJob

title = "Modelador Bim"
text = """
Contrato por Obra Determinada o Servicio Específico Tiempo completo
Al unirte a un equipo de más de 4000 personas trabajando en Chile y Perú, serás parte de una red ágil de profesionales con talento y grandes aspiraciones. Contamos contigo para sumarte a nuestra cultura donde la flexibilidad nos diferencia, el trabajo en equipo nos potencia, la pasión nos mueve al éxito y la integridad nos guía. ¡Únete al Grupo Flesan y forma parte de un ambiente laboral con empowerment y oportunidades de crecimiento!

RESPONSABILIDADES:

- Producir modelos que cumplan con los lineamientos y Planes de Ejecución BIM de los proyectos.

- Realizar el control de Calidad del modelo según los lineamientos BIM.

- Desarrollar presentaciones 4D en coordinación con el equipo de planificación del proyecto, con el fin de apoyar a las licitaciones.

- Presentar los modelos (3D) para facilitar la visualización, mediante imágenes y recorridos virtuales realizando

especificaciones técnicas.

- Revisar los planos y especificaciones técnicas para asegurar que los modelos se encuentren actualizados conforme al proyecto solicitado.

REQUISITOS:

- Estudiante Técnico o Universitario de las carreras: Ingeniería Civil, Arquitectura, Ingeniería Mecánico, Ing. Eléctrica,

Ingeniería Sanitaria y/o Construcción Civil o afines.

- Experiencia de 06 meses en construcción civil, manejando Revit.

- Conocimiento en Navisworks (Básico), Revit (Intermedio).

BENEFICIOS:

- Sueldo acorde al mercado en planilla

- EPS (Opcional)+Seguro Oncológico

- Convenios corporativos

- Oportunidad de crecimiento y desarrollo

“Esta oferta laboral se rige bajo la Ley Nº 29973 que incentiva la inclusión de personas con discapacidad al mundo laboral.
Requerimientos

Educación mínima: Técnico
Menos de 1 año de experiencia
Edad: entre 22 y 37 años
Disponibilidad de viajar: No
Disponibilidad de cambio de residencia: No
"""

isTrainee = checkIsTraineeJob(title.lower(), text.lower())
print(isTrainee)