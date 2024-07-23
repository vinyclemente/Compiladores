from lexico import Lexer
from sintatico import Parser

def main():
    # Exemplo de código a ser analisado
    codigo = '''
    def func1 ( int A , int B )
    {
    int SM [2];
    SM [0] = A + B ;
    SM [1] = B * C ;
    return ;
    }

    def principal ()
    {
    int C ;
    int D ;
    int R ;
    C = 4 ;
    D = 5 ;
    R = func1 (C , D ) ;
    return ;
    }
    '''

    # Analisador léxico e sintático
    lexer = Lexer(codigo)
    tokens = lexer.get_tokens()
    print(f'Tokens: {tokens}')

    analisador = Parser(tokens)
    try:
        analisador.parse()
        print("Análise sintática concluída com sucesso!")
    except SyntaxError as e:
        print(f"Erro de sintaxe: {e}")

if __name__ == "__main__":
    main()
