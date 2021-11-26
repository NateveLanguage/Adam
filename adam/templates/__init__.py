import importlib as imp

from adam.utils import tolist, tokenize

class Template():
	def __init__(self, name = "english"):
		self.template_name = name
		
		# from adam.templates.{template} import *
		module_name = "adam.templates." + self.template_name
		template = imp.import_module(module_name)

		self.alphabet = template.alphabet
		self.digits = template.digits
		self.alphanum = template.alphanum
		self.blanks = template.blanks
		self.strings = template.strings
		self.matrices = template.matrices
		self.vectors = template.vectors
		self.embedded = template.embedded
		self.commentaries = template.commentaries
		self.floating = template.floating
		
		self.identifier = template.identifier

		special_functions = template.special_functions.replace(4 * " ", "\t") # Indent with tabs
		self.special_functions = special_functions

		self.USE = template.USE
		self.WAIT = template.WAIT
		self.INCLUDE = template.INCLUDE
		
		preprocess = [template.USE, template.WAIT, template.INCLUDE]
		process = [template.IMPORT, template.FROM, template.AS, template.PASS, template.IN]
		conditionals = [template.IF, template.ELIF, template.ELSE, template.TRY, template.EXCEPT, template.WITH]
		loops = [template.WHILE, template.FOR, template.BREAK, template.CONTINUE]
		functions = [template.OPERATOR, template.RETURN]
		classes = [template.CLASS, template.SELF]
		bools = [template.AND, template.OR, template.NOT, template.TRUE, template.FALSE]

		self.primitives = [template.FLOAT, template.INT, template.COMPLEX, template.MATRIX, template.VECTOR, template.STRING, template.NULL]
		std_funcs = preprocess + process + conditionals + loops + functions + classes + bools
		self.operators = tolist(template.one_char_symbols) + template.two_char_symbols

		self.protected = self.primitives + std_funcs + self.operators

		self.protected_tokens = tokenize(self.protected)
		self.protected_IDs = list(range(len(self.protected)))

		self.codes = [template.identifier, template.eof]

		self.ALL = self.primitives + self.codes + self.protected_IDs
