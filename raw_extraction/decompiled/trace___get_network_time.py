# trace___get_network_time.py
# Function: _get_network_time | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def _get_network_time():
    """
    获取网络时间（多源）
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
    #   36: LOAD_CONST           'https://worldtimeapi.org/api/ip'
    #   38: LOAD_CONST           'https://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp'
    #   40: BUILD_LIST          
    #   42: STORE_VAR            _var_var_76
    #   44: LOAD_VAR             _var_var_76
    #   46: GET_ITER            
    #   48: FOR_ITER             137
    #   52: STORE_VAR            _var_var_77
    #   56: LOAD_CONST           0
    #   58: LOAD_CONST           None
    #   60: IMPORT               requests
    #   62: STORE_VAR            _var_var_58
    #   64: LOAD_VAR             _var_var_58
    #   66: LOAD_ATTR            float
    #   86: LOAD_VAR             _var_var_77
    #   88: LOAD_CONST           3
    #   90: LOAD_CONST           <tuple>
    #   94: STORE_VAR            _var_var_78
    #   96: LOAD_VAR             _var_var_78
    #   98: LOAD_ATTR           
    #  118: LOAD_CONST           200
    #  120: COMPARE             
    #  124: IF_NOT               97
    #  128: LOAD_VAR             _var_var_78
    #  130: LOAD_ATTR           
    #  150: CALL                 argc=0
    #  158: STORE_VAR            _var_var_22
    #  160: LOAD_CONST           'unixtime'
    #  162: LOAD_VAR             _var_var_22
    #  164: CONTAINS            
    #  168: IF_NOT               25
    #  172: LOAD_GLOBAL         
    #  182: LOAD_VAR             _var_var_22
    #  184: LOAD_CONST           'unixtime'
    #  186: BINARY_SUBSCR       
    #  190: CALL                 argc=1
    #  198: SWAP                
    #  200: POP                 
    #  208: GOTO                 92
    #  210: CALL                 argc=1
    #  218: POP                 
    #  220: RETURN              
    #  222: LOAD_CONST           'data'
    #  224: LOAD_VAR             _var_var_22
    #  226: CONTAINS            
    #  230: IF_NOT               42
    #  234: LOAD_CONST           't'
    #  236: LOAD_VAR             _var_var_22
    #  238: LOAD_CONST           'data'
    #  240: BINARY_SUBSCR       
    #  244: CONTAINS            
    #  248: IF_NOT               31
    #  252: LOAD_GLOBAL         
    #  262: LOAD_VAR             _var_var_22
    #  264: LOAD_CONST           'data'
    #  266: BINARY_SUBSCR       
    #  270: LOAD_CONST           't'
    #  272: BINARY_SUBSCR       
    #  276: CALL                 argc=1
    #  284: LOAD_CONST           1000
    #  286: BINARY_OP           
    #  290: SWAP                
    #  292: POP                 
    #  300: GOTO                 46
    #  302: CALL                 argc=1
    #  310: POP                 
    #  312: RETURN              
    #  314: LOOP                 135
    #  318: LOOP                 137
    #  322: LOOP                 139
    #  326: END_FOR             
    #  328: POP                 
    #  330: LOAD_CONST           None
    #  338: GOTO                 27
    #  346: POP                 
    #  348: RETURN_CONST         None
    #  350: TRY                 
    #  352: POP                 
    #  354: POP_EXCEPT          
    #  356: LOOP                 156
    #  360: COPY                
    #  362: POP_EXCEPT          
    #  364: RERAISE             
    #  366: TRY                 
    #  368: LOAD_CONST           None
    #  374: LOAD_CONST           bytes(20)
    #  376: CALL                 argc=1
    #  384: POP                 
    #  386: RERAISE             
    #  388: COPY                
    #  390: POP_EXCEPT          
    #  392: RERAISE             
    #  394: LOAD_CONST           None
    #  398: LOAD_CONST           bytes(20)
    #  400: BUILD_TUPLE          len=1
    #  404: POP                 
    #  406: RETURN              
    pass  # See raw bytecode disassembly for control flow