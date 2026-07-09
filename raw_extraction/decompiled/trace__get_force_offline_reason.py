# trace__get_force_offline_reason.py
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
    #   28: LOAD_GLOBAL          _force_offline_reason
    #   44: GOTO                 20
    #   46: CALL                 argc=1
    #   54: POP                 
    #   56: RETURN              
    #   58: TRY                 
    #   60: LOAD_CONST           None
    #   66: LOAD_CONST           bytes(20)
    #   68: CALL                 argc=1
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