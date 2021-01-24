# inject-sofplus-func

The python script will parse an SoFplus '.func' script file and generate an 'sp_sc_func_load_cvar' friendly string. After loading all the functions <filename>_init will be called (assuming you have a valid func file) to begin the script

A real version would use the python injector to send the lines to the client/server console, this just prints  

mm_get_res.func is just an example func file.  

This would be useful if you dont have write access to a server but you have the 'rcon' password, or you want to test a mod on your server without spending the time to upload the files. But for now this is mainly client side only (e,g, packets sent to server might be too big, or lost so that'd need to be acounted for)

The functions would be in memory and non-persistant (gone after a restart)

**Ideas for problems**
__cvar length too big__ - creating aliases for every sofplus command sequentially , and making sure to use cmall cvar names in your sripts  
__Packets lost__ - a callback function that returns the length of a cvar we're trying to create:  

untested alias method~  

Original function:  
function inject_callback(~slot,~cvar)  
{  
  sp_sc_cvar_len ~len $~cvar  
  sp_sv_client_cvar_set $~slot 6 $~len  
}  
  
would look something like this: (just my theory)
alias f function    
alias l sp_sc_cvar_len  
alias s sp_sv_client_cvar_set
sp_sc_alias a "sp_sc_cvar_append ${@}"  

a b #f " i(~s,c)%0a{%0a" #l " ~l $~c%0a" #s " $~s 6 $~l%0a}" 
  
  
