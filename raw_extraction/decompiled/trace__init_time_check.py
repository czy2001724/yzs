# trace__init_time_check.py
# Function: init_time_check | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def init_time_check():
    """
    初始化时间检查
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_CONST           0
    #   30: LOAD_CONST           None
    #   32: IMPORT               time
    #   34: STORE_VAR            _var_var_57
    #   36: LOAD_VAR             _var_var_57
    #   38: LOAD_ATTR            _last_valid_time
    #   58: CALL                 argc=0
    #   66: STORE_GLOBAL         _last_valid_time
    #   68: LOAD_GLOBAL          sys
    #   78: CALL                 argc=0
    #   86: STORE_VAR            _var_var_79
    #   88: LOAD_VAR             _var_var_79
    #   90: TO_BOOL             
    #   98: IF_NOT               9
    #  102: LOAD_VAR             _var_var_79
    #  104: LOAD_GLOBAL          _get_network_time
    #  114: BINARY_OP           
    #  118: STORE_GLOBAL         _network_time_offset
    #  120: LOAD_GLOBAL          dirname
    #  130: LOAD_GLOBAL          executable
    #  140: LOAD_CONST           'frozen'
    #  142: LOAD_CONST           False
    #  144: CALL                 argc=3
    #  152: TO_BOOL             
    #  160: IF_NOT               140
    #  164: LOAD_GLOBAL          open
    #  174: LOAD_ATTR            str
    #  194: LOAD_ATTR           
    #  214: LOAD_GLOBAL          open
    #  224: LOAD_ATTR            str
    #  244: LOAD_ATTR           
    #  264: LOAD_GLOBAL          executable
    #  274: LOAD_ATTR           
    #  294: CALL                 argc=1
    #  302: LOAD_CONST           '.timestamp'
    #  304: CALL                 argc=2
    #  312: STORE_GLOBAL         _time_file
    #  316: LOAD_GLOBAL         
    #  326: LOAD_GLOBAL         
    #  336: LOAD_CONST           'w'
    #  338: CALL                 argc=2
    #  346: BEFORE_WITH         
    #  348: STORE_VAR            _var_var_21
    #  350: LOAD_VAR             _var_var_21
    #  352: LOAD_ATTR           
    #  372: LOAD_GLOBAL         
    #  382: LOAD_GLOBAL         
    #  392: LOAD_GLOBAL          _get_network_time
    #  402: CALL                 argc=1
    #  410: CALL                 argc=1
    #  418: CALL                 argc=1
    #  426: POP                 
    #  428: LOAD_CONST           None
    #  430: LOAD_CONST           None
    #  432: LOAD_CONST           None
    #  434: CALL                 argc=2
    #  442: POP                 
    #  444: LOAD_CONST           None
    #  452: GOTO                 43
    #  460: POP                 
    #  462: RETURN_CONST         None
    #  464: TRY                 
    #  466: WITH_EXCEPT_START   
    #  468: TO_BOOL             
    #  476: IF                   1
    #  480: RERAISE             
    #  482: POP                 
    #  484: POP_EXCEPT          
    #  486: POP                 
    #  488: POP                 
    #  490: JUMP_BACKWARD_NO_INTERRUPT
    #  492: COPY                
    #  494: POP_EXCEPT          
    #  496: RERAISE             
    #  498: TRY                 
    #  500: POP                 
    #  502: POP_EXCEPT          
    #  504: JUMP_BACKWARD_NO_INTERRUPT
    #  506: COPY                
    #  508: POP_EXCEPT          
    #  510: RERAISE             
    #  512: TRY                 
    #  514: LOAD_CONST           None
    #  520: LOAD_CONST           bytes(20)
    #  522: CALL                 argc=1
    #  530: POP                 
    #  532: RERAISE             
    #  534: COPY                
    #  536: POP_EXCEPT          
    #  538: RERAISE             
    #  540: LOAD_CONST           None
    #  544: LOAD_CONST           bytes(20)
    #  546: BUILD_TUPLE          len=1
    #  550: POP                 
    #  552: RETURN              
    pass  # See raw bytecode disassembly for control flow