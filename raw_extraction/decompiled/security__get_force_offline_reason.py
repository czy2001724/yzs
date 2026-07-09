# security__get_force_offline_reason.py
# Function: get_force_offline_reason | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def get_force_offline_reason():
    """
    获取强制下线原因（服务端解绑/删除激活码时推送），返回None表示无强制下线
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: IF_NOT               130
    #   32: STORE_ATTR          
    #   42: RETURN_CONST        
    #   44: CONTAINS            
    #   48: BINARY_SUBSCR       
    #   52: STORE_SUBSCR        
    #   56: LOAD_ATTR           
    #   76: POP                 
    #   78: RERAISE             
    #   80: COPY                
    #   82: POP_EXCEPT          
    #   84: RERAISE             
    #   86: LOAD_CONST           None
    #   90: LOAD_CONST           bytes(20)
    #   92: BUILD_TUPLE          len=1
    #   96: POP                 
    #   98: RETURN              
    pass  # See raw bytecode disassembly for control flow