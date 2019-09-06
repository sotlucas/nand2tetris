// Test file
// 1110011111010000
@var
D=D+1

@R15
0;JMP            // this is an inline comment

(STH)
    @i
    D;JEQ
    M=D|A;JMP // is this useful?¿

(LOOP)
    @24
    D=M
    @LOOP              // a comment // inside a comment
    D;JGT

(END)      // infinite loop
    @END
    0;JMP
