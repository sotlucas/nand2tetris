// Program to move a square with the keyboard

    @SCREEN
    D=A
    @addr
    M=D

    @addr // addr = -1
    A=M
    M=-1
    
(LOOP)
    @KBD
    D=M
    @133
    D=D-A
    @MOVE
    D;JEQ
    @LOOP
    0;JMP

(MOVE)
    @32
    D=A
    @addr
    M=D+M
    @addr
    A=M
    M=-1
    @LOOP
    0;JMP
