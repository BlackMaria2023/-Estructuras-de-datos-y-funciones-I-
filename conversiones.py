import sys

tasa_sol = float(sys.argv[1])
tasa_arg = float(sys.argv[2])
tasa_dolar = float(sys.argv[3])
pesos = int(sys.argv[4])

tasas = {
    "Sol" : tasa_sol,
    "Peso_arg": tasa_arg,
    "Dolar" : tasa_dolar
}

print(f"Los {pesos} equivalen a: ")
print(f" {tasas ['Sol'] * pesos} Soles")
print(f" {tasas ['Peso_arg'] * pesos} Pesos Argentinos")
print(f" {tasas ['Dolar'] * pesos} Dólares")