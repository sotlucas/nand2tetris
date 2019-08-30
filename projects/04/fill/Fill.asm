// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
    
    @8191
    D=A
    @max
    M=D // max = 8191


(WAIT)
    @i
    M=0 // i = 0
    @SCREEN
    D=A
    @addr
    M=D // addr = SCREEN
    @KBD
    D=M
    @BLACKEN
    D;JNE // if KBD == 0 then goto BLACKEN
    @WHITEN
    0;JMP // else goto WHITEN

(BLACKEN)
    @i
    D=M
    @max
    D=D-M
    @WAIT
    D;JGT
    
    @addr
    A=M
    M=-1 // RAM[SCREEN + i] = -1
    @addr
    M=M+1

    @i
    M=M+1 // i = i + 1
     
    @BLACKEN
    0;JMP

(WHITEN)
    @i
    D=M
    @max
    D=D-M
    @WAIT
    D;JGT
    
    @addr
    A=M
    M=0 // RAM[SCREEN + i] = 0
    @addr
    M=M+1

    @i
    M=M+1 // i = i + 1
     
    @WHITEN
    0;JMP

(END)
    @END
    0;JMP
