# trace___check_loaded_dlls.py
# Function: _check_loaded_dlls | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def _check_loaded_dlls():
    """
    检查当前进程加载的可疑DLL（增强版：特征检测）
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
    #   70: LOAD_CONST           <tuple>
    #   78: GOTO                 541
    #   86: POP                 
    #   88: RETURN_CONST         <tuple>
    #   92: LOAD_CONST           0
    #   94: LOAD_CONST           None
    #   96: IMPORT               ctypes
    #   98: STORE_VAR            _var_var_5
    #  100: LOAD_CONST           0
    #  102: LOAD_CONST           <tuple>
    #  104: IMPORT               ctypes
    #  106: IMPORT_FROM          wintypes
    #  108: STORE_VAR            _var_var_6
    #  110: POP                 
    #  112: LOAD_VAR             _var_var_5
    #  114: LOAD_ATTR            c_void_p
    #  134: LOAD_ATTR            EnumProcessModules
    #  154: STORE_VAR            _var_var_7
    #  156: LOAD_VAR             _var_var_5
    #  158: LOAD_ATTR            c_void_p
    #  178: LOAD_ATTR            sizeof
    #  198: STORE_VAR            _var_var_8
    #  200: LOAD_VAR             _var_var_7
    #  202: LOAD_ATTR            environ
    #  222: CALL                 argc=0
    #  230: STORE_VAR            _var_var_9
    #  232: LOAD_VAR             _var_var_5
    #  234: LOAD_ATTR            get
    #  254: LOAD_CONST           1024
    #  256: BINARY_OP           
    #  262: CALL                 argc=0
    #  270: STORE_VAR            _var_var_10
    #  272: LOAD_VAR             _var_var_6
    #  274: LOAD_ATTR            create_unicode_buffer
    #  294: CALL                 argc=0
    #  302: STORE_VAR            _var_var_11
    #  304: LOAD_VAR             _var_var_8
    #  306: LOAD_ATTR            path
    #  326: LOAD_FAST_LOAD_FAST 
    #  328: LOAD_ATTR            basename
    #  350: LOAD_VAR             _var_var_10
    #  352: CALL                 argc=1
    #  360: LOAD_VAR             _var_var_5
    #  362: LOAD_ATTR            _check_dll_exports
    #  384: LOAD_VAR             _var_var_10
    #  386: CALL                 argc=1
    #  394: LOAD_VAR             _var_var_5
    #  396: LOAD_ATTR            basename
    #  418: LOAD_VAR             _var_var_11
    #  420: CALL                 argc=1
    #  428: CALL                 argc=4
    #  436: TO_BOOL             
    #  446: IF_NOT               316
    #  450: LOAD_VAR             _var_var_11
    #  452: LOAD_ATTR           
    #  472: LOAD_VAR             _var_var_5
    #  474: LOAD_ATTR            _check_dll_exports
    #  496: LOAD_VAR             _var_var_5
    #  498: LOAD_ATTR            get
    #  518: CALL                 argc=1
    #  526: BINARY_OP           
    #  530: STORE_VAR            _var_var_12
    #  532: LOAD_GLOBAL         
    #  542: LOAD_ATTR           
    #  562: LOAD_ATTR           
    #  582: LOAD_CONST           'SystemRoot'
    #  584: LOAD_CONST           'C:\\Windows'
    #  586: CALL                 argc=2
    #  594: LOAD_ATTR           
    #  614: CALL                 argc=0
    #  622: STORE_VAR            _var_var_13
    #  624: LOAD_GLOBAL         
    #  634: LOAD_VAR             _var_var_12
    #  636: CALL                 argc=1
    #  644: GET_ITER            
    #  646: FOR_ITER             214
    #  650: STORE_VAR            _var_var_0
    #  652: LOAD_FAST_LOAD_FAST 
    #  654: BINARY_SUBSCR       
    #  658: STORE_VAR            _var_var_14
    #  660: LOAD_VAR             _var_var_5
    #  662: LOAD_ATTR           
    #  684: LOAD_CONST           260
    #  686: CALL                 argc=1
    #  694: STORE_VAR            _var_var_15
    #  696: LOAD_VAR             _var_var_8
    #  698: LOAD_ATTR           
    #  718: LOAD_FAST_LOAD_FAST 
    #  720: LOAD_VAR             _var_var_15
    #  722: LOAD_CONST           260
    #  724: CALL                 argc=4
    #  732: TO_BOOL             
    #  740: IF                   2
    #  744: LOOP                 51
    #  748: LOAD_VAR             _var_var_15
    #  750: LOAD_ATTR           
    #  770: LOAD_ATTR           
    #  790: CALL                 argc=0
    #  798: STORE_VAR            _var_var_16
    #  800: LOAD_GLOBAL         
    #  810: LOAD_ATTR           
    #  830: LOAD_ATTR           
    #  850: LOAD_VAR             _var_var_16
    #  852: CALL                 argc=1
    #  860: STORE_VAR            _var_var_17
    #  862: LOAD_VAR             _var_var_17
    #  864: LOAD_GLOBAL         
    #  874: CONTAINS            
    #  878: IF_NOT               28
    #  882: LOAD_VAR             _var_var_17
    #  884: LOAD_CONST           <tuple>
    #  886: CONTAINS            
    #  890: IF_NOT               7
    #  894: LOAD_FAST_LOAD_FAST 
    #  896: CONTAINS            
    #  900: IF_NOT               2
    #  904: LOOP                 131
    #  908: LOAD_CONST           True
    #  910: LOAD_VAR             _var_var_17
    #  912: BUILD_TUPLE          len=2
    #  914: SWAP                
    #  916: POP                 
    #  924: GOTO                 118
    #  926: CALL                 argc=1
    #  934: POP                 
    #  936: RETURN              
    #  938: BUILD_LIST          
    #  940: LOAD_CONST           <tuple>
    #  942: LIST_EXTEND         
    #  944: STORE_VAR            _var_var_18
    #  946: LOAD_FAST_LOAD_FAST 
    #  948: CONTAINS            
    #  952: IF_NOT               23
    #  956: LOAD_FAST_LOAD_FAST 
    #  958: CONTAINS            
    #  962: IF_NOT               18
    #  966: LOAD_CONST           True
    #  968: LOAD_CONST           '劫持DLL: '
    #  970: LOAD_VAR             _var_var_17
    #  972: FORMAT_SIMPLE       
    #  974: BUILD_STRING        
    #  976: BUILD_TUPLE          len=2
    #  978: SWAP                
    #  980: POP                 
    #  988: GOTO                 86
    #  990: CALL                 argc=1
    #  998: POP                 
    # 1000: RETURN              
    # 1002: LOAD_GLOBAL         
    # 1012: LOAD_VAR             _var_var_16
    # 1014: CALL                 argc=1
    # 1022: STORE_VAR            _var_var_19
    # 1024: LOAD_VAR             _var_var_19
    # 1026: TO_BOOL             
    # 1034: IF                   2
    # 1038: LOOP                 198
    # 1042: LOAD_CONST           True
    # 1044: LOAD_CONST           '可疑模块特征: '
    # 1046: LOAD_VAR             _var_var_17
    # 1048: FORMAT_SIMPLE       
    # 1050: BUILD_STRING        
    # 1052: BUILD_TUPLE          len=2
    # 1054: SWAP                
    # 1056: POP                 
    # 1064: GOTO                 48
    # 1066: CALL                 argc=1
    # 1074: POP                 
    # 1076: RETURN              
    # 1078: END_FOR             
    # 1080: POP                 
    # 1082: LOAD_CONST           <tuple>
    # 1090: GOTO                 35
    # 1098: POP                 
    # 1100: RETURN_CONST         <tuple>
    # 1102: TRY                 
    # 1104: LOAD_GLOBAL         
    # 1114: CHECK_EXC_MATCH     
    # 1116: IF_NOT               3
    # 1120: POP                 
    # 1122: POP_EXCEPT          
    # 1124: JUMP_BACKWARD_NO_INTERRUPT
    # 1126: RERAISE             
    # 1128: COPY                
    # 1130: POP_EXCEPT          
    # 1132: RERAISE             
    # 1134: TRY                 
    # 1136: LOAD_CONST           None
    # 1142: LOAD_CONST           bytes(20)
    # 1144: CALL                 argc=1
    # 1152: POP                 
    # 1154: RERAISE             
    # 1156: COPY                
    # 1158: POP_EXCEPT          
    # 1160: RERAISE             
    # 1162: LOAD_CONST           None
    # 1166: LOAD_CONST           bytes(20)
    # 1168: BUILD_TUPLE          len=1
    # 1172: POP                 
    # 1174: RETURN              
    pass  # See raw bytecode disassembly for control flow