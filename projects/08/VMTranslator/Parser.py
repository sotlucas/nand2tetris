#!/usr/bin/env python3

import re


class Parser():
    """
    Handles the parsing of a single .vm file, and encapsulates access to the
    input code. It reads VM commands, parses them, and provides convenient
    access to their components. In addition, it removes all white space and
    comments.

    A command is composed by three parts:
    <command> <segment> <index>
    i.e. push local 2

    If is an arithmetic command the segment and index part are not present
    i.e. add
    """

    # Command types
    C_ARITHMETIC = 0
    C_PUSH = 1
    C_POP = 2
    C_LABEL = 3
    C_GOTO = 4
    C_IF = 5
    C_FUNCTION = 6
    C_RETURN = 7
    C_CALL = 8

    def __init__(self, file_name):
        vm_file = open(file_name, 'r')
        self._lines = self._remove_empty_strings(self._remove_comments(vm_file.read().split('\n')))
        vm_file.close()

        for line in self._lines:
            print(line)

        self._lines.reverse()
        self._current_line = None

    def _remove_comments(self, lines):
        return [re.sub(r'//(.+)*', '', line) for line in lines]

    def _remove_empty_strings(self, str_list):
        return list(filter(None, str_list))

    def advance(self):
        self._current_line = self._lines.pop()

    def has_more_commands(self):
        return self._lines != []

    def _is_arithmetic(self, line):
        commands = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']
        for command in commands:
            if command in line:
                return True
        return False

    def _is_push(self, line):
        return ('push' in line)

    def _is_pop(self, line):
        return ('pop' in line)

    def _is_label(self, line):
        return ('label' in line)

    def _is_goto(self, line):
        return ('goto' in line)

    def _is_if(self, line):
        return ('if-goto' in line)

    def _is_function(self, line):
        return ('function' in line)

    def _is_return(self, line):
        return ('return' in line)

    def _is_call(self, line):
        return ('call' in line)

    def command_type(self):
        if self._is_call(self._current_line):
            return Parser.C_CALL
        elif self._is_return(self._current_line):
            return Parser.C_RETURN
        elif self._is_function(self._current_line):
            return Parser.C_FUNCTION
        elif self._is_if(self._current_line):
            return Parser.C_IF
        elif self._is_goto(self._current_line):
            return Parser.C_GOTO
        elif self._is_label(self._current_line):
            return Parser.C_LABEL
        elif self._is_arithmetic(self._current_line):
            return Parser.C_ARITHMETIC
        elif self._is_push(self._current_line):
            return Parser.C_PUSH
        elif self._is_pop(self._current_line):
            return Parser.C_POP
        else:
            return None

    def command(self):
        """
        Returns the command itself (push, pop, sub, add, etc.).
        :return: string
        """
        return self._current_line.split()[0]

    def arg1(self):
        """
        Returns the first argument of the current command. Should be called
        only if the current command is C_PUSH, C_POP, C_FUNCTION or C_CALL.
        Should not be called if the current command is C_RETURN.
        :return: string
        """
        return self._current_line.split()[1]

    def arg2(self):
        """
        Returns the second argument of the current command. Should be called
        only if the current command is C_PUSH, C_POP, C_FUNCTION or C_CALL.
        :return: int
        """
        return int(self._current_line.split()[2])
