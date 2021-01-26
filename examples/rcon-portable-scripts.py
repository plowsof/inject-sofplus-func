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
'''
**output**
b'rcon zero func_cvar\n'
b'rcon sp_sc_cvar_append func_cvar "function%20khokraad()%0a{%0a%20say%20%22hello%20wo"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=50 chunk=50
b'rcon sp_sc_cvar_append func_cvar "rld%22%0a%20set%20counter%200%0a%20sp_sc_func_exec"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=100 chunk=50
b'rcon sp_sc_cvar_append func_cvar "%20fahsuwif%0a}%0a%0a"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=150 chunk=50
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
b'rcon sp_sc_func_load_cvar func_cvar\n'
b'rcon zero func_cvar\n'
b'rcon sp_sc_cvar_append func_cvar "function%20fahsuwif()%0a{%0a%20sp_sc_flow_if%20num"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=50 chunk=50
b'rcon sp_sc_cvar_append func_cvar "ber%20cvar%20counter%20<=%20val%2099%0a%20{%0a%20%"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=100 chunk=50
b'rcon sp_sc_cvar_append func_cvar "20say%20%22bingobango%22%0a%20%20sp_sc_func_exec%2"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=150 chunk=50
b'rcon sp_sc_cvar_append func_cvar "0ebesaylv%20%24counter%0a%20%20sset%20~cmd%20sp_sc"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=200 chunk=50
b'rcon sp_sc_cvar_append func_cvar "_func_exec%20fahsuwif%0a%20%20sp_sc_timer%20500%20"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=250 chunk=50
b'rcon sp_sc_cvar_append func_cvar "%23~cmd%0a%20%20add%20counter%201%0a%20}%0a}%0a"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=300 chunk=50
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
b'rcon sp_sc_func_load_cvar func_cvar\n'
b'rcon zero func_cvar\n'
b'rcon sp_sc_cvar_append func_cvar "function%20ebesaylv(~int)%0a{%0a%20sp_sc_cvar_rand"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=50 chunk=50
b'rcon sp_sc_cvar_append func_cvar "om_int%20~test%20100000000000000000000%20888888888"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=100 chunk=50
b'rcon sp_sc_cvar_append func_cvar "888888888888%0a%20sp_sv_client_cvar_set%200%20%24~"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=150 chunk=50
b'rcon sp_sc_cvar_append func_cvar "int%20%24~test%0a}"\n'
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
curs=200 chunk=50
b'rcon sp_sc_cvar_unescape func_cvar func_cvar\n'
b'rcon sp_sc_func_load_cvar func_cvar\n'
exec the init
khokraad
b'rcon sp_sc_func_exec khokraad\n'
'''
