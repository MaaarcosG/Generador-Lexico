# Este es el scanner que se generara con las reglas establecidas por ./Inputs/MyCOCOR.ATG
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import character_read
from scanner import scanner_data

# Obtenemos los keywords
keywords = []

ANY = [chr(x) for x in range(0, 256)]

# characters disponibles
letter= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letter = character_read(letter)

digit= "0123456789"
digit = character_read(digit)

cr = chr(13)
cr  = character_read(cr)

lf = chr(10)
lf  = character_read(lf)

tab = chr(9)
tab  = character_read(tab)

ignore = cr+lf+tab
ignore  = character_read(ignore)

comillas = chr(34)
comillas  = character_read(comillas)

stringletter = ''.join(set(set(ANY)-set(comillas)-set(ignore)))
stringletter  = character_read(stringletter)

operadores ="+-=()[]{}|.<>"
operadores  = character_read(operadores)

MyANY = ''.join(set(ANY)-set(operadores))
MyANY  = character_read(MyANY)

# Aqui se obtenemos cada uno de los tokens permitidos
ident = letter+" (("+letter+"|"+digit+")*)"
string = "(("+comillas+")*) "+stringletter+" (("+stringletter+")*) "+comillas
char = '+" ((" +/ +")*) "+letter+'
charnumber = "CHR"+" (" +digit+" (("+digit+")*) " +")"
charinterval = "CHR"+" (" +digit+" (("+digit+")*) " +")" +". "". " +"CHR"+" (" +digit+" (("+digit+")*) " +")"
nontoken = MyANY
startcode = " ("+". "
endcode = ". "+")"

# Nombres de las variables
names_automatas_keywords = ['ident']
names_automatas = ['string', 'char', 'charnumber', 'charinterval', 'nontoken', 'startcode', 'endcode=+".']

# Si existe EXCEPT WORDS se agrega a esta lista
data_automata_keywords = [ident]
automata = [string,char,charnumber,charinterval,nontoken,startcode,endcode]
data_characters = [ chr(13), chr(10), chr(9), chr(34)]

# Se scannea lo generado
if __name__ == '__main__':
	scanner_data(keywords, automata, data_automata_keywords, data_characters, names_automatas_keywords, names_automatas)
