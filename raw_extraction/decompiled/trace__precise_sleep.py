# trace__precise_sleep.py
# Function: precise_sleep | File: <frozen automation>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def precise_sleep(duration):
    """
    精确延时函数 - 使用忙等待实现高精度计时
    
    
    
    Windows 的 time.sleep() 精度通常只有 10-15ms，
    
    此函数通过忙等待实现更高精度的延时。
    
    
    
    Args:
    
        duration: 延时时间（秒）
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_VAR             duration
    #   30: LOAD_CONST           0
    #   32: COMPARE             
    #   36: IF_NOT               11
    #   42: LOAD_CONST           None
    #   50: GOTO                 137
    #   58: POP                 
    #   60: RETURN_CONST         None
    #   62: LOAD_GLOBAL          time
    #   72: LOAD_ATTR            sleep
    #   94: CALL                 argc=0
    #  102: LOAD_VAR             duration
    #  104: BINARY_OP           
    #  108: STORE_VAR            _var_var_0
    #  110: LOAD_VAR             duration
    #  112: LOAD_CONST           0.02
    #  114: COMPARE             
    #  118: IF_NOT               25
    #  122: LOAD_GLOBAL          time
    #  132: LOAD_ATTR           
    #  154: LOAD_VAR             duration
    #  156: LOAD_CONST           0.015
    #  158: BINARY_OP           
    #  162: CALL                 argc=1
    #  170: POP                 
    #  172: LOAD_GLOBAL          time
    #  182: LOAD_ATTR            sleep
    #  204: CALL                 argc=0
    #  212: LOAD_VAR             _var_var_0
    #  214: COMPARE             
    #  218: IF_NOT               28
    #  224: LOAD_GLOBAL          time
    #  234: LOAD_ATTR            sleep
    #  256: CALL                 argc=0
    #  264: LOAD_VAR             _var_var_0
    #  266: COMPARE             
    #  270: IF_NOT               2
    #  274: LOOP                 28
    #  278: LOAD_CONST           None
    #  286: GOTO                 19
    #  294: POP                 
    #  296: RETURN_CONST         None
    #  298: TRY                 
    #  300: LOAD_CONST           None
    #  306: LOAD_CONST           bytes(20)
    #  308: CALL                 argc=1
    #  316: POP                 
    #  318: RERAISE             
    #  320: COPY                
    #  322: POP_EXCEPT          
    #  324: RERAISE             
    #  326: LOAD_CONST           None
    #  330: LOAD_CONST           bytes(20)
    #  332: BUILD_TUPLE          len=1
    #  336: POP                 
    #  338: RETURN              
    pass  # See raw bytecode disassembly for control flow