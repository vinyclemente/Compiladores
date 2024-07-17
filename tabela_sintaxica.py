TABELA_SINTAXICA = {
    'PROGRAM': {'def': ['FUNCLIST'], '$': []},
    'FUNCLIST': {'def': ['FUNCDEF', 'T6']},
    'FUNCDEF': {'def': ['def', 'ident', '(', 'PARAMLIST', ')', '{', 'STATELIST', '}']},
    'PARAMLIST': {')': [], 'int': ['int', 'ident', 'T7'], 'float': ['float', 'ident', 'T7'], 'string': ['string', 'ident', 'T7']},
    'STATEMENT': {'ident': ['ATRIBSTAT', ';'], '{': ['{', 'STATELIST', '}'], 'int': ['VARDECL', ';'], 'float': ['VARDECL', ';'], 'string': ['VARDECL', ';'], ';': [';'], 'break': ['break', ';'], 'print': ['PRINTSTAT', ';'], 'read': ['READSTAT', ';'], 'return': ['RETURNSTAT', ';'], 'if': ['IFSTAT'], 'for': ['FORSTAT']},
    'VARDECL': {'int': ['int', 'ident', 'T1'], 'float': ['float', 'ident', 'T1'], 'string': ['string', 'ident', 'T1']},
    'ATRIBSTAT': {'ident': ['LVALUE', '=', 'EXPRESSION']},
    'FUNCCALL': {'exec': ['exec', 'ident', '(', 'PARAMLISTCALL', ')']},
    'PARAMLISTCALL': {'ident': ['ident', 'T9'], ')': []},
    'PRINTSTAT': {'print': ['print', 'EXPRESSION']},
    'READSTAT': {'read': ['read', 'LVALUE']},
    'RETURNSTAT': {'return': ['return']},
    'IFSTAT': {'if': ['if', '(', 'EXPRESSION', ')', '{', 'STATELIST', '}', 'T10']},
    'FORSTAT': {'for': ['for', '(', 'ATRIBSTAT', ';', 'EXPRESSION', ';', 'ATRIBSTAT', ')', 'STATEMENT']},
    'STATELIST': {'ident': ['STATEMENT', 'T11'], '{': ['STATEMENT', 'T11'], 'int': ['STATEMENT', 'T11'], 'float': ['STATEMENT', 'T11'], 'string': ['STATEMENT', 'T11'], ';': ['STATEMENT', 'T11'], 'break': ['STATEMENT', 'T11'], 'print': ['STATEMENT', 'T11'], 'read': ['STATEMENT', 'T11'], 'return': ['STATEMENT', 'T11'], 'if': ['STATEMENT', 'T11'], 'for': ['STATEMENT', 'T11'], '}': []},
    'ALLOCEXPRESSION': {'new': ['new', 'T12']},
    'NUMEXPRESSION': {'ident': ['TERM', 'T3'], '(': ['TERM', 'T3'], 'int_constant': ['TERM', 'T3'], '+': ['TERM', 'T3'], '-': ['TERM', 'T3'], 'float_constant': ['TERM', 'T3'], 'string_constant': ['TERM', 'T3'], 'null': ['TERM', 'T3']},
    'EXPRESSION': {'ident': ['NUMEXPRESSION', 'T14'], '(': ['NUMEXPRESSION', 'T14'], 'int_constant': ['NUMEXPRESSION', 'T14'], '+': ['NUMEXPRESSION', 'T14'], '-': ['NUMEXPRESSION', 'T14'], 'float_constant': ['NUMEXPRESSION', 'T14'], 'string_constant': ['NUMEXPRESSION', 'T14'], 'null': ['NUMEXPRESSION', 'T14']},
    'TERM': {'ident': ['UNARYEXPR', 'T4'], '(': ['UNARYEXPR', 'T4'], 'int_constant': ['UNARYEXPR', 'T4'], '+': ['UNARYEXPR', 'T4'], '-': ['UNARYEXPR', 'T4'], 'float_constant': ['UNARYEXPR', 'T4'], 'string_constant': ['UNARYEXPR', 'T4'], 'null': ['UNARYEXPR', 'T4']},
    'UNARYEXPR': {'ident': ['FACTOR'], '(': ['FACTOR'], 'int_constant': ['FACTOR'], '+': ['+', 'FACTOR'], '-': ['-', 'FACTOR'], 'float_constant': ['FACTOR'], 'string_constant': ['FACTOR'], 'null': ['FACTOR']},
    'FACTOR': {'ident': ['LVALUE'], '(': ['(', 'NUMEXPRESSION', ')'], 'int_constant': ['int_constant'], 'float_constant': ['float_constant'], 'string_constant': ['string_constant'], 'null': ['null']},
    'LVALUE': {'ident': ['ident', 'T5']},
    'T1': {';': [], '[': ['[', 'int_constant', ']', 'T1'], '=': ['=', 'EXPRESSION']},
    'T2': {'[': ['[', 'NUMEXPRESSION', ']', 'T13']},
    'T3': {'ident': [], ',': [], ')': [], ';': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': ['+', 'TERM', 'T3'], '-': ['-', 'TERM', 'T3']},
    'T4': {'ident': [], ',': [], ')': [], ';': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': [], '-': [], '*': ['*', 'UNARYEXPR', 'T4'], '/': ['/', 'UNARYEXPR', 'T4'], '%': ['%', 'UNARYEXPR', 'T4']},
    'T5': {',': [], ')': [], ';': [], '[': ['[', 'NUMEXPRESSION', ']', 'T5'], '=': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': [], '-': [], '*': [], '/': [], '%': []},
    'T6': {'def': ['FUNCLIST'], '$': []},
    'T7': {',': [',', 'PARAMLIST'], ')': []},
    'T9': {',': [',', 'PARAMLISTCALL'], ')': []},
    'T10': {'else': ['else', 'STATEMENT'], 'ident': [], '{': [], 'int': [], 'float': [], 'string': [], ';': [], 'break': [], 'print': [], 'read': [], 'return': [], 'if': [], 'for': [], '}': []},
    'T11': {'ident': ['STATELIST'], '{': ['STATELIST'], 'int': ['STATELIST'], 'float': ['STATELIST'], 'string': ['STATELIST'], ';': ['STATELIST'], 'break': ['STATELIST'], 'print': ['STATELIST'], 'read': ['STATELIST'], 'return': ['STATELIST'], 'if': ['STATELIST'], 'for': ['STATELIST'], '}': []},
    'T12': {'int': ['PRIMITIVETYPE', 'T8'], 'float': ['PRIMITIVETYPE', 'T8'], 'string': ['PRIMITIVETYPE', 'T8'], 'ident': ['IDENTEXPRESSION', 'T8']},
    'T13': {',': [], ')': [], ';': [], '<': [], '>': [], '<=': [], '>=': [], '==': [], '!=': [], '+': [], '-': [], '*': [], '/': [], '%': []},
    'T14': {'ident': [], ',': [], ')': [], ';': [], '<': ['RELOP', 'NUMEXPRESSION'], '>': ['RELOP', 'NUMEXPRESSION'], '<=': ['RELOP', 'NUMEXPRESSION'], '>=': ['RELOP', 'NUMEXPRESSION'], '==': ['RELOP', 'NUMEXPRESSION'], '!=': ['RELOP', 'NUMEXPRESSION']}
}

# TABELA_SINTAXICA = {
#     'PROGRAM': {
#         'def': ['FUNCDEF', 'PROGRAM'],
#         '$': ['EPSILON']
#     },
#     'FUNCDEF': {
#         'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']
#     },
#     'PARLIST': {
#         'int': ['PARLIST_T1'],
#         'float': ['PARLIST_T1'],
#         'string': ['PARLIST_T1'],
#         ')': ['EPSILON']
#     },
#     'PARLIST_T1': {
#         ',': [',', 'TYPE', 'id', 'PARLIST_T1'],
#         ')': ['EPSILON']
#     },
#     'STMTLIST': {
#         'int': ['VARDECL', 'STMTLIST'],
#         'float': ['VARDECL', 'STMTLIST'],
#         'string': ['VARDECL', 'STMTLIST'],
#         'id': ['STMT', 'STMTLIST'],
#         'print': ['STMT', 'STMTLIST'],
#         'return': ['STMT', 'STMTLIST'],
#         'if': ['STMT', 'STMTLIST'],
#         '{': ['STMT', 'STMTLIST'],
#         '}': ['EPSILON'],
#         '$': ['EPSILON']
#     },
#     'VARDECL': {
#         'int': ['VARDECL_T', ';'],
#         'float': ['VARDECL_T', ';'],
#         'string': ['VARDECL_T', ';']
#     },
#     'VARDECL_T': {
#         'id': ['TYPE', '=', 'EXPR']
#     },
#     'TYPE': {
#         'int': ['int'],
#         'float': ['float'],
#         'string': ['string']
#     },
#     'STMT': {
#         'int': ['VARDECL'],
#         'float': ['VARDECL'],
#         'string': ['VARDECL'],
#         'id': ['ATRIBST', ';'],
#         'print': ['PRINTST', ';'],
#         'return': ['RETURNST', ';'],
#         'if': ['IFSTMT'],
#         '{': ['{', 'STMTLIST', '}'],
#         ';': [';']
#     },
#     'ATRIBST': {
#         'id': ['id', '=', 'EXPR']
#     },
#     'PRINTST': {
#         'print': ['print', 'EXPR']
#     },
#     'RETURNST': {
#         'return': ['return', 'EXPR']
#     },
#     'IFSTMT': {
#         'if': ['if', '(', 'EXPR', ')', 'STMT', 'else', 'STMT'],
#         'if_no_else': ['if', '(', 'EXPR', ')', 'STMT']
#     },
#     'EXPR': {
#         'id': ['ident'],
#         'ident': ['ident'],
#         'num': ['TERM', 'EXPR_T'],
#         '(': ['TERM', 'EXPR_T']
#     },
#     'EXPR_T': {
#         '+': ['+', 'TERM', 'EXPR_T'],
#         '-': ['-', 'TERM', 'EXPR_T'],
#         '<': ['<', 'TERM'],
#         '>': ['>', 'TERM'],
#         '==': ['==', 'TERM'],
#         ';': ['EPSILON'],
#         ')': ['EPSILON'],
#         ',': ['EPSILON']
#     },
#     'TERM': {
#         'id': ['FACTOR', 'TERM_T'],
#         'num': ['FACTOR', 'TERM_T'],
#         '(': ['FACTOR', 'TERM_T']
#     },
#     'TERM_T': {
#         '*': ['*', 'FACTOR', 'TERM_T'],
#         '/': ['/', 'FACTOR', 'TERM_T'],
#         '+': ['EPSILON'],
#         '-': ['EPSILON'],
#         '<': ['EPSILON'],
#         '>': ['EPSILON'],
#         '==': ['EPSILON'],
#         ';': ['EPSILON'],
#         ')': ['EPSILON'],
#         ',': ['EPSILON']
#     },
#     'FACTOR': {
#         'id': ['id'],
#         'num': ['num'],
#         '(': ['(', 'EXPR', ')']
#     }
# }



















# refaça o código acima utilizando a seguinte tabela como referencia:
# MAIN → STMT | FLIST | ε
# FLIST → FDEF FLIST | FDEF
# FDEF → def id(PARLIST){STMTLIST}
# PARLIST → int id, PARLIST | int id | ε
# STMT → int id;
# | ATRIBST;
# | PRINTST;
# | RETURNST;
# | IFSTMT
# | {STMTLIST}
# | ;
# ATRIBST → id = EXPR | id = FCALL
# FCALL → id(PARLISTCALL)
# PARLISTCALL → id, PARLISTCALL | id | ε
# PRINTST → print EXPR
# RETURNST → return
# IFSTMT → if(EXPR) STMT else STMT
# | if(EXPR) STMT
# STMTLIST → STMT STMTLIST | STMT
# EXPR → NUMEXPR < NUMEXPR
# | NUMEXPR > NUMEXPR
# | NUMEXPR == NUMEXPR
# | NUMEXPR
# NUMEXPR → NUMEXPR + TERM
# | NUMEXPR - TERM
# | TERM
# TERM → TERM * FACTOR | FACTOR
# FACTOR → num | (NUMEXPR) | id

# TABELA_SINTAXICA = {
#     'MAIN': {'def': ['FLIST'], 'id': ['STMT'], '$': []},
#     'FLIST': {'def': ['FDEF', 'FLIST'], 'id': ['FDEF']},
#     'FDEF': {'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']},
#     'PARLIST': {'int': ['int', 'id', 'T1'], ')': [], '$': []},
#     'STMT': {'int': ['int', 'id', ';'], 'id': ['ATRIBST', ';'], 'print': ['PRINTST'], 'return': ['RETURNST'], 'if': ['IFSTMT'], '{': ['{', 'STMTLIST', '}'], ';': [';']},
#     'ATRIBST': {'id': ['id', '=', 'T2']},
#     'FCALL': {'id': ['id', '(', 'PARLISTCALL', ')']},
#     'PARLISTCALL': {'id': ['id', 'T3'], ')': []},
#     'PRINTST': {'print': ['print', 'EXPR']},
#     'RETURNST': {'return': ['return']},
#     'IFSTMT': {'if': ['if', '(', 'EXPR', ')', 'STMT', 'else', 'STMT'], 'id': ['if', '(', 'EXPR', ')', 'STMT']},
#     'STMTLIST': {'int': ['STMT', 'STMTLIST'], 'id': ['STMT', 'STMTLIST'], 'print': ['STMT', 'STMTLIST'], 'return': ['STMT', 'STMTLIST'], 'if': ['STMT', 'STMTLIST'], '{': ['STMT', 'STMTLIST'], ';': ['STMT', 'STMTLIST']},
#     'EXPR': {'id': ['NUMEXPR', 'T4'], '(': ['NUMEXPR', 'T4'], 'num': ['NUMEXPR', 'T4']},
#     'NUMEXPR': {'id': ['TERM', 'T5'], '(': ['TERM', 'T5'], 'num': ['TERM', 'T5']},
#     'TERM': {'id': ['FACTOR', 'T6'], '(': ['FACTOR', 'T6'], 'num': ['FACTOR', 'T6']},
#     'FACTOR': {'num': ['num'], '(': ['(', 'NUMEXPR', ')'], 'id': ['id']},
#     'T1': {',': [',', 'PARLIST'], ')': []},
#     'T2': {'id': ['EXPR'], 'num': ['EXPR'], '(': ['EXPR']},
#     'T3': {',': [',', 'PARLISTCALL'], ')': []},
#     'T4': {'<': ['<', 'NUMEXPR'], '>': ['>', 'NUMEXPR'], '==': ['==', 'NUMEXPR'], '$': []},
#     'T5': {'+': ['+', 'TERM', 'T5'], '-': ['-', 'TERM', 'T5'], '<': [], '>': [], '==': [], ')': [], ';': []},
#     'T6': {'*': ['*', 'FACTOR', 'T6'], '$': []},
#     'T7': {'def': ['FUNCLIST'], '$': []}
# }