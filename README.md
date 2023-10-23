# ING_DiBa PDF Kontoauszug zu CSV

## Überblick

Dieses Python-Skript dient zum Einlesen von mehreren Kontoauszügen eines ING_DiBa Girokontos im PDF-Format. 
Es extrahiert die relevanten Informationen wie Datum, Betrag und Verwendungszweck und exportiert diese in eine CSV-Datei.

## Voraussetzungen

- Python 3.x
- PyPDF2
- pandas
- datetime

### Installation der Abhängigkeiten

Installieren Sie die benötigten Python-Bibliotheken mit pip:

```bash
pip install PyPDF2 pandas
```

## Verwendung
Das Skript sollte im gleichen Ordner wie die PDF-Kontoauszüge liegen. Alternativ können Sie den Ordnerpfad im Skript manuell setzen.

## Funktionsweise
Das Skript durchläuft die folgenden Schritte:

1. Sucht alle PDF-Dateien im festgelegten Ordner.
2. Öffnet jede PDF-Datei und liest sie Seite für Seite.
3. Extrahiert das Datum, den Betrag und den Verwendungszweck jeder Transaktion.
4. Speichert die gesammelten Daten in einer CSV-Datei.

## Lizenz
Dieses Projekt steht unter der MIT-Lizenz.
