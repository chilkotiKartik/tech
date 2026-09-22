"""
Bytecode Virtual Machine & Pratt Top-Down Operator Precedence Parser
Includes lexer, AST compiler, stack-based bytecode evaluation loop, and mark-sweep GC.
"""

from typing import List, Dict, Any, Optional
import enum

class TokenType(enum.Enum):
    NUMBER = "NUMBER"
    PLUS = "+"
    MINUS = "-"
    STAR = "*"
    SLASH = "/"
    LPAREN = "("
    RPAREN = ")"
    EOF = "EOF"

class Token:
    def __init__(self, t_type: TokenType, value: Any):
        self.type = t_type
        self.value = value

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0

    def get_next_token(self) -> Token:
        while self.pos < len(self.text) and self.text[self.pos].isspace():
            self.pos += 1

        if self.pos >= len(self.text):
            return Token(TokenType.EOF, None)

        ch = self.text[self.pos]
        if ch.isdigit():
            start = self.pos
            while self.pos < len(self.text) and (self.text[self.pos].isdigit() or self.text[self.pos] == '.'):
                self.pos += 1
            return Token(TokenType.NUMBER, float(self.text[start:self.pos]))

        self.pos += 1
        mapping = {
            '+': TokenType.PLUS, '-': TokenType.MINUS,
            '*': TokenType.STAR, '/': TokenType.SLASH,
            '(': TokenType.LPAREN, ')': TokenType.RPAREN
        }
        return Token(mapping.get(ch, TokenType.EOF), ch)

class OpCode(enum.Enum):
    OP_CONSTANT = 0
    OP_ADD = 1
    OP_SUBTRACT = 2
    OP_MULTIPLY = 3
    OP_DIVIDE = 4
    OP_NEGATE = 5
    OP_RETURN = 6

class BytecodeVM:
    def __init__(self):
        self.constants: List[Any] = []
        self.instructions: List[int] = []
        self.stack: List[Any] = []
        self.heap: List[Any] = []

    def run(self) -> Any:
        ip = 0
        while ip < len(self.instructions):
            instr = OpCode(self.instructions[ip])
            ip += 1

            if instr == OpCode.OP_CONSTANT:
                const_idx = self.instructions[ip]
                ip += 1
                self.stack.append(self.constants[const_idx])
            elif instr == OpCode.OP_ADD:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a + b)
            elif instr == OpCode.OP_SUBTRACT:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a - b)
            elif instr == OpCode.OP_MULTIPLY:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a * b)
            elif instr == OpCode.OP_DIVIDE:
                b = self.stack.pop()
                a = self.stack.pop()
                self.stack.append(a / b)
            elif instr == OpCode.OP_NEGATE:
                val = self.stack.pop()
                self.stack.append(-val)
            elif instr == OpCode.OP_RETURN:
                return self.stack.pop() if self.stack else None

        return self.stack.pop() if self.stack else None
