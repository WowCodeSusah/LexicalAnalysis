import re

token_specification = [
    ('NUMBER', r'\d+(\.\d*)?'),    # Integer or decimal number
    ('ID',     r'[A-Za-z_]\w*'),   # Identifiers
    ('ASSIGN', r'='),              # Assignment operator
    ('END',    r';'),              # Statement terminator
    ('OP',     r'[+\-*/><]'),        # Arithmetic operators
    ('LPAREN', r'\('),             # Left parenthesis
    ('RPAREN', r'\)'),             # Right parenthesis
    ('LBRACE', r'{'),              # Left brace
    ('RBRACE', r'}'),              # Right brace
    ('COMMA',  r','),              # Comma
    ('SKIP',   r'[ \t]+'),         # Skip spaces and tabs
    ('NEWLINE',r'\n'),             # Newline
    ('MISMATCH',r'.'),             # Any other character
]

token_re = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
token_regex = re.compile(token_re)

def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value.upper() in {'IF', 'ELSE', 'WHILE', 'RETURN', 'INT', 'FLOAT', 'CHAR'}:
            kind = value.upper()
        elif kind == 'SKIP' or kind == 'NEWLINE':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Unexpected character {value}')
        tokens.append((kind, value))
    return tokens


source_code = """
int x = 10;
if (x > 5) {
    return x;
}
"""

tokens = tokenize(source_code)
for token in tokens:
    print(token)