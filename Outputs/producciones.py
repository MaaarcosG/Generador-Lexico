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
				# si es booleano
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

	# COMIENZA LAS EVALUACIONES DE LAS PRODUCCIOENS
	# funcion Expr
	def Expr(self):
		while self.expect(self.Stat()):
			self.Stat()
			self.read_token(";")
		self.read_token(".")

	# funcion Stat
	def Stat(self):
		value = 0
		value=self.Expression(value)
		print(str(value))

	# funcion Expression
	def Expression(self,result):
		result1, result2 = 0, 0
		result1=self.Term(result1)
		while self.expect(self.read_token("+")) or self.expect(self.read_token("-")):
			if self.expect(self.read_token("+")):	
				self.read_token("+")
				result2=self.Term(result2)
				result1+=result2
	
			elif self.expect(self.read_token("-")):
				self.read_token("-")
				result2=self.Term(result2)
				result1-=result2
		result=result1
		return result

	# funcion Term
	def Term(self,result):
		result1, result2 =  0,0
		result1=self.Factor(result1)
		while self.expect(self.read_token("*")) or self.expect(self.read_token("/")):
			if self.expect(self.read_token("*")):	
				self.read_token("*")
				result2=self.Factor(result2)
				result1*=result2
	
			elif self.expect(self.read_token("/")):
				self.read_token("/")
				result2=self.Factor(result2)
				result1/=result2
		result=result1
		return result

	# funcion Factor
	def Factor(self,result):
		signo=1
		if self.expect(self.read_token('-')):
			self.read_token("-")
			signo = -1
		if self.expect(self.Number(result)):
			result=self.Number(result)
			
		elif self.expect(self.read_token("(")):
			self.read_token("(")
			result=self.Expression(result)
			self.read_token(")")
		result*=signo
		return result

	# funcion Number
	def Number(self,result):
		self.read_token('number', True)
		result = int(self.last_token.value)
		return result

