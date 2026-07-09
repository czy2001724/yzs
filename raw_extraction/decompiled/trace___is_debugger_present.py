# trace___is_debugger_present.py
# Function: _is_debugger_present | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def _is_debugger_present():
    """
    检测调试器（Windows API）
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          sys
    #   38: LOAD_ATTR            ctypes
    #   58: LOAD_CONST           'win32'
    #   60: COMPARE             
    #   64: IF_NOT               11
    #   70: LOAD_CONST           False
    #   78: GOTO                 360
    #   86: POP                 
    #   88: RETURN_CONST         False
    #   92: LOAD_GLOBAL          kernel32
    #  102: LOAD_ATTR            c_bool
    #  122: LOAD_ATTR            GetCurrentProcess
    #  142: STORE_VAR            _var_var_7
    #  144: LOAD_VAR             _var_var_7
    #  146: LOAD_ATTR            ntdll
    #  166: CALL                 argc=0
    #  174: TO_BOOL             
    #  182: IF_NOT               11
    #  188: LOAD_CONST           True
    #  196: GOTO                 301
    #  204: POP                 
    #  206: RETURN_CONST         True
    #  208: LOAD_GLOBAL          kernel32
    #  218: LOAD_ATTR            c_ulong
    #  240: LOAD_CONST           False
    #  242: CALL                 argc=1
    #  250: STORE_VAR            _var_var_25
    #  252: LOAD_VAR             _var_var_7
    #  254: LOAD_ATTR           
    #  274: LOAD_VAR             _var_var_7
    #  276: LOAD_ATTR           
    #  296: CALL                 argc=0
    #  304: LOAD_GLOBAL          kernel32
    #  314: LOAD_ATTR           
    #  336: LOAD_VAR             _var_var_25
    #  338: CALL                 argc=1
    #  346: CALL                 argc=2
    #  354: POP                 
    #  356: LOAD_VAR             _var_var_25
    #  358: LOAD_ATTR           
    #  378: TO_BOOL             
    #  386: IF_NOT               11
    #  392: LOAD_CONST           True
    #  400: GOTO                 199
    #  408: POP                 
    #  410: RETURN_CONST         True
    #  414: LOAD_GLOBAL          kernel32
    #  424: LOAD_ATTR            c_bool
    #  444: LOAD_ATTR           
    #  464: STORE_VAR            _var_var_26
    #  466: LOAD_GLOBAL          kernel32
    #  476: LOAD_ATTR           
    #  498: CALL                 argc=0
    #  506: STORE_VAR            _var_var_27
    #  508: LOAD_VAR             _var_var_26
    #  510: LOAD_ATTR           
    #  530: LOAD_VAR             _var_var_7
    #  532: LOAD_ATTR           
    #  552: CALL                 argc=0
    #  560: LOAD_CONST           31
    #  562: LOAD_GLOBAL          kernel32
    #  572: LOAD_ATTR           
    #  594: LOAD_VAR             _var_var_27
    #  596: CALL                 argc=1
    #  604: LOAD_GLOBAL          kernel32
    #  614: LOAD_ATTR           
    #  636: LOAD_VAR             _var_var_27
    #  638: CALL                 argc=1
    #  646: LOAD_CONST           None
    #  648: CALL                 argc=5
    #  656: STORE_VAR            _var_var_28
    #  658: LOAD_VAR             _var_var_28
    #  660: LOAD_CONST           0
    #  662: COMPARE             
    #  666: IF_NOT               27
    #  670: LOAD_VAR             _var_var_27
    #  672: LOAD_ATTR           
    #  692: LOAD_CONST           0
    #  694: COMPARE             
    #  698: IF_NOT               11
    #  704: LOAD_CONST           True
    #  712: GOTO                 43
    #  720: POP                 
    #  722: RETURN_CONST         True
    #  724: LOAD_CONST           False
    #  732: GOTO                 33
    #  740: POP                 
    #  742: RETURN_CONST         False
    #  744: TRY                 
    #  746: POP                 
    #  748: POP_EXCEPT          
    #  750: JUMP_BACKWARD_NO_INTERRUPT
    #  752: COPY                
    #  754: POP_EXCEPT          
    #  756: RERAISE             
    #  758: TRY                 
    #  760: POP                 
    #  762: POP_EXCEPT          
    #  764: JUMP_BACKWARD_NO_INTERRUPT
    #  766: COPY                
    #  768: POP_EXCEPT          
    #  770: RERAISE             
    #  772: TRY                 
    #  774: LOAD_CONST           None
    #  780: LOAD_CONST           bytes(20)
    #  782: CALL                 argc=1
    #  790: POP                 
    #  792: RERAISE             
    #  794: COPY                
    #  796: POP_EXCEPT          
    #  798: RERAISE             
    #  800: LOAD_CONST           None
    #  804: LOAD_CONST           bytes(20)
    #  806: BUILD_TUPLE          len=1
    #  810: POP                 
    #  812: RETURN              
    pass  # See raw bytecode disassembly for control flow