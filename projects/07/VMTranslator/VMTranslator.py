#!/usr/bin/env python3

import argparse
import Parser
import CodeWriter


class VMTranslator():
    def __init__(self, file_name):
        self.parser = Parser.Parser(file_name)
        self.code_writer = CodeWriter.CodeWriter(file_name)

    def translate(self):
        self.parser.advance()
        while self.parser.has_more_commands():
            self.parser.advance()
            if self.parser.command_type() == self.parser.C_ARITHMETIC:
                self.code_writer.write_arithmetic(self.parser.command())
            elif self.parser.command_type() == self.parser.C_PUSH:
                self.code_writer.write_push(self.parser.segment(), self.parser.index())
            elif self.parser.command_type() == self.parser.C_POP:
                self.code_writer.write_pop(self.parser.segment(), self.parser.index())
            else:
                continue
        self.code_writer.close()
        

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='VMTranslator for the Jack Compiler. It converts .vm files to .asm files.')
    argparser.add_argument('file', help='a .vm file to translate to a .asm file')
    args = argparser.parse_args()

    vm_translator = VMTranslator(args.file)
    vm_translator.translate()
    

