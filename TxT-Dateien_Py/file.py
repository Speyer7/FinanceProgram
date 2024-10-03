def speichern_liste(dateiname, liste):
    with open(dateiname, 'w') as file:
        for element in liste:
            file.write(f"{element}\n")

def laden_liste(dateiname):
    liste = []
    try:
        with open(dateiname, 'r') as file:
            liste = [zeile.strip() for zeile in file]
    except FileNotFoundError:
        print(f"Die Datei {dateiname} wurde nicht gefunden und wird neu erstellt.")
    return liste

def hinzufuegen_element(dateiname, element):
    liste = laden_liste(dateiname)
    liste.append(element)
    speichern_liste(dateiname, liste)

def entfernen_element(dateiname, element):
    liste = laden_liste(dateiname)
    try:
        liste.remove(element)
        speichern_liste(dateiname, liste)
    except ValueError:
        print(f"Das Element {element} ist nicht in der Liste.")

# Beispiel für die Verwendung der Funktionen
meine_liste_datei = 'meine_liste.txt'
meine_liste = laden_liste(meine_liste_datei)  # Lädt die Liste oder erstellt eine neue, wenn sie nicht existiert
print("Aktuelle Liste:", meine_liste)

# Element hinzufügen
#hinzufuegen_element(meine_liste_datei, 'hey')
#print("Liste nach dem Hinzufügen eines Elements:", laden_liste(meine_liste_datei))

# Element entfernen
entfernen_element(meine_liste_datei, 'hey')
print("Liste nach dem Entfernen eines Elements:", laden_liste(meine_liste_datei))