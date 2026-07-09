# trace__init_integrity_check.py
# Function: init_integrity_check | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def init_integrity_check():
    """
    初始化完整性校验，返回hash供后续验证
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          _exe_hash
    #   38: CALL                 argc=0
    #   46: STORE_GLOBAL         _exe_hash
    #   48: LOAD_GLOBAL         
    #   64: GOTO                 20
    #   66: CALL                 argc=1
    #   74: POP                 
    #   76: RETURN              
    #   78: TRY                 
    #   80: LOAD_CONST           None
    #   86: LOAD_CONST           bytes(20)
    #   88: CALL                 argc=1
    #   96: POP                 
    #   98: RERAISE             
    #  100: COPY                
    #  102: POP_EXCEPT          
    #  104: RERAISE             
    #  106: LOAD_CONST           None
    #  110: LOAD_CONST           bytes(20)
    #  112: BUILD_TUPLE          len=1
    #  116: POP                 
    #  118: RETURN              
    pass  # See raw bytecode disassembly for control flow