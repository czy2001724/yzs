# security__init_security.py
# Function: init_security | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def init_security(server_url, machine_id):
    """
    初始化安全模块
    在程序启动时调用
    
    Args:
        server_url: 服务器地址（用于心跳验证）
        machine_id: 机器ID（用于心跳验证）
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_ATTR           
    #   48: TO_BOOL             
    #   56: BINARY_SUBSCR       
    #   60: BINARY_SUBSCR       
    #   66: CHECK_EXC_MATCH     
    #   70: RETURN              
    #   72: CALL                 argc=223
    #   80: RETURN              
    #   82: MATCH_CLASS         
    #   84: COMPARE             
    #   88: CALL                 argc=79
    #   98: CALL                 argc=123
    #  106: UNARY_INVERT        
    #  108: END_FOR             
    #  110: LOAD_LOCALS         
    #  112: STORE_FAST_LOAD_FAST
    #  114: LOAD_ATTR           
    #  134: COPY                
    #  138: BUILD_LIST          
    #  140: LOAD_SUPER_ATTR     
    #  144: LOAD_SUPER_ATTR     
    #  148: UNPACK               104
    #  152: LOOP                 21
    #  156: LIST_EXTEND         
    #  158: BUILD_CONST_KEY_MAP 
    #  160: LOAD_ATTR           
    #  180: LOAD_ASSERTION_ERROR
    #  186: CALL                 argc=69
    #  196: BUILD_MAP           
    #  198: END_SEND            
    #  200: CALL                 argc=49
    #  208: STORE_FAST_STORE_FAST
    #  210: TO_BOOL             
    #  218: CALL                 argc=187
    #  228: CALL                 argc=63
    #  236: DELETE_GLOBAL       
    #  238: SEND                
    #  242: SET_ADD             
    #  244: FORMAT_SIMPLE       
    #  246: IF_NONE              177
    #  252: CALL                 argc=224
    #  262: LOAD_CONST           bytes(20)
    #  264: CALL                 argc=1
    #  272: POP                 
    #  274: RERAISE             
    #  276: COPY                
    #  278: POP_EXCEPT          
    #  280: RERAISE             
    #  282: LOAD_CONST           None
    #  286: LOAD_CONST           bytes(20)
    #  288: BUILD_TUPLE          len=1
    #  292: POP                 
    #  294: RETURN              
    pass  # See raw bytecode disassembly for control flow