# web_server__WebServer__build_editable_groups.py
# Function: _build_editable_groups | File: <frozen web_server>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def _build_editable_groups(self):
    """
    构建只包含可编辑步骤的groups结构
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   26: LOAD_ATTR           
    #   46: JUMP_BACKWARD_NO_INTERRUPT
    #   48: UNPACK               16
    #   54: LOAD_GLOBAL         
    #   68: LOAD_DEREF          
    #   70: LOAD_SUPER_ATTR     
    #   74: BINARY_SUBSCR       
    #   80: SET_ADD             
    #   86: BINARY_SUBSCR       
    #   90: BINARY_OP           
    #   94: LOAD_ATTR           
    #  114: FOR_ITER             71
    #  118: LIST_APPEND         
    #  120: MATCH_KEYS          
    #  122: GET_AWAITABLE       
    #  124: DELETE_DEREF        
    #  126: TO_BOOL             
    #  134: FORMAT_SIMPLE       
    #  136: CALL                 argc=13
    #  144: DELETE_GLOBAL       
    #  146: GET_LEN             
    #  148: GOTO                 157
    #  150: FOR_ITER             140
    #  154: STORE_NAME          
    #  156: LOAD_GLOBAL         
    #  166: BEFORE_WITH         
    #  172: LOAD_SUPER_ATTR     
    #  176: GOTO                 193
    #  178: LOAD_DEREF          
    #  180: LOAD_ATTR           
    #  200: YIELD               
    #  202: FOR_ITER             156
    #  206: RETURN              
    #  208: CALL                 argc=226
    #  216: BINARY_OP           
    #  220: RETURN              
    #  222: CALL                 argc=34
    #  232: CALL                 argc=37
    #  240: LOAD_ATTR           
    #  260: BINARY_OP           
    #  264: LOAD_VAR            
    #  266: LOAD_VAR            
    #  268: GET_ANEXT           
    #  270: MATCH_MAPPING       
    #  272: STORE_GLOBAL        
    #  274: LOAD_ATTR           
    #  294: MATCH_MAPPING       
    #  296: RETURN              
    #  302: DELETE_DEREF        
    #  306: STORE_SUBSCR        
    #  310: SET_FUNCTION_ATTRIBUTE
    #  312: BUILD_MAP           
    #  314: JUMP_BACKWARD_NO_INTERRUPT
    #  316: TO_BOOL             
    #  324: STORE_ATTR          
    #  338: CALL                 argc=151
    #  346: RETURN_CONST        
    #  350: LOAD_ATTR           
    #  370: COPY                
    #  372: RETURN_CONST        
    #  374: LOAD_ATTR           
    #  394: CALL                 argc=234
    #  402: MATCH_KEYS          
    #  404: CONVERT_VALUE       
    #  406: COMPARE             
    #  410: LOAD_FROM_DICT_OR_DEREF
    #  412: TO_BOOL             
    #  422: CLEANUP_THROW       
    #  424: BUILD_MAP           
    #  426: CALL                 argc=173
    #  434: MATCH_MAPPING       
    #  436: STORE_FAST_LOAD_FAST
    #  440: SETUP_ANNOTATIONS   
    #  442: TO_BOOL             
    #  450: LOAD_ATTR            copy
    #  470: CALL                 argc=232
    #  482: IF_NOT_NONE          253
    #  486: CALL                 argc=103
    #  494: FOR_ITER             202
    #  498: LOAD_FROM_DICT_OR_DEREF
    #  500: LIST_APPEND         
    #  502: MATCH_MAPPING       
    #  504: STORE_FAST_STORE_FAST
    #  508: STORE_SUBSCR        
    #  512: SEND                
    #  516: LOAD_FROM_DICT_OR_GLOBALS
    #  518: SET_UPDATE          
    #  520: EXIT_INIT_CHECK     
    #  522: IF_NONE              62
    #  526: BINARY_SUBSCR       
    #  530: BEFORE_ASYNC_WITH   
    #  532: SET_ADD             
    #  534: FOR_ITER             133
    #  542: CALL                 argc=66
    #  550: LOOP                 56
    #  556: DELETE_DEREF        
    #  560: BINARY_SUBSCR       
    #  564: CALL                 argc=234
    #  572: GOTO                 102
    #  576: BEFORE_ASYNC_WITH   
    #  578: TO_BOOL             
    #  588: MATCH_CLASS         
    #  590: END_SEND            
    #  592: TRY                 
    #  594: LOAD_CONST           None
    #  600: LOAD_CONST           bytes(20)
    #  602: CALL                 argc=1
    #  610: POP                 
    #  612: RERAISE             
    #  614: COPY                
    #  616: POP_EXCEPT          
    #  618: RERAISE             
    #  620: LOAD_CONST           None
    #  624: LOAD_CONST           bytes(20)
    #  626: BUILD_TUPLE          len=1
    #  630: POP                 
    #  632: RETURN              
    pass  # See raw bytecode disassembly for control flow