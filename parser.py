# Importaciones
import ply.lex as lex
import ply.yacc as yacc

# Definición de tokens
tokens = ['ABC', 'PIZQ', 'PDER', 'ENTER']

t_ABC = r'abc'
t_PIZQ = r'\('
t_PDER = r'\)'
t_ENTER = r'\n'

# Gramática para el lenguaje L = (^n abc )^n-1, donde n = 1, 2, 3, ...

# s -> e1 ENTER
# e1 -> PIZQ e2
# e2 -> e1 PDER | ABC

# Función para manejar errores léxicos
def t_error(t):
    print('Se tiene un error léxico.')

# Funciones para manejar las reglas de la gramática
def p_s(p):
    '''
    s : e1 ENTER
    '''
    
def p_e1(p):
    '''
    e1 : PIZQ e2
    '''

def p_e2(p):
    '''
    e2 : e1 PDER
       | ABC
    '''

# Función para manejar errores sintácticos
def p_error(p):
    print('La cadena ingresada no pertenece al lenguaje.')

# Función principal para manejar el parser
def parser(cadena):
    lexer = lex.lex()
    parser = yacc.yacc()
    cadena = cadena + '\n'
    parser.parse(cadena)
    if not parser.errorok:
        return 'La cadena ingresada no pertenece al lenguaje.'
    return 'La cadena ingresada pertenece al lenguaje.'