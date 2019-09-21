## VM Translator

This is a Virtual Machine translator. It translates .vm code (bytecode) to the Hack Assembly language.

In this project I'm extending the VM Translator to allow branching and function calls.

#### Run

You can run one single file at a time:
```
python VMTranslator.py test.vm
```

or a whole directory (this will merge all the .vm files into one single .asm file):
```
python VMTranslator.py test/
```

This will generate a `test.asm` file that could be run in the [CPUEmulator](../../../tools/).
