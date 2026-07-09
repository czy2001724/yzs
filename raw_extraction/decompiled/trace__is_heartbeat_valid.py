# trace__is_heartbeat_valid.py
# Function: is_heartbeat_valid | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def is_heartbeat_valid():
    """
    检查心跳状态
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          _last_heartbeat_success
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