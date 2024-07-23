import re

class Lexer:
    def __init__(self, codigo):
        self.codigo = codigo
        self.tokens = []
        # Atualizar a expressão regular para reconhecer identificadores com índices
        self.token_pattern = re.compile(r'\s*(?P<ident>[a-zA-Z_][a-zA-Z_0-9]*(?:\s*\[\s*\d+\s*\])*)|'
                                        r'(?P<int_constant>\d+)|'
                                        r'(?P<op>[+\-*/=])|'
                                        r'(?P<delim>[;,.(){}[\]])|'
                                        r'(?P<word>\b(?:def|int|return|exec)\b)|'
                                        r'(?P<space>\s+)|'
                                        r'(?P<error>.)')
        self.tokenize()

    def tokenize(self):
        pos = 0
        while pos < len(self.codigo):
            match = self.token_pattern.match(self.codigo, pos)
            if not match:
                raise ValueError(f'Caractere inesperado: {self.codigo[pos]}')

            tipo = match.lastgroup
            valor = match.group(tipo)
            if tipo == 'error':
                raise ValueError(f'Caractere inesperado: {valor}')
            if tipo == 'space':
                pos = match.end()
                continue
            elif tipo == 'ident' and valor in {'def', 'int', 'return', 'exec'}:
                self.tokens.append(('ident', valor))
            elif tipo != 'ident' and tipo != 'int_constant':
                self.tokens.append((tipo, valor))
            elif tipo == 'ident':
                self.tokens.append(('ident', valor))
            elif tipo == 'int_constant':
                self.tokens.append(('int_constant', valor))

            pos = match.end()

        self.tokens.append(('$', ''))

    def get_tokens(self):
        return self.tokens
