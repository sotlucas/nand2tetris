#!/usr/bin/env python3

class CodeWriter():

    # Temp position in RAM
    TEMP = 5
    
    def __init__(self, file_name):
        self._file_name_final = file_name.split('.')[0]
        self._outfile = open(self._file_name_final + '.asm', 'w')
        self.segments = {'local':'LCL', 'argument':'ARG', 'this':'THIS', 'that':'THAT'}
        self._eq_number = 0
        self._gt_number = 0
        self._lt_number = 0

    # Writing operations
    def write_arithmetic(self, command):
        """
        Writes the asembly code that is the translation of the given
        arithmetic command.
        """
        self._outfile.write(f'// {command}\n') # For debugging purposes
        if command == 'add':
            self._add()
        elif command == 'sub':
            self._sub()
        elif command == 'neg':
            self._neg()
        elif command == 'and':
            self._and()
        elif command == 'or':
            self._or()
        elif command == 'not':
            self._not()
        elif command == 'eq':
            self._eq()
        elif command == 'gt':
            self._gt()
        elif command == 'lt':
            self._lt()

    def write_push(self, segment, index):
        """
        Writes the asembly code that is the translation of the given
        PUSH command.
        """
        self._outfile.write(f'// push {segment} {index}\n') # For debugging purposes
        if segment == 'constant':
            self._outfile.writelines(
                [f'@{index}\n',
                'D=A\n',
                '@SP\n',
                'A=M\n',
                'M=D\n',
                '@SP\n',
                'M=M+1\n']
            )
        elif segment == 'temp':
            self._outfile.writelines(
                [f'@{CodeWriter.TEMP + index}\n',
                'D=A\n',
                '@addr\n',
                'M=D\n',

                '@addr\n',
                'A=M\n',
                'D=M\n',
                '@SP\n',
                'A=M\n',
                'M=D\n',

                '@SP\n',
                'M=M+1\n']
            )
        elif segment == 'pointer':
            symbol = 'THAT' if index == 1 else 'THIS'
            self._outfile.writelines(
                [f'@{symbol}\n',
                'D=M\n',

                '@SP\n',
                'A=M\n',
                'M=D\n',

                '@SP\n',
                'M=M+1\n']
            )
        elif segment == 'static':
            self._outfile.writelines(
                [f'@{self._file_name_final}.{index}\n',
                'D=M\n',

                '@SP\n',
                'A=M\n',
                'M=D\n',

                '@SP\n',
                'M=M+1\n']
            )
        else:
            self._outfile.writelines(
                [f'@{index}\n',
                'D=A\n',
                f'@{self.segments[segment]}\n',
                'D=D+M\n',
                '@addr\n',
                'M=D\n',

                '@addr\n',
                'A=M\n',
                'D=M\n',
                '@SP\n',
                'A=M\n',
                'M=D\n',

                '@SP\n',
                'M=M+1\n']
            )

    def write_pop(self, segment, index):
        """
        Writes the asembly code that is the translation of the given
        POP command.
        """
        self._outfile.write(f'// pop {segment} {index}\n') # For debugging purposes
        if segment == 'temp':
            self._outfile.writelines(
                [f'@{CodeWriter.TEMP + index}\n',
                'D=A\n',
                '@addr\n',
                'M=D\n',

                '@SP\n',
                'M=M-1\n',

                '@SP\n',
                'A=M\n',
                'D=M\n',
                '@addr\n',
                'A=M\n',
                'M=D\n']
            )
        elif segment == 'pointer':
            symbol = 'THAT' if index == 1 else 'THIS'
            self._outfile.writelines(
                ['@SP\n',
                'M=M-1\n',
                'A=M\n',
                'D=M\n',
                f'@{symbol}\n',
                'M=D\n']
            )
        elif segment == 'static':
            self._outfile.writelines(
                ['@SP\n',
                'M=M-1\n',
                'A=M\n',
                'D=M\n',
                f'@{self._file_name_final}.{index}\n',
                'M=D\n']
            )
        else:
            self._outfile.writelines(
                [f'@{index}\n',
                'D=A\n',
                f'@{self.segments[segment]}\n',
                'D=D+M\n',
                '@addr\n',
                'M=D\n',

                '@SP\n',
                'M=M-1\n',

                '@SP\n',
                'A=M\n',
                'D=M\n',
                '@addr\n',
                'A=M\n',
                'M=D\n']
            )

    def write_label(self, label):
        """
        Writes the asembly code that effects the label command.
        """
        self._outfile.writelines(f'({label})\n')
        
    def write_goto(self, label):
        """
        Writes the asembly code that effects the goto command.
        """
        self._outfile.writelines(
            [f'@{label}\n',
            '0;JMP\n']
        )

    def write_if(self, label):
        """
        Writes the asembly code that effects the if-goto command.
        """
        self._outfile.writelines(
            [f'@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=M\n',
            f'@{label}\n',
            'D;JNE\n']
        )
        

    def close(self):
        self._outfile.close()

    # Arithmetic operations
    def _add(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',

            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',

            'A=M\n',
            'M=D+M\n',

            '@SP\n',
            'M=M+1\n']
        )

    def _sub(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',

            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',

            'A=M\n',
            'M=M-D\n',

            '@SP\n',
            'M=M+1\n']
        )

    def _neg(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',

            'A=M\n',
            'M=-M\n',

            '@SP\n',
            'M=M+1\n']
        )


    def _and(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',

            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',

            'A=M\n',
            'M=D&M\n',

            '@SP\n',
            'M=M+1\n']
        )

    def _or(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',

            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',

            'A=M\n',
            'M=D|M\n',

            '@SP\n',
            'M=M+1\n']
        )

    def _not(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',

            'A=M\n',
            'M=!M\n',

            '@SP\n',
            'M=M+1\n']
        )


    def _eq(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=D-M\n',

            f'@eq{self._eq_number}\n',
            'D;JEQ\n',
            'D=0\n',
            f'@eq.end{self._eq_number}\n',
            '0;JMP\n',

            f'(eq{self._eq_number})\n',
            'D=-1\n',
            f'(eq.end{self._eq_number})\n',
            '@SP\n',
            'A=M\n',
            'M=D\n',

            '@SP\n',
            'M=M+1\n']
        )
        self._eq_number += 1

    def _gt(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=D-M\n',

            f'@gt{self._gt_number}\n',
            'D;JLT\n',
            'D=0\n',
            f'@gt.end{self._gt_number}\n',
            '0;JMP\n',

            f'(gt{self._gt_number})\n',
            'D=-1\n',
            f'(gt.end{self._gt_number})\n',
            '@SP\n',
            'A=M\n',
            'M=D\n',

            '@SP\n',
            'M=M+1\n']
        )
        self._gt_number += 1

    def _lt(self):
        self._outfile.writelines(
            ['@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=M\n',

            '@SP\n',
            'M=M-1\n',
            'A=M\n',
            'D=D-M\n',

            f'@lt{self._lt_number}\n',
            'D;JGT\n',
            'D=0\n',
            f'@lt.end{self._lt_number}\n',
            '0;JMP\n',

            f'(lt{self._lt_number})\n',
            'D=-1\n',
            f'(lt.end{self._lt_number})\n',
            '@SP\n',
            'A=M\n',
            'M=D\n',

            '@SP\n',
            'M=M+1\n']
        )
        self._lt_number += 1
