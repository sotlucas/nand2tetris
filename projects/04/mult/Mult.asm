// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

    @R0
    D=M
    @a
    M=D
    @FINISH // if a = 0 then FINISH
    D;JEQ

    @R1
    D=M
    @b
    M=D
    @FINISH // if b = 0 then FINISH
    D;JEQ

    @i
    M=0 // i = 0
    
    @acum
    M=0 // acum = 0 

(LOOP)
    @i
    D=M
    @b
    D=D-M
    @FINISH
    D;JEQ // if i > b then FINISH
    
    @a
    D=M
    @acum
    M=M+D // acum = acum + a

    @i
    M=M+1 // i = i + 1
    
    @LOOP
    0;JMP // LOOP

(FINISH)
    @acum
    D=M
    @R2
    M=D // R2 = acum

(END)
    @END
    0;JMP
