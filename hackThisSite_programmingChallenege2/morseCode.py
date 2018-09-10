
class Morse():
	def __init__(self):
		print("MorseObject Created")

	#morse hardcoded values
		a = ('.', '-')
		b = ('-','.','.', '.')
		c = ('-', '.', '-', '.')
		d = ('-', '.', '.')
		e = ('.')
		f = ('.','.','-','.')
		g = ('-','-','.')
		h = ('.', '.', '.', '.')
		i = ('.', '.')
		j = ('.', '-', '-', '-')
		k = ('-', '.', '-')
		l = ('.','-','.','.')
		m = ('-', '-')
		n = ('-', '.')
		o = ('-', '-', '-')
		p = ('.', '-', '-', '.')
		q = ('-', '-', '.', '-')
		r = ('.', '-', '.')
		s = ('.', '.', '.')
		t = ('-')
		u = ('.', '.', '-')
		v = ('.', '.', '.', '-')
		w = ('.', '-', '-')
		x = ('-', '.', '.', '-')
		y = ('-', '.', '-', '-')
		z = ('-', '-', '.', '.')

		m1 = ('.', '-', '-', '-', '-')
		m2 = ('.', '.', '-', '-', '-')
		m3 = ('.', '.', '.', '-', '-')
		m4 = ('.', '.', '.', '.', '-')
		m5 = ('.', '.', '.', '.', '.')
		m6 = ('-', '.', '.', '.', '.')
		m7 = ('-', '-', '.', '.', '.')
		m8 = ('-', '-', '-', '.', '.')
		m9 = ('-', '-', '-', '-', '.')
		m0 = ('-', '-', '-', '-', '-')
		
		#dictionary for hopefully faster translations
		self.morse = {m1:'1',m2:'2',m3:'3',m4:'4',m5:'5',m6:'6',m7:'7',m8:'8',m9:'9',m0:'0', a:'a',b:'b',c:'c',d:'d',e:'e',f:'f',g:'g',h:'h',i:'i',j:'j',k:'k',l:'l',m:'m',n:'n',o:'o',p:'p',q:'q',r:'r',s:'s',t:'t',u:'u',v:'v',w:'w',x:'x',y:'y',z:'z'}

		
	#prints the disctionary values
	def printAlphanumeric(self):
		print(self.morse)

	#translates a single letter by taking in a list representing morse code
	#returns a char
	def translate(self, letterInCode):

		return self.morse[tuple(letterInCode)]
		
	#translates a whole string of morse code
	#returns a list of translated character back
	def translateBrokenString(self, string):
		code = []
		translation = []
		for char in string:
			if char != ' ':
				code.append(char)
			else:
				translation.append(self.translate(code))
				code = []
		return translation