"""
DESCRIPCION DE LA PRUEBA TECNICA
Dado un horario en formato de 12 horas con AM o PM (ej: hh:mm:ssAM o hh:mm:ssPM),
escribe una función que convierta ese horario al formato de 24 horas (militar).
"""

def conversion_a_24_horas(s):
    periodo = s[-2:]
    hora, minuto, segundo = map(int, s[:-2].split(":"))


#Si es PM y la hora no son las 12, le sumamos 12 y sin las 12 es 0
#01:00:00PM - 01 + 12 ==> (13:00:00)
#08:15:00PM - 08 + 12 ==> (20:15:00)
#pero si es AM y 12 
#12:01:00AM - 12 = 0 ==> (00:01:00)

    if periodo == "AM":
        if hora == 12:
            hora = 0
    else:
        if hora != 12:
            hora += 12

    return f"{hora:02}:{minuto:02}:{segundo:02}"


#Entrada de los casos de prueba del caso 1 al caso 7
entradas = [
    "07:05:45PM",
    "12:01:00PM",
    "12:01:00AM",
    "01:00:00AM",
    "11:59:59PM",
    "04:30:00AM",
    "08:15:45PM"
]

for i, entrada in enumerate(entradas, start=1):
    print(f"CASO {i} = Entrada: {entrada} =====> Salida esperada: {conversion_a_24_horas(entrada)}")
