# file to create another file

from os import write


def create_file_compiler(dfa, extras, parser, name = "nani"):
    print("Haciendo archivo ", name)
    i = 0
    output = open("./outputs/" + name + ".py", "w+", encoding="utf-8")
    output.write('# Este es el scanner que se generara con las reglas establecidas por ./Inputs/%s.ATG\n\n' % name)

    output.write('import os\n')
    output.write('import sys\n')
    output.write('sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))\n')
    output.write('from DFA_Direct.dfa_direct import ecerradura_node, simulate_dfa_direct\n')
    output.write('from utils import read_str\n')
    output.write('from analysis import terminacion_compilador\n')
    output.write("import collections\n")
    output.write("EPSILON = 'ε'\n\n")

    output.write(parser)

    output.write("class Token:\n")
    output.write("\tdef __init__(self, type, value):\n")
    output.write("\t\tself.type = type\n")
    output.write("\t\tself.value = value\n\n")
    
    output.write("# ESTA EN BASE AL ARCHIVO DFA_Direct structure\n")
    output.write("class Automata:\n")
    output.write("\tdef __init__(self, exp):\n\t\tself.id = exp \n\t\tself.states = []\n\n")
    output.write("class State: \n")
    output.write("\tdef __init__(self,num):\n\t\tself.id = num\n\t\tself.transitions = []\n\t\tself.accept = False \n\n")
    output.write("class Handler: \n")
    output.write("\tdef __init__(self,sym,id):\n\t\tself.symbol = sym\n\t\tself.id = id\n\n")

    output.write("def generate_transition_automata():\n")
    
    output.write("\tautomatas = []\n")
    creando_automatas(dfa, i, output)
    # sumamos uno al contador
    i += 1
    for automata in extras:
        creando_automatas(extras[automata], i, output, automata)
        i += 1
    output.write("\t# lista para los tokens\n")
    output.write("\ttokens = []\n\n")
    output.write("\t# comienza la solicitud del archiv\n")
    output.write("\tm_file = input('Ingrese el archivo a evaluar: ')\n")
    output.write("\tprueba = open(m_file)\n")
    output.write("\tdata = prueba.read()\n")
    output.write("\tprueba.close()\n")
    
    output.write("\ti = 0\n")
    output.write("\tlast = 0\n")
    output.write("\twhile i < len(data):\n")
    output.write("\t\tvalid = terminacion_compilador(data, automata0, i)\n")
    output.write("\t\tif valid:\n")
    output.write("\t\t\tif last != 0 and (i - last > 0):\n")
    output.write("\t\t\t\twhile last < i:\n")
    output.write("\t\t\t\t\tprint(data[last], end='')\n")
    output.write("\t\t\t\t\tlast += 1\n")
    output.write("\t\t\t\tprint(': False')\n")
    output.write("\t\t\tlast += len(valid)\n")
    output.write("\t\t\taut = 1\n")
    output.write("\t\t\tnew_token = Token('Token', valid)\n")
    output.write("\t\t\twhile aut<len(automatas):\n")
    output.write("\t\t\t\tif (simulate_dfa_direct(automatas[aut], valid)):\n")
    output.write("\t\t\t\t\tnew_token = Token(automatas[aut].id, valid)\n")
    output.write("\t\t\t\t\tbreak\n")
    output.write('\t\t\t\taut += 1\n')
    output.write("\t\t\tprint('%s = %s' % (new_token.type,new_token.value))\n")
    output.write("\t\t\ttokens.append(new_token)\n")
    output.write("\t\t\ti += len(valid)\n")
    output.write("\t\telse:\n")
    output.write("\t\t\t\ti+=1\n")
    output.write("\tparser = Production_Parse(tokens)\n")
    output.write("\tparser.Expr()\n\n")
    output.write('if __name__ == "__main__":\n'+'   generate_transition_automata()')

    output.close()

# funcion para ir escribiendo las transcciones conforme a lo indicado
def creando_automatas(automata, i, file, name='nombre'):
    file.write("\tautomata"+str(i)+' = Automata("'+ name +'")\n')
    for node in automata.state:
        file.write("\ttemp_node= State("+ str(node.id) + ")\n")
        if node.accept:
            file.write("\ttemp_node.accept = True\n")
        for transition in node.transition:
            file.write("\ttemp_transition = Handler('" +transition.symbol+"', "+str(transition.id) +")\n")
            file.write("\ttemp_node.transitions.append(temp_transition)\n")
        file.write("\tautomata"+str(i)+".states.append(temp_node)\n")
    file.write("\tautomatas.append(automata"+str(i)+")\n")
    file.write("\n")