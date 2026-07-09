# security__init_time_check.py
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
    #   26: GET_AWAITABLE       
    #   28: STORE_ATTR          
    #   40: LOAD_FROM_DICT_OR_DEREF
    #   42: BINARY_OP           
    #   46: BINARY_OP           
    #   50: MATCH_MAPPING       
    #   52: LOAD_GLOBAL         
    #   62: CALL                 argc=138
    #   72: STORE_SUBSCR        
    #   78: FOR_ITER             182
    #   82: CALL                 argc=90
    #   92: CHECK_EG_MATCH      
    #   94: IF_NOT               33
    #  100: RETURN_GENERATOR    
    #  102: NOT                 
    #  104: CALL                 argc=192
    #  114: BINARY_OP           
    #  118: LOAD_CONST          
    #  122: DICT_UPDATE         
    #  124: COMPARE             
    #  134: GET_YIELD_FROM_ITER 
    #  136: LOAD_DEREF          
    #  138: STORE_SLICE         
    #  140: MATCH_CLASS         
    #  142: CALL                 argc=25
    #  150: LOAD_BUILD_CLASS    
    #  152: YIELD               
    #  154: SET_ADD             
    #  158: UNPACK               141
    #  162: LOAD_ATTR           
    #  182: FOR_ITER             161
    #  186: GET_ITER            
    #  188: RETURN_CONST        
    #  190: DICT_UPDATE         
    #  192: RETURN              
    #  194: IF_NOT               48
    #  198: TO_BOOL             
    #  208: STORE_ATTR          
    #  218: POP                 
    #  220: COMPARE             
    #  224: CLEANUP_THROW       
    #  228: RETURN_GENERATOR    
    #  230: FORMAT_WITH_SPEC    
    #  232: LOAD_ATTR           
    #  252: STORE_SLICE         
    #  254: GET_AWAITABLE       
    #  256: LOAD_FAST_CHECK     
    #  258: MATCH_SEQUENCE      
    #  260: TO_BOOL             
    #  268: CONTAINS            
    #  272: CHECK_EXC_MATCH     
    #  274: DELETE_DEREF        
    #  278: LOAD_GLOBAL         
    #  288: CALL                 argc=13
    #  296: COMPARE             
    #  300: MAP_ADD             
    #  304: LOAD_ATTR           
    #  324: FOR_ITER             66
    #  330: BINARY_OP           
    #  336: RESERVED            
    #  338: BINARY_SUBSCR       
    #  344: BEFORE_ASYNC_WITH   
    #  346: BINARY_OP           
    #  352: MATCH_SEQUENCE      
    #  356: STORE_DEREF         
    #  358: DELETE_DEREF        
    #  364: COMPARE             
    #  368: CALL                 argc=64
    #  376: WITH_EXCEPT_START   
    #  378: CALL                 argc=200
    #  386: END_FOR             
    #  388: IS                  
    #  390: DELETE_DEREF        
    #  392: LOOP                 43
    #  398: CALL                 argc=52
    #  406: SET_FUNCTION_ATTRIBUTE
    #  408: END_ASYNC_FOR       
    #  414: LOAD_GLOBAL         
    #  426: LOAD_VAR            
    #  430: STORE_GLOBAL        
    #  432: TO_BOOL             
    #  440: FOR_ITER             154
    #  446: POP_EXCEPT          
    #  450: BINARY_OP           
    #  454: MATCH_KEYS          
    #  456: TO_BOOL             
    #  468: COMPARE             
    #  472: IF                   187
    #  476: GOTO                 141
    #  478: IF_NOT_NONE          86
    #  482: IF_NOT_NONE          158
    #  486: CALL                 argc=16
    #  496: STORE_FAST_LOAD_FAST
    #  498: MAP_ADD             
    #  500: BUILD_TUPLE          len=174
    #  504: CALL                 argc=89
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