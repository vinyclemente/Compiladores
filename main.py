from lexico import Lexer
from sintatico import Parser

def main():
    # Exemplo de código a ser analisado
    # codigo = '''
    # def func1(int A, int B) {
    #     int SM[2];
    #     SM[0] = A + B;
    #     SM[1] = A + B;
    #     return;
    # }

    # def func2(int X, int Y) {
    #     int SM[3];
    #     SM[0] = X + Y;
    #     SM[1] = SH - X;
    #     SM[2] = X * Y;
    #     return;
    # }

    # def func3(int P, int Q) {
    #     int M[4];
    #     M[0] = P + Q;
    #     M[1] = G - P;
    #     M[2] = P * Q;
    #     M[3] = W / Q;
    #     return;
    # }

    # def func4(int A, int B, int C) {
    #     int N[3];
    #     N[0] = A + B + C;
    #     N[1] = A * B;
    #     return;
    # }

    # def func5(int U, int V) {
    #     int O[2];
    #     O[0] = U + V;
    #     O[1] = H * U;
    #     return;
    # }

    # def func7(int K, int L) {
    #     int Y[4];
    #     Y[0] = K + L;
    #     Y[1] = K * L;
    #     Y[2] = G - L;
    #     return;
    # }

    # def func9(int A, int B) {
    #     int W[3];
    #     W[0] = A + B;
    #     return;
    # }

    # def principal() {
    #     int A;
    #     int B;
    #     int C;
    #     int D;
    #     int E;
    #     int F;
    #     int G;
    #     int H;
    #     int I;
    #     A = 4;
    #     B = 5;
    #     C = 6;
    #     D = 7;
    #     R = func1(A, B);
    #     E = func2(A, C);
    #     F = func3(B, D);
    #     G = func4(C, A, B);
    #     H = func5(D, B);
    #     I = func6(A, D);
    #     return;
    # }
    # '''

    nome_arquivo = input('Digite o nome do arquivo a ser analisado: ')
    arquivo = open(nome_arquivo, 'r', encoding='utf-8')
    codigo = arquivo.read()

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
