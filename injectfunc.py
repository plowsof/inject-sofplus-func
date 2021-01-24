import os

func_name = "mm_get_res.func"
func_loc = os.path.join('.','mm_get_res.func')

def main():
	global func_loc
	with open(func_loc, 'r') as f:
		lines = f.readlines()

	funclist = {}
	cvar = ""
	counter = 0
	funcOpen = 0
	for x in lines:
		x = x.replace("\n", "%0a")
		x = x.replace("\"", "%22")
		x = x.replace("\t", " ")
		if x[0:8] == "function":
			if funcOpen == 0:
				funcOpen = 1
				cvar = x	
			else:
				funclist[counter] = ("\"" + str(cvar) + "\"")
				counter += 1
				cvar = x
		else:
			cvar += x
	funclist[counter] = ("\"" + str(cvar) + "\"")
	'''
	with open("injectme.txt", "w+") as f:
		for i in funclist:
			f.write(funclist[i] + "\n")
	'''
	func_load(funclist)

def func_load(funclist):
	global func_name
	init_func = func_name.replace(".func","_init")
	#This example just prints
	#The real version would enter these lines into the clients console using the python injector
	for x in funclist:
		print(";set func_cvar %s;" % funclist[x])
		print(";~;")
		print(";sp_sc_cvar_unescape func_cvar func_cvar;")
		print(";~;")
		print(";sp_sc_func_load_cvar func_cvar;")
		print(";~;")
	print(";sp_sc_func_exec %s;" % init_func)

if __name__ == '__main__':
	main()