import sys

recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]

#agrego empezar el año
empezar_año = ['2021-02-02', "06:00", "Empezar el Año”"]
recordatorios.insert(1, empezar_año) 

#edito fecha
recordatorios.insert(3, ['2021-07-16', "13:00", "No hacer nada es feriado"])

del recordatorios[4]

#remover el dia del trabajo

del recordatorios[2]

#agregar navidad y año nuevo a las 22:00

navidad = ['2021-12-25', "22:00", "Cena de Navidad"]
recordatorios.insert(4, navidad) #se puede agregar texto,etc

año_nuevo = ['2021-12-31', "22:00", "Cena de Año Nuevo"]
recordatorios.insert(7, año_nuevo) #se puede agregar texto,etc

print(recordatorios)





