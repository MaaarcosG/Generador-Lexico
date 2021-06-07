# Este es el scanner que se generara con las reglas establecidas por ./Inputs/Double.ATG

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from structure_tokens import State, Automata, Token, Handler
from utils import ecerradura_node, simulate_dfa_direct
from analysis import terminacion_compilador

class Production_Parse:
	def __init__(self, tokens):
		self.tokens = tokens
		self.counter_tokens = 0
		self.first_token = self.tokens[self.counter_tokens]
		self.last_token = ''

	def operation_tokens( self ):
		self.counter_tokens += 1
		if self.counter_tokens < len(self.tokens):
			self.first_token = self.tokens[self.counter_tokens]
			self.last_token = self.tokens[self.counter_tokens - 1]

	def expect(self, item, arg = None):
		counter_tokens = self.counter_tokens
		possible = False
		if item != None:
			try:
				if arg == None:
					ans = item()
				else:
					ans = item(arg)
				if type(ans) == bool:
					possible = ans
				else:
					possible = True
			except:
				possible = False
		self.counter_tokens = counter_tokens
		self.first_token = self.tokens[self.counter_tokens]
		self.last_token = self.tokens[self.counter_tokens - 1]
		return possible

	def read_token(self, item, type = False):
		if type:
			if self.first_token.type == item:
				self.operation_tokens()
				return True
			else:
				return False
		else:
			if self.first_token.value == item:
				self.operation_tokens()
				return True
			else:
				return False

	# Declaramos las variables int como globales para las operaiones
	value, result, value1, value2 = 0,0,0,0

	# COMIENZA LAS EVALUACIONES DE LAS PRODUCCIOENS
	def Expr(self):
		while self.expect(self.Stat,) :
			self.Stat()
			self.read_token(";")
		while self.expect(self.white,):
			self.read_token('white', True)
		while self.expect(self.read_token(".", False)):
			self.read_token(".")

	def Stat(self):
		value = self.Expression(value)
		print("Resultado: ", value)

	def Expression(self,result):
		value1 = self.Term(value1)
		while self.expect(self.read_token,"+") or self.expect(self.read_token,"-") :
			if self.expect(self.read_token,"+"	):
				self.read_token("+")
				re=self.Term(re)
				self.result2>()
				result1+=result2
	
			elif self.expect(self.read_token,"-"):
				self.read_token("-")
				re=self.Term(re)
				self.result2>()
				result1-=result2
		result=result1
		return result

	def Term(self,result):
		result1,result2=0,0
		result1=self.Factor(result1)
		while self.expect(self.read_token,"*") or self.expect(self.read_token,"/") :
			if self.expect(self.read_token,"*"	):
				self.read_token("*")
				re=self.Factor(re)
				self.result2>()
				result1*=result2
	
			elif self.expect(self.read_token,"/"):
				self.read_token("/")
				re=self.Factor(re)
				self.result2>()
				result1/=result2
		result=result1
		return result

	def Factor(self,result):
		sign=1
		if self.expect(self.read_token,'-'):
			self.read_token("-")
			sign = -1
			result=self.Number(result)
		if self.expect(self.Number, result):
			result = self.Number(result)
		elif self.expect(self.read_token,"("):
			self.read_token("(")
			result=self.Expression(result)
			self.read_token(")")
		
		result*=sign 

	def Number(self,ref, result):
		self.read_token('number', True)
		decnumber_result = float(last_token.value)
		return decnumber_result


