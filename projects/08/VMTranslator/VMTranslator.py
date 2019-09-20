#!/usr/bin/env python3

import argparse
import glob
import Parser
import CodeWriter
import sys


class VMTranslator():
    def __init__(self, outfilename):
        self.parser = None
        self.code_writer = CodeWriter.CodeWriter(outfilename)

    def change_file(self, filename):
        self.parser = Parser.Parser(filename)

    def translate(self):
        self.code_writer.write_init()
        while self.parser.has_more_commands():
            self.parser.advance()
            if self.parser.command_type() == self.parser.C_ARITHMETIC:
                self.code_writer.write_arithmetic(self.parser.command())
            elif self.parser.command_type() == self.parser.C_PUSH:
                self.code_writer.write_push(self.parser.arg1(), self.parser.arg2())
            elif self.parser.command_type() == self.parser.C_POP:
                self.code_writer.write_pop(self.parser.arg1(), self.parser.arg2())
            elif self.parser.command_type() == self.parser.C_LABEL:
                self.code_writer.write_label(self.parser.arg1())
            elif self.parser.command_type() == self.parser.C_GOTO:
                self.code_writer.write_goto(self.parser.arg1())
            elif self.parser.command_type() == self.parser.C_IF:
                self.code_writer.write_if(self.parser.arg1())
            elif self.parser.command_type() == self.parser.C_FUNCTION:
                self.code_writer.write_function(self.parser.arg1(), self.parser.arg2())
            elif self.parser.command_type() == self.parser.C_RETURN:
                self.code_writer.write_return()
            elif self.parser.command_type() == self.parser.C_CALL:
                self.code_writer.write_call(self.parser.arg1(), self.parser.arg2())
            else:
                continue

    def close(self):
        self.code_writer.close()
        

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='VMTranslator for the Hack platform. It converts .vm files to .asm files.')
    argparser.add_argument('src_path', help='Path for the .vm file/s to translate')
    args = argparser.parse_args()
    files = glob.glob(args.src_path + '/*.vm')

    vm_translator = VMTranslator(args.src_path)
    if files:
        for infile in files:
            vm_translator.change_file(infile)
            vm_translator.translate()
    else:
        vm_translator.change_file(args.src_path)
        vm_translator.translate()
    vm_translator.close()
