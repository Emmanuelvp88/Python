
import matplotlib.pyplot as plt

datos = []

with open("Historial.txt", 'r') as file:
    for linea in file:
        if linea.startswith("From "):
            elementos = linea.split()
            correo = elementos[1]
            dia = elementos[2]
            mes = elementos[3]
            hora = elementos[4]
            año = elementos[5]

            diccionario = {
                "correo": correo,
                "dia": dia,
                "mes": mes,
                "hora": hora,
                "año": año
            }

            datos.append(diccionario)

conteo_dias = {}
total_de_correos = 0
total_num_de_dias = 0
lista_ejex = {}

dias_completos = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for diccionario in datos:
    dia = diccionario["dia"]
    conteo_dias[dia] = conteo_dias.get(dia, 0) + 1

for valor in dias_completos:
    if valor not in conteo_dias:
        conteo_dias[valor] = 0

dias_de_correos_enviados = list(conteo_dias.keys())
valor_de_correos_enviados = list(conteo_dias.values())
for suma in valor_de_correos_enviados:
    total_de_correos = int(total_de_correos + suma)
for d, v in conteo_dias.items():
    lista_ejex[d, v] = round((v * 100) / total_de_correos)

plt.figure()
pos = list(range(len(dias_de_correos_enviados)))
bars = plt.bar(pos, lista_ejex.values(), align="center", linewidth=0, color="purple")
bars[1].set_color("red")
plt.xticks(pos, dias_de_correos_enviados, alpha=0.8)
plt.tick_params(top="off", bottom="off", left="off", right="off", labelleft="off", labelbottom="on")
plt.title("Porcentaje de correos enviados por día", alpha=0.6)
for spine in plt.gca().spines.values():
    spine.set_visible(False)
for bar in bars:
    plt.gca().text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(int(bar.get_height())) + "%", ha="center",
                   color="black", va="bottom", fontsize=12)

    plt.show()
