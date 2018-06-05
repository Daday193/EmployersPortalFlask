import os
import datetime

Arq = 0
diretorio = 'C:\\Users\\e000864\\PycharmProjects\\untitled\\venv\\EstudoFlask\\static\\042018'

for _, _, arquivo in os.walk(diretorio):

    try:
        while Arq <= len(arquivo):
            #print(arquivo[Arq])
            Arq += 1

    except Exception:
        print()
