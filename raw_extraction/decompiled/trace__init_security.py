# trace__init_security.py
# Function: init_security | File: <frozen security>
# Python 3.13 bytecode - no decompiler exists. Instructions below for manual analysis.

def init_security(server_url, machine_id):
    """
    初始化安全模块
    在程序启动时调用
    
    Args:
        server_url: 服务器地址（用于心跳验证）
        machine_id: 机器ID（用于心跳验证）
    """

    # --- Bytecode instructions ---
    #    4: LOAD_CONST           None
    #    8: LOAD_CONST           bytes(20)
    #   10: BUILD_TUPLE          len=1
    #   14: POP                 
    #   18: LOAD_CONST           None
    #   20: STORE_VAR            __assert_armored__
    #   28: LOAD_GLOBAL          init_time_check
    #   38: CALL                 argc=0
    #   46: POP                 
    #   48: LOAD_GLOBAL          sys
    #   58: CALL                 argc=0
    #   66: POP                 
    #   68: LOAD_GLOBAL          exit
    #   78: LOAD_GLOBAL          start_heartbeat
    #   88: LOAD_CONST           'frozen'
    #   90: LOAD_CONST           False
    #   92: CALL                 argc=3
    #  100: TO_BOOL             
    #  108: IF_NOT               61
    #  112: LOAD_GLOBAL         
    #  122: CALL                 argc=0
    #  130: TO_BOOL             
    #  138: IF                   22
    #  142: LOAD_GLOBAL          start_heartbeat
    #  152: LOAD_ATTR           
    #  174: LOAD_CONST           1
    #  176: CALL                 argc=1
    #  184: POP                 
    #  186: LOAD_VAR             server_url
    #  188: TO_BOOL             
    #  196: IF_NOT               17
    #  200: LOAD_VAR             machine_id
    #  202: TO_BOOL             
    #  210: IF_NOT               10
    #  214: LOAD_GLOBAL         
    #  224: LOAD_FAST_LOAD_FAST  machine_id
    #  226: LOAD_CONST           120
    #  228: LOAD_CONST           <tuple>
    #  232: POP                 
    #  234: LOAD_CONST           True
    #  242: GOTO                 19
    #  250: POP                 
    #  252: RETURN_CONST         True
    #  254: TRY                 
    #  256: LOAD_CONST           None
    #  262: LOAD_CONST           bytes(20)
    #  264: CALL                 argc=1
    #  272: POP                 
    #  274: RERAISE             
    #  276: COPY                
    #  278: POP_EXCEPT          
    #  280: RERAISE             
    #  282: LOAD_CONST           None
    #  286: LOAD_CONST           bytes(20)
    #  288: BUILD_TUPLE          len=1
    #  292: POP                 
    #  294: RETURN              
    pass  # See raw bytecode disassembly for control flow