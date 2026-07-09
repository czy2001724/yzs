# trace___calculate_exe_hash.py
# Function: _calculate_exe_hash | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def _calculate_exe_hash():
    """
    计算当前exe文件的hash
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          sys
    #   38: LOAD_GLOBAL          executable
    #   48: LOAD_CONST           'frozen'
    #   50: LOAD_CONST           False
    #   52: CALL                 argc=3
    #   60: TO_BOOL             
    #   68: IF                   11
    #   74: LOAD_CONST           'DEV_MODE'
    #   82: GOTO                 164
    #   90: POP                 
    #   92: RETURN_CONST         'DEV_MODE'
    #   96: LOAD_GLOBAL          executable
    #  106: LOAD_ATTR            hashlib
    #  126: STORE_VAR            _var_var_74
    #  128: LOAD_GLOBAL          hexdigest
    #  138: LOAD_VAR             _var_var_74
    #  140: LOAD_CONST           'rb'
    #  142: CALL                 argc=2
    #  150: BEFORE_WITH         
    #  152: STORE_VAR            _var_var_21
    #  154: LOAD_GLOBAL         
    #  164: LOAD_ATTR           
    #  186: LOAD_VAR             _var_var_21
    #  188: LOAD_ATTR           
    #  208: CALL                 argc=0
    #  216: CALL                 argc=1
    #  224: LOAD_ATTR           
    #  244: CALL                 argc=0
    #  252: LOAD_CONST           None
    #  254: LOAD_CONST           32
    #  256: BINARY_SLICE        
    #  258: SWAP                
    #  260: LOAD_CONST           None
    #  262: LOAD_CONST           None
    #  264: LOAD_CONST           None
    #  266: CALL                 argc=2
    #  274: POP                 
    #  282: GOTO                 64
    #  284: CALL                 argc=1
    #  292: POP                 
    #  294: RETURN              
    #  296: TRY                 
    #  298: WITH_EXCEPT_START   
    #  300: TO_BOOL             
    #  308: IF                   1
    #  312: RERAISE             
    #  314: POP                 
    #  316: POP_EXCEPT          
    #  318: POP                 
    #  320: POP                 
    #  322: GOTO                 19
    #  324: COPY                
    #  326: POP_EXCEPT          
    #  328: RERAISE             
    #  330: TRY                 
    #  332: POP                 
    #  334: POP_EXCEPT          
    #  336: LOAD_CONST           'ERROR'
    #  344: GOTO                 33
    #  352: POP                 
    #  354: RETURN_CONST         'ERROR'
    #  356: COPY                
    #  358: POP_EXCEPT          
    #  360: RERAISE             
    #  364: LOAD_CONST           None
    #  372: GOTO                 19
    #  380: POP                 
    #  382: RETURN_CONST         None
    #  384: TRY                 
    #  386: LOAD_CONST           None
    #  392: LOAD_CONST           bytes(20)
    #  394: CALL                 argc=1
    #  402: POP                 
    #  404: RERAISE             
    #  406: COPY                
    #  408: POP_EXCEPT          
    #  410: RERAISE             
    #  412: LOAD_CONST           None
    #  416: LOAD_CONST           bytes(20)
    #  418: BUILD_TUPLE          len=1
    #  422: POP                 
    #  424: RETURN              
    pass  # See raw bytecode disassembly for control flow