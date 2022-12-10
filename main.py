"""
Progetto: Ordinatore di cartelle
Data inizio: 11/12/22
Data completamento prima versione: 11/12/22
Descrizione: Script che ordina i file della directory Scaricati in sotto cartelle in base al tipo di file
note: funzionante solo per Linux e per l'user cloudy
migliorie: interfaccia grafica, versatilita linux mac windows, non dipendente da un user, tradurre tutto in inglese
librerie usate: os, shutil(solo metodo move)
|-------------------------------------------------------------------------------------------------------------------|
"""

# librerie necessarie al funzionamento
import os
from shutil import move


# definisco path delle cartella Scaricati e una lista di tutte le cartelle che mi servono
path_cartella_scaricati = '/home/cloudy/Scaricati/'
lista_path = []
for path in ['immagini', 'video', 'zip', 'iso', 'programmi',  'file_testo', 'audio', 'web', 'altro']:
    lista_path.append(path_cartella_scaricati + path)


# controlliamo se le cartelle esistono se no le creiamo
for directorty in lista_path:
    if os.path.isdir(directorty):
        print(f'la cartella "{directorty}" esiste')
    else:
        print(f'{directorty} non esiste, creo la cartella')
        os.makedirs(directorty)


# creazione filtro dei file
file_immagini = ['.png', '.jpg', '.jpeg', '.svg']
file_video = ['.mp4', '.html5']
file_zip = ['.gz', '.tar', '.zip', '.deb', '.rar']
file_iso = ['.iso']
file_programmi = ['.exe']
file_testuali = ['.txt', '.odt', '.latex']
file_audio = ['.mp3', '.pcm']
file_web = ['.html']


# smistamento file
for file in os.listdir(path_cartella_scaricati):
    file = path_cartella_scaricati + file
    if os.path.isfile(file):
        if any(extension in file for extension in file_immagini):
            move(file, lista_path[0])
        elif any(extension in file for extension in file_video):
            move(file, lista_path[1])
        elif any(extension in file for extension in file_zip):
            move(file, lista_path[2])
        elif any(extension in file for extension in file_iso):
            move(file, lista_path[3])
        elif any(extension in file for extension in file_programmi):
            move(file, lista_path[4])
        elif any(extension in file for extension in file_testuali):
            move(file, lista_path[5])
        elif any(extension in file for extension in file_audio):
            move(file, lista_path[6])
        elif any(extension in file for extension in file_web):
            move(file, lista_path[7])
        else:
            move(file, lista_path[8])
