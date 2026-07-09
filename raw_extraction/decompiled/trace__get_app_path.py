# trace__get_app_path.py
# Function: get_app_path | File: <frozen automation>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def get_app_path():
    """
    获取应用程序所在目录（兼容exe打包）
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          sys
    #   38: LOAD_GLOBAL          os
    #   48: LOAD_CONST           'frozen'
    #   50: LOAD_CONST           False
    #   52: CALL                 argc=3
    #   60: TO_BOOL             
    #   68: IF_NOT               54
    #   72: LOAD_GLOBAL          dirname
    #   82: LOAD_ATTR            abspath
    #  102: LOAD_ATTR           
    #  122: LOAD_GLOBAL          os
    #  132: LOAD_ATTR           
    #  152: CALL                 argc=1
    #  166: GOTO                 93
    #  168: CALL                 argc=1
    #  176: POP                 
    #  178: RETURN              
    #  180: LOAD_GLOBAL          dirname
    #  190: LOAD_ATTR            abspath
    #  210: LOAD_ATTR           
    #  230: LOAD_GLOBAL          dirname
    #  240: LOAD_ATTR            abspath
    #  260: LOAD_ATTR           
    #  280: LOAD_GLOBAL         
    #  290: CALL                 argc=1
    #  298: CALL                 argc=1
    #  312: GOTO                 20
    #  314: CALL                 argc=1
    #  322: POP                 
    #  324: RETURN              
    #  326: TRY                 
    #  328: LOAD_CONST           None
    #  334: LOAD_CONST           bytes(20)
    #  336: CALL                 argc=1
    #  344: POP                 
    #  346: RERAISE             
    #  348: COPY                
    #  350: POP_EXCEPT          
    #  352: RERAISE             
    #  354: LOAD_CONST           None
    #  358: LOAD_CONST           bytes(20)
    #  360: BUILD_TUPLE          len=1
    #  364: POP                 
    #  366: RETURN              
    pass  # See raw bytecode disassembly for control flow