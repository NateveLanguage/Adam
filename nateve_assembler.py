try:
	from eggdriver import *
	import sys, os, subprocess
except ImportError:
	print('ImportError')


def ninput(prompt = '', default = ''):
	return float(input(prompt, default))

def binput(prompt = '', default = ''):
	return bool(input(prompt, default))

def update_std():
	subprocess.call([sys.executable, '-m', 'pip', 'install', 'eggdriver'])

def include(file_name = ''):
	file = file_name.split('.')[0]
	subprocess.call([sys.executable, '-m', 'adam', 'build', file])


def recibe_numero(prompt = '', default = ''):
	return float(input(prompt, default))

def recibe_booleano(prompt = '', default = ''):
	return bool(input(prompt, default))

def actualiza_std():
	subprocess.call(["py", "-m", "pip", "install", "eggdriver"])

imprime = print
recibe = input
Matriz = Matrix

deriva = derive
sen = sin
serie_sen = sin_serie
serie_cos = cos_serie

	def root():print("a")
	imprime("Hola")

