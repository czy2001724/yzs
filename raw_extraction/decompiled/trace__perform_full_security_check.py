# trace__perform_full_security_check.py
# Function: perform_full_security_check | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def perform_full_security_check():
    """
    执行完整的安全检查
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          verify_integrity
    #   38: CALL                 argc=0
    #   46: UNPACK               2
    #   50: STORE_FAST_STORE_FAST
    #   52: LOAD_VAR             _var_var_84
    #   54: TO_BOOL             
    #   62: IF                   13
    #   66: LOAD_CONST           False
    #   68: LOAD_VAR             _var_var_85
    #   70: BUILD_TUPLE          len=2
    #   78: GOTO                 121
    #   80: CALL                 argc=1
    #   88: POP                 
    #   90: RETURN              
    #   92: LOAD_GLOBAL          _heartbeat_thread
    #  102: CALL                 argc=0
    #  110: TO_BOOL             
    #  118: IF                   11
    #  124: LOAD_CONST           <tuple>
    #  132: GOTO                 94
    #  140: POP                 
    #  142: RETURN_CONST         <tuple>
    #  144: LOAD_GLOBAL         
    #  154: CALL                 argc=0
    #  162: UNPACK               2
    #  166: STORE_FAST_STORE_FAST
    #  168: LOAD_VAR             _var_var_86
    #  170: TO_BOOL             
    #  178: IF                   13
    #  182: LOAD_CONST           False
    #  184: LOAD_VAR             _var_var_87
    #  186: BUILD_TUPLE          len=2
    #  194: GOTO                 63
    #  196: CALL                 argc=1
    #  204: POP                 
    #  206: RETURN              
    #  208: LOAD_GLOBAL         
    #  218: IF_NONE              26
    #  222: LOAD_GLOBAL         
    #  232: CALL                 argc=0
    #  240: TO_BOOL             
    #  248: IF                   11
    #  254: LOAD_CONST           <tuple>
    #  262: GOTO                 29
    #  270: POP                 
    #  272: RETURN_CONST         <tuple>
    #  274: LOAD_CONST           <tuple>
    #  282: GOTO                 19
    #  290: POP                 
    #  292: RETURN_CONST         <tuple>
    #  294: TRY                 
    #  296: LOAD_CONST           None
    #  302: LOAD_CONST           bytes(20)
    #  304: CALL                 argc=1
    #  312: POP                 
    #  314: RERAISE             
    #  316: COPY                
    #  318: POP_EXCEPT          
    #  320: RERAISE             
    #  322: LOAD_CONST           None
    #  326: LOAD_CONST           bytes(20)
    #  328: BUILD_TUPLE          len=1
    #  332: POP                 
    #  334: RETURN              
    pass  # See raw bytecode disassembly for control flow