def generate_transition_automata():
	automatas = []
	automata0 = Automata("nombre")
	temp_node= State(0)
	temp_transition = Handler('w', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('d', 2)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('0', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''
'', 4)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''
'', 4)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''	'', 4)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('+', 5)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('-', 5)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('/', 5)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(1)
	temp_transition = Handler('h', 6)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(2)
	temp_transition = Handler('o', 5)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(3)
	temp_node.accept = True
	temp_transition = Handler('0', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('.', 7)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(4)
	temp_node.accept = True
	temp_transition = Handler(''
'', 4)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''
'', 4)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''	'', 4)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(5)
	temp_node.accept = True
	automata0.states.append(temp_node)
	temp_node= State(6)
	temp_transition = Handler('i', 8)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(7)
	temp_transition = Handler('0', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 9)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(8)
	temp_transition = Handler('l', 10)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(9)
	temp_node.accept = True
	temp_transition = Handler('0', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 9)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 9)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	temp_node= State(10)
	temp_transition = Handler('e', 5)
	temp_node.transitions.append(temp_transition)
	automata0.states.append(temp_node)
	automatas.append(automata0)

	automata1 = Automata("while")
	temp_node= State(0)
	temp_transition = Handler('w', 1)
	temp_node.transitions.append(temp_transition)
	automata1.states.append(temp_node)
	temp_node= State(1)
	temp_transition = Handler('h', 2)
	temp_node.transitions.append(temp_transition)
	automata1.states.append(temp_node)
	temp_node= State(2)
	temp_transition = Handler('i', 3)
	temp_node.transitions.append(temp_transition)
	automata1.states.append(temp_node)
	temp_node= State(3)
	temp_transition = Handler('l', 4)
	temp_node.transitions.append(temp_transition)
	automata1.states.append(temp_node)
	temp_node= State(4)
	temp_transition = Handler('e', 5)
	temp_node.transitions.append(temp_transition)
	automata1.states.append(temp_node)
	temp_node= State(5)
	temp_node.accept = True
	automata1.states.append(temp_node)
	automatas.append(automata1)

	automata2 = Automata("do")
	temp_node= State(0)
	temp_transition = Handler('d', 1)
	temp_node.transitions.append(temp_transition)
	automata2.states.append(temp_node)
	temp_node= State(1)
	temp_transition = Handler('o', 2)
	temp_node.transitions.append(temp_transition)
	automata2.states.append(temp_node)
	temp_node= State(2)
	temp_node.accept = True
	automata2.states.append(temp_node)
	automatas.append(automata2)

	automata3 = Automata("number")
	temp_node= State(0)
	temp_transition = Handler('0', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 1)
	temp_node.transitions.append(temp_transition)
	automata3.states.append(temp_node)
	temp_node= State(1)
	temp_node.accept = True
	temp_transition = Handler('0', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 1)
	temp_node.transitions.append(temp_transition)
	automata3.states.append(temp_node)
	automatas.append(automata3)

	automata4 = Automata("decnumber")
	temp_node= State(0)
	temp_transition = Handler('0', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 1)
	temp_node.transitions.append(temp_transition)
	automata4.states.append(temp_node)
	temp_node= State(1)
	temp_transition = Handler('0', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('.', 2)
	temp_node.transitions.append(temp_transition)
	automata4.states.append(temp_node)
	temp_node= State(2)
	temp_transition = Handler('0', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 3)
	temp_node.transitions.append(temp_transition)
	automata4.states.append(temp_node)
	temp_node= State(3)
	temp_node.accept = True
	temp_transition = Handler('0', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('1', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('2', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('3', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('4', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('5', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('6', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('7', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('8', 3)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler('9', 3)
	temp_node.transitions.append(temp_transition)
	automata4.states.append(temp_node)
	automatas.append(automata4)

	automata5 = Automata("white")
	temp_node= State(0)
	temp_transition = Handler(''
'', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''
'', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''	'', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''	'', 1)
	temp_node.transitions.append(temp_transition)
	automata5.states.append(temp_node)
	temp_node= State(1)
	temp_node.accept = True
	temp_transition = Handler(''
'', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''
'', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''	'', 1)
	temp_node.transitions.append(temp_transition)
	temp_transition = Handler(''	'', 1)
	temp_node.transitions.append(temp_transition)
	automata5.states.append(temp_node)
	automatas.append(automata5)

	# lista para los tokens
	tokens = []

	# comienza la solicitud del archiv
	m_file = input('Ingrese el archivo a evaluar: ')
	prueba = open(m_file)
	data = prueba.read()
	prueba.close()
	i = 0
	last = 0
	while i < len(data):
		valid = terminacion_compilador(data, automata0, i)
		if valid:
			if last != 0 and (i - last > 0):
				while last < i:
					print(data[last], end='')
					last += 1
				print(': False')
			last += len(valid)
			aut = 1
			evaluate_token = Token('Token', valid)
			while aut<len(automatas):
				if (simulate_dfa_direct(automatas[aut], valid)):
					evaluate_token = Token(automatas[aut].id, valid)
					break
				aut += 1
			print('%s = %s' % (evaluate_token.type,evaluate_token.value))
			tokens.append(evaluate_token)
			i += len(valid)
		else:
				i+=1
	parser = Production_Parse(tokens)
# Operaciones realizadas despues del analisis
	parser.Expr()

if __name__ == "__main__":
   generate_transition_automata()