## VM Translator

This is a Virtual Machine translator. It translates .vm code (bytecode) to the Hack Assembly language.

In this project I'm extending the VM Translator to allow branching and function calls.

#### Run
```
python VMTranslator.py test.asm
```

This will generate a `test.asm` file that could be run in the [CPUEmulator](../../../tools/).
