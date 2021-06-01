# Este es el scanner que se generara con las reglas establecidas por ./Inputs/Ejemplo.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = ['if', 'while']

# characters disponibles
letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter  = character_read(letter)

digit = "0123456789"
digit  = character_read(digit)

hexdigit = digit+"ABCDEF"
hexdigit  = character_read(hexdigit)

# Aqui se obtenemos cada uno de los tokens permitidos
ids = letter+" (("+letter+")*)"
number = digit+" (("+digit+")*)"
hexnumber = hexdigit+" (("+hexdigit+")*) " +"H"

# Nombres de las variables
names_automatas_keywords = ['ids']
names_automatas = ['number', 'hexnumber']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = [ids]
automata = [number,hexnumber]
data_characters = []

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)