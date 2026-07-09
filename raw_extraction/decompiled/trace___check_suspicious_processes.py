# trace___check_suspicious_processes.py
# Function: _check_suspicious_processes | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def _check_suspicious_processes():
    """
    检查是否有可疑进程运行
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          sys
    #   38: LOAD_ATTR            psutil
    #   58: LOAD_CONST           'win32'
    #   60: COMPARE             
    #   64: IF_NOT               11
    #   70: LOAD_CONST           <tuple>
    #   78: GOTO                 338
    #   86: POP                 
    #   88: RETURN_CONST         <tuple>
    #   92: LOAD_CONST           0
    #   94: LOAD_CONST           None
    #   96: IMPORT               psutil
    #   98: STORE_VAR            _var_var_29
    #  100: LOAD_GLOBAL          name
    #  110: LOAD_ATTR            process_iter
    #  132: CALL                 argc=0
    #  140: STORE_VAR            _var_var_30
    #  142: LOAD_VAR             _var_var_29
    #  144: LOAD_ATTR            pid
    #  164: LOAD_VAR             _var_var_30
    #  166: CALL                 argc=1
    #  174: LOAD_ATTR            _VM_PROCESSES
    #  194: CALL                 argc=0
    #  202: LOAD_ATTR            AccessDenied
    #  222: CALL                 argc=0
    #  230: STORE_VAR            _var_var_31
    #  232: LOAD_VAR             _var_var_29
    #  234: LOAD_ATTR           
    #  254: LOAD_CONST           'name'
    #  256: LOAD_CONST           'pid'
    #  258: BUILD_LIST          
    #  260: CALL                 argc=1
    #  268: GET_ITER            
    #  270: FOR_ITER             155
    #  274: STORE_VAR            _var_var_32
    #  278: LOAD_VAR             _var_var_32
    #  280: LOAD_ATTR           
    #  300: LOAD_CONST           'name'
    #  302: BINARY_SUBSCR       
    #  306: LOAD_ATTR            AccessDenied
    #  326: CALL                 argc=0
    #  334: STORE_VAR            _var_var_33
    #  336: LOAD_VAR             _var_var_32
    #  338: LOAD_ATTR           
    #  358: LOAD_CONST           'pid'
    #  360: BINARY_SUBSCR       
    #  364: STORE_VAR            _var_var_34
    #  366: LOAD_FAST_LOAD_FAST 
    #  368: COMPARE             
    #  372: IF_NOT               2
    #  376: LOOP                 55
    #  380: LOAD_VAR             _var_var_33
    #  382: LOAD_CONST           'python.exe'
    #  384: COMPARE             
    #  388: IF_NOT               57
    #  394: LOAD_VAR             _var_var_29
    #  396: LOAD_ATTR            pid
    #  416: LOAD_VAR             _var_var_30
    #  418: CALL                 argc=1
    #  426: LOAD_ATTR           
    #  446: CALL                 argc=0
    #  454: STORE_VAR            _var_var_35
    #  456: LOAD_VAR             _var_var_35
    #  458: TO_BOOL             
    #  466: IF_NOT               18
    #  470: LOAD_VAR             _var_var_35
    #  472: LOAD_ATTR           
    #  492: LOAD_VAR             _var_var_34
    #  494: COMPARE             
    #  498: IF_NOT               2
    #  502: LOOP                 118
    #  506: LOAD_VAR             _var_var_33
    #  508: LOAD_GLOBAL         
    #  518: CONTAINS            
    #  522: IF_NOT               15
    #  526: LOAD_CONST           True
    #  528: LOAD_VAR             _var_var_33
    #  530: BUILD_TUPLE          len=2
    #  532: SWAP                
    #  534: POP                 
    #  542: GOTO                 106
    #  544: CALL                 argc=1
    #  552: POP                 
    #  554: RETURN              
    #  556: LOAD_VAR             _var_var_33
    #  558: LOAD_GLOBAL         
    #  568: CONTAINS            
    #  572: IF_NOT               2
    #  576: LOOP                 155
    #  580: LOOP                 157
    #  584: END_FOR             
    #  586: POP                 
    #  588: LOAD_CONST           <tuple>
    #  596: GOTO                 79
    #  604: POP                 
    #  606: RETURN_CONST         <tuple>
    #  608: TRY                 
    #  610: POP                 
    #  612: POP_EXCEPT          
    #  614: JUMP_BACKWARD_NO_INTERRUPT
    #  616: COPY                
    #  618: POP_EXCEPT          
    #  620: RERAISE             
    #  622: TRY                 
    #  624: LOAD_VAR             _var_var_29
    #  626: LOAD_ATTR           
    #  646: LOAD_VAR             _var_var_29
    #  648: LOAD_ATTR           
    #  668: BUILD_TUPLE          len=2
    #  670: CHECK_EXC_MATCH     
    #  672: IF_NOT               4
    #  676: POP                 
    #  678: POP_EXCEPT          
    #  680: LOOP                 207
    #  684: RERAISE             
    #  686: COPY                
    #  688: POP_EXCEPT          
    #  690: RERAISE             
    #  692: TRY                 
    #  694: LOAD_GLOBAL         
    #  704: CHECK_EXC_MATCH     
    #  706: IF_NOT               3
    #  710: POP                 
    #  712: POP_EXCEPT          
    #  714: JUMP_BACKWARD_NO_INTERRUPT
    #  716: POP                 
    #  718: POP_EXCEPT          
    #  720: JUMP_BACKWARD_NO_INTERRUPT
    #  722: COPY                
    #  724: POP_EXCEPT          
    #  726: RERAISE             
    #  728: TRY                 
    #  730: LOAD_CONST           None
    #  736: LOAD_CONST           bytes(20)
    #  738: CALL                 argc=1
    #  746: POP                 
    #  748: RERAISE             
    #  750: COPY                
    #  752: POP_EXCEPT          
    #  754: RERAISE             
    #  756: LOAD_CONST           None
    #  760: LOAD_CONST           bytes(20)
    #  762: BUILD_TUPLE          len=1
    #  766: POP                 
    #  768: RETURN              
    pass  # See raw bytecode disassembly for control flow