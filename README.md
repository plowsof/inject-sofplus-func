# inject-sofplus-func

The python script will parse an SoFplus '.func' script file and generate an 'sp_sc_func_load_cvar' friendly string.

A real version would use the python injector to send the lines to the client/server console, this just prints

mm_get_res.func is just an example func file.

This would be useful if you dont have write access to a server but you have the 'rcon' password, or you want to test a mod on your server without spending the time to upload the files.

The functions would be in memory and non-persistant (gone after a restart)
