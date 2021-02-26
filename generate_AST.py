import sys
from ply import lex, yacc


def get_parser():

    tokens = (
        'ATOMIC',
        'NOT',
        'CONJUNCTION',
        'DISJUNCTION',
        'UNTIL',
        'RELEASE',
        'NEXT',
        'GLOBAL',
        'FINAL',
        'LPAREN',
        'RPAREN',
    )

    t_ATOMIC = r'[a-z]'
    t_NOT = r'¬'
    t_CONJUNCTION = r'∧'
    t_DISJUNCTION = r'∨'
    t_UNTIL = r'U'
    t_RELEASE = r'R'
    t_NEXT = r'X'
    t_GLOBAL = r'G'
    t_FINAL = r'F'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'


    # Define a rule so we can track line numbers
    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # A string containing ignored characters (spaces and tabs)
    t_ignore  = ' \t'

    # Error handling rule
    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    lexer = lex.lex()

    ##############################
    # yacc start

    def p_expression_group(p):
        'expression : LPAREN expression RPAREN'
        p[0] = p[2]

    def p_expression_atomic(p):
        '''expression : ATOMIC
        '''
        p[0] = ('atomic', p[1])


    def p_expression_sinop(p):
        '''expression : NOT expression
                        | NEXT expression
                        | GLOBAL expression
                        | FINAL expression
        '''
        p[0] = ('single-expression', p[1], p[2])


    def p_expression_binop(p):
        '''expression : expression CONJUNCTION expression
                        | expression DISJUNCTION expression
                        | expression UNTIL expression
                        | expression RELEASE expression
        '''
        p[0] = ('binary-expression', p[2], p[1], p[3])


    # Error rule for syntax errors
    def p_error(p):
        print("Syntax error in input!")

    precedence = (
        ('left', 'CONJUNCTION', 'DISJUNCTION'),
        ('left', 'UNTIL', 'RELEASE'),
        ('right', 'NEXT', 'FINAL', 'GLOBAL', 'NOT')
    )

    # Build the parser
    parser = yacc.yacc()

    return parser


# print(sys.argv[1])
s = 'G(bUc∧dUe)'
# s = 'GbUc∧dUe'
parser = get_parser()
result = parser.parse(s)
print(result)