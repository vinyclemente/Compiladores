from collections import deque

class Parser:
    def __init__(self, tokens):
        self.tokens = deque(tokens)
        self.token = None
        self.next_token()

    def next_token(self):
        self.token = self.tokens.popleft() if self.tokens else ('$','')

    def match(self, expected_type):
        print(f'Esperado: {expected_type}, Encontrado: {self.token[0]}')
        if self.token[0] == expected_type:
            self.next_token()
        else:
            raise SyntaxError(f'Esperado {expected_type}, encontrado {self.token[0]}')

    def parse(self):
        self.program()
        if self.token[0] != '$':
            raise SyntaxError(f'Esperado $, encontrado {self.token[0]}')

    def program(self):
        while self.token[0] == 'ident' and self.token[1] == 'def':
            self.function_definition()
        if self.token[0] != '$':
            raise SyntaxError(f'Esperado $, encontrado {self.token[0]}')

    def function_definition(self):
        self.match('ident')  # def
        self.match('ident')  # nome da função
        self.match('delim')  # (
        if self.token[0] == 'ident' and self.token[1] == 'int':
            self.match('ident')  # int
            self.match('ident')  # variável
            while self.token[0] == 'delim' and self.token[1] == ',':
                self.match('delim')  # ,
                self.match('ident')  # int
                self.match('ident')  # variável
        self.match('delim')  # )
        self.match('delim')  # {
        self.declarations()
        self.statements()
        self.match('delim')  # }

    def declarations(self):
        while self.token[0] == 'ident' and self.token[1] == 'int':
            self.match('ident')  # int
            self.match('ident')  # variável
            if self.token[0] == 'op' and self.token[1] == '=':
                self.match('op')  # =
                self.expression()  # expressão para inicialização
            self.match('delim')  # ;
        # Permite declarações de variáveis, mas não exige

    def statements(self):
        while self.token[0] in {'ident', 'return', 'exec'}:
            if self.token[0] == 'ident':
                if self.token[1] in {'return', 'exec'}:
                    self.match('ident')  # return ou exec
                    self.match('delim')  # ;
                else:
                    self.assignment()
            else:
                self.match('ident')  # return ou exec
                self.match('delim')  # ;

    def assignment(self):
        self.match('ident')  # variável
        self.match('op')  # =

        # Processa a expressão após o =
        self.expression()

        self.match('delim')  # ; após a expressão

    def expression(self):
        self.operand()
        while self.token[0] == 'op' and self.token[1] in {'+', '-', '*', '/'}:
            self.match('op')  # operador
            self.operand()

    def operand(self):
        if self.token[0] == 'ident' or self.token[0] == 'int_constant':
            self.match(self.token[0])
        elif self.token[0] == 'delim' and self.token[1] in {'(', '[', ']'}:
            self.match('delim')
            if self.token[0] == 'ident' or self.token[0] == 'int_constant':
                self.match(self.token[0])
            self.match('delim')
        else:
            raise SyntaxError(f'Operando esperado, encontrado {self.token[0]}')
