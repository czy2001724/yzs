# security__init_integrity_check.py
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
    #   26: FOR_ITER             171
    #   30: LOAD_ATTR           
    #   50: IF_NOT_NONE          254
    #   54: IF_NOT_NONE          245
    #   60: TO_BOOL             
    #   68: GET_YIELD_FROM_ITER 
    #   70: LOAD_SUPER_ATTR     
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