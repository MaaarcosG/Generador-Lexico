from parser_decom import parser
from read_compiler import read_file
from analysis import analyze
from create_file import create_file_compiler

archivo = input('Ingrese el nombre del archivo: ')
file_open = open(archivo)
informacion = file_open.read()
file_open.close()

data, character, keywords, tokens, productions = read_file(informacion)
automata_dfa, dfa_more, data_parse = analyze(data, character, keywords, tokens, productions)
create_file_compiler(automata_dfa, dfa_more, data_parse, data)