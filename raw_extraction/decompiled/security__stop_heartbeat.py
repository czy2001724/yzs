# security__stop_heartbeat.py
# Function: stop_heartbeat | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def stop_heartbeat():
    """
    停止心跳验证
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
    #   48: IF_NOT_NONE          16
    #   52: TRY                 
    #   54: LOAD_CONST           None
    #   60: LOAD_CONST           bytes(20)
    #   62: CALL                 argc=1
    #   70: POP                 
    #   72: RERAISE             
    #   74: COPY                
    #   76: POP_EXCEPT          
    #   78: RERAISE             
    #   80: LOAD_CONST           None
    #   84: LOAD_CONST           bytes(20)
    #   86: BUILD_TUPLE          len=1
    #   90: POP                 
    #   92: RETURN              
    pass  # See raw bytecode disassembly for control flow