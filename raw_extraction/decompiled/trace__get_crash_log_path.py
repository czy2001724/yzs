# trace__get_crash_log_path.py
# Function: get_crash_log_path | File: <frozen main_pyqt_v3>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def get_crash_log_path():
    """
    获取崩溃日志路径
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
    #   68: IF_NOT               84
    #   72: LOAD_GLOBAL          join
    #   82: LOAD_ATTR            executable
    #  102: LOAD_ATTR           
    #  122: LOAD_GLOBAL          join
    #  132: LOAD_ATTR            executable
    #  152: LOAD_ATTR           
    #  172: LOAD_GLOBAL          os
    #  182: LOAD_ATTR           
    #  202: CALL                 argc=1
    #  210: LOAD_CONST           'crash_log.txt'
    #  212: CALL                 argc=2
    #  226: GOTO                 123
    #  228: CALL                 argc=1
    #  236: POP                 
    #  238: RETURN              
    #  240: LOAD_GLOBAL          join
    #  250: LOAD_ATTR            executable
    #  270: LOAD_ATTR           
    #  290: LOAD_GLOBAL          join
    #  300: LOAD_ATTR            executable
    #  320: LOAD_ATTR           
    #  340: LOAD_GLOBAL          join
    #  350: LOAD_ATTR            executable
    #  370: LOAD_ATTR           
    #  390: LOAD_GLOBAL         
    #  400: CALL                 argc=1
    #  408: CALL                 argc=1
    #  416: LOAD_CONST           'crash_log.txt'
    #  418: CALL                 argc=2
    #  432: GOTO                 20
    #  434: CALL                 argc=1
    #  442: POP                 
    #  444: RETURN              
    #  446: TRY                 
    #  448: LOAD_CONST           None
    #  454: LOAD_CONST           bytes(20)
    #  456: CALL                 argc=1
    #  464: POP                 
    #  466: RERAISE             
    #  468: COPY                
    #  470: POP_EXCEPT          
    #  472: RERAISE             
    #  474: LOAD_CONST           None
    #  478: LOAD_CONST           bytes(20)
    #  480: BUILD_TUPLE          len=1
    #  484: POP                 
    #  486: RETURN              
    pass  # See raw bytecode disassembly for control flow