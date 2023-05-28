with open("Historial.txt") as archivo:
    for i in archivo:
        if i.startswith("From "):
            print(i.rstrip())
archivos = []
dir(archivos)
