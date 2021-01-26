def func_parse(func_loc,func_name):
	with open(func_loc, 'r') as f:
		lines = f.readlines()

	funclist = {}
	obfuscate = {}
	cvar = ""
	counter = 0
	funcOpen = 0
	for x in lines:
		if x[0:8] == "function":
			if funcOpen == 0:
				funcOpen = 1
				cvar = x	
			else:
				funclist[counter] = str(cvar)
				counter += 1
				cvar = x
			part = x.split("(")
			part2 = part[0].split()
			func = part2[1]
			rand = get_random_string(8)
			obfuscate[func] = rand
		else:
			cvar += x
	funclist[counter] = str(cvar)
	for x in funclist:
		cvar = funclist[x]
		cvar = cvar.replace("\n", r"%0a")
		cvar = cvar.replace("\"", "%22")
		cvar = cvar.replace("\t", " ")
		cvar = cvar.replace(" ","%20")
		cvar = cvar.replace("$","%24")
		cvar = cvar.replace("#","%23")
		cvar = cvar.replace("/",r"%2F")
		
		for z in obfuscate:
			cvar = cvar.replace(z,obfuscate[z])
		funclist[x] = cvar
		'''
	with open("injectme.txt", "w+") as f:
		for i in funclist:
			f.write(funclist[i] + "\n"
			'''
	func_name = obfuscate[str(func_name.replace(".func","_init"))]
	print(func_name)
	func_load(funclist,func_name)

def fdelay():
	time.sleep(0.3)
def func_load(funclist,func_name):
	global cbuf_addText
	global COM_Printf
	init_func = func_name
	#This example just prints
	#The real version would enter these lines into the clients console using the python injector
	for x in funclist:
		cursor = 0
		chunk=50
		end = chunk
		myAddTextWrapper("rcon zero func_cvar\n")
		fdelay()
		while cursor < len(funclist[x]):
			myAddTextWrapper("rcon sp_sc_cvar_append func_cvar \"%s\"\n" % funclist[x][cursor:end])
			fdelay()
			myAddTextWrapper("rcon sp_sc_cvar_unescape func_cvar func_cvar\n")
			fdelay()
			cursor+=chunk
			end+=chunk
			print("curs="+str(cursor)+" chunk="+str(chunk))
			fdelay()
		myAddTextWrapper("rcon sp_sc_cvar_unescape func_cvar func_cvar\n")
		fdelay()
		myAddTextWrapper("rcon sp_sc_func_load_cvar func_cvar\n")
		fdelay()
	print("exec the init")
	print(init_func)
	myAddTextWrapper("rcon sp_sc_func_exec %s\n" % init_func)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def myAddTextWrapper(input):
	global cbuf_addText
	print(input.encode('latin-1'))
	cbuf_addText(input.encode('latin-1'))
def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
