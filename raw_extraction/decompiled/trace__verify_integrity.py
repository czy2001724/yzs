# trace__verify_integrity.py
# Function: verify_integrity | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def verify_integrity():
    """
    验证代码完整性
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          _exe_hash
    #   38: IF_NOT_NONE          31
    #   42: LOAD_GLOBAL          _calculate_exe_hash
    #   52: LOAD_GLOBAL         
    #   62: LOAD_CONST           'frozen'
    #   64: LOAD_CONST           False
    #   66: CALL                 argc=3
    #   74: TO_BOOL             
    #   82: NOT                 
    #   90: GOTO                 48
    #   92: CALL                 argc=1
    #  100: POP                 
    #  102: RETURN              
    #  104: LOAD_GLOBAL         
    #  114: CALL                 argc=0
    #  122: STORE_VAR            _var_var_75
    #  124: LOAD_VAR             _var_var_75
    #  126: LOAD_GLOBAL          _exe_hash
    #  136: COMPARE             
    #  146: GOTO                 20
    #  148: CALL                 argc=1
    #  156: POP                 
    #  158: RETURN              
    #  160: TRY                 
    #  162: LOAD_CONST           None
    #  168: LOAD_CONST           bytes(20)
    #  170: CALL                 argc=1
    #  178: POP                 
    #  180: RERAISE             
    #  182: COPY                
    #  184: POP_EXCEPT          
    #  186: RERAISE             
    #  188: LOAD_CONST           None
    #  192: LOAD_CONST           bytes(20)
    #  194: BUILD_TUPLE          len=1
    #  198: POP                 
    #  200: RETURN              
    pass  # See raw bytecode disassembly for control flow