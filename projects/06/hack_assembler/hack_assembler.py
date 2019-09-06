#!/usr/bin/python
import argparse
import re

def dec_to_bin(decimal, length):
    return f'{decimal & (2 ** length - 1):b}'.rjust(16, '0')

dest_table = {''   :'000',
              'M'  :'001',
              'D'  :'010',
              'MD' :'011',
              'A'  :'100',
              'AM' :'101',
              'AD' :'110',
              'AMD':'111'}

jump_table = {''   :'000',
              'JGT':'001',
              'JEQ':'010',
              'JGE':'011',
              'JLT':'100',
              'JNE':'101',
              'JLE':'110',
              'JMP':'111'}

comp_table = {'0'  :'0101010', # Desde aca es a==0
              '1'  :'0111111',
              '-1' :'0111010',
              'D'  :'0001100',
              'A'  :'0110000',
              '!D' :'0001101',
              '!A' :'0110001',
              '-D' :'0001111',
              '-A' :'0110011',
              'D+1':'0011111',
              'A+1':'0110111',
              'D-1':'0001110',
              'A-1':'0110010',
              'D+A':'0000010',
              'D-A':'0010011',
              'A-D':'0000111',
              'D&A':'0000000',
              'D|A':'0010101',
              'M'  :'1110000', # Desde aca es a==1
              '!M' :'1110001',
              '-M' :'1110011',
              'M+1':'1110111',
              'M-1':'1110010',
              'D+M':'1000010',
              'D-M':'1010011',
              'M-D':'1000111',
              'D&M':'1000000',
              'D|M':'1010101'}

pre_defined = {'R0':'0',
               'R1':'1',
               'R2':'2',
               'R3':'3',
               'R4':'4',
               'R5':'5',
               'R6':'6',
               'R7':'7',
               'R8':'8',
               'R9':'9',
               'R10':'10',
               'R11':'11',
               'R12':'12',
               'R13':'13',
               'R14':'14',
               'R15':'15',
               'SCREEN':'16384',
               'KBD':'24576',
               'SP':'0',
               'LCL':'1',
               'ARG':'2',
               'THIS':'3',
               'THAT':'4'}

variables = {}

labels = {}

def search_labels(input_file):
    with open(input_file, 'r') as infile:
        current_line = 0
        for line in infile:
            line = line.strip()
            line = re.split(r'[\s].*', line)[0] # Remove whitespace and inline comments
            if line and '/' not in line:
                if '(' in line: 
                    label = re.search(r'[^\(].+[^\)]', line).group(0)
                    labels[label] = current_line
                else:
                    current_line += 1
    

def parse_file(input_file):
    output_file = input_file.split('.')[0] + '.hack'
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            binary = ''
            line = line.strip()
            line = re.split(r'[\s].*', line)[0]
            if line and '/' not in line:
                if '@' in line: # It's an A-instruction
                    value = line.split('@')[1]
                    if not value.isdigit():
                        if labels.get(value): # It's a label
                            value = labels.get(value)
                        elif pre_defined.get(value):
                            value = pre_defined.get(value)
                        elif variables.get(value):
                            value = variables.get(value)
                        else: # Add new variable
                            if not variables: 
                                variables[value] = 16
                                value = 16
                            else:
                                max_value = int(max(variables.values()))
                                variables[value] = max_value + 1
                                value = max_value + 1
                    binary = dec_to_bin(int(value), 16)
                elif '=' in line: # It's a C-instruction
                    dest, comp = line.split('=')
                    jump = ''
                    if ';' in comp:
                        comp, jump = comp.split(';')
                    binary = '111' + comp_table[comp] + dest_table[dest] + jump_table[jump]
                elif ';' in line: # Just a jump
                    comp, jump = line.split(';')
                    binary = '111' + comp_table[comp] + '000' + jump_table[jump]
                if '(' not in line:
                    print(binary, file=outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser( description='HACK Assembler. Transforms .asm files to .hack files' )
    parser.add_argument('file', help='.asm file to transform to a .hack file')
    args = parser.parse_args()

    search_labels(args.file)
    parse_file(args.file)
