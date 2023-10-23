import PyPDF2
from datetime import datetime
import pandas as pd
import os
import glob


# Pfad zum Ordner in dem das Skript liegt (wo auch die PDF Dateien liegen) --> hier wird auch die CSV Datei gespeichert --> kann auch ein anderer manuell gesetzter Ordner sein
folder_path = os.path.dirname(os.path.abspath(__file__))

# Pfad für CSV Datei
csv_path = os.path.join(os.path.normpath(folder_path), 'output.csv')

# Funktion um zu prüfen ob ein String ein Datum ist
def is_date(date_str):
    try:
        date = datetime.strptime(date_str, "%d.%m.%y")
    except ValueError:
        try:
            date = datetime.strptime(date_str, "%d.%m.%Y")
        except ValueError:
            return False
    
    return date.strftime("%d.%m.%Y")

# Funktion um zu prüfen ob ein String eine Betrag ist
def is_double(string):
    string = string.replace('.', '')
    try:
        float(string.replace(',', '.'))
    except ValueError:
        return False
    if not ',' in string:
        return False
    return True

# Funktion um CSV Datei zu schreiben
def write_csv(path, record:list, sortby:str, sep:str=";"):
    """
    record = [{'klsId':85854, 'kgs8': 1234}, {'klsId':3333, 'kgs8': 98766}, ...]
    """
    df = pd.DataFrame.from_records(record)
    #df.sort_values(by=[sortby], inplace=True, ascending=False)
    df.to_csv(path, index=False, header=True, sep=sep)

# Funktion um den Verwendungszweck zu bekommen
def get_usecase(line_num, lines):
    line = lines[line_num]
    text = ' '.join(line.split(' ')[1:-1])
    line = lines[line_num + 1]
    text += ' '.join(line.split(' ')[1:])
    check_max_lines = 5
    for i in range(check_max_lines):
        try:
            add_line = lines[line_num + 1 + i]
        except IndexError:
            break
        first_word = add_line.split(' ')[0]
        if not is_date(first_word):
            text += ' '.join(add_line.split(' ')[1:]) + ' '


    return text

def read_pdf(pdf_reader, records):
    # Verarbeitung der PDF Datei
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        lines = text.split('\n')
        for line_num in range(len(lines)):
            line = lines[line_num]
            first_word = line.split(' ')[0]
            last_word = line.split(' ')[-1]
            record = {}
            if is_date(first_word) and is_double(last_word):
                record['Datum'] = is_date(first_word)
                record['Betrag'] = last_word
                verwendungszweck = get_usecase(line_num, lines)
                record['Verwendungszweck'] = verwendungszweck
                records.append(record)

def main():

    records = []
    # suche alle PDF Dateien im Ordner
    os.chdir(folder_path)
    for pdf_path in glob.glob("*.pdf"):

        # PDF Datei öffnen
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        read_pdf(pdf_reader, records)

        # PDF Datei schließen
        pdf_file.close()
    
    # csv schreiben
    write_csv(csv_path, records, ';')

if __name__ == '__main__':
    main()