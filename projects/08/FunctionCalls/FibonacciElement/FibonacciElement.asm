@256
D=A
@SP
M=D
// call Sys.init 0
@Sys.init$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(Sys.init$ret.0)
// function Sys.init 0
(Sys.init)
@i
M=0
@0
D=A
@n
M=D
(Sys.init$LOOP)
@n
D=M
@i
D=D-M
@Sys.init$ENDLOOP
D;JEQ
@SP
A=M
M=0
@i
M=M+1
@SP
M=M+1
@Sys.init$LOOP
0;JMP
(Sys.init$ENDLOOP)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
@Main.fibonacci$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0;JMP
// function Main.fibonacci 0
(Main.fibonacci)
@i
M=0
@0
D=A
@n
M=D
(Main.fibonacci$LOOP)
@n
D=M
@i
D=D-M
@Main.fibonacci$ENDLOOP
D;JEQ
@SP
A=M
M=0
@i
M=M+1
@SP
M=M+1
@Main.fibonacci$LOOP
0;JMP
(Main.fibonacci$ENDLOOP)
// push argument 0
@0
D=A
@ARG
D=D+M
@addr
M=D
@addr
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D-M
@lt0
D;JGT
D=0
@lt.end0
0;JMP
(lt0)
D=-1
(lt.end0)
@SP
A=M
M=D
@SP
M=M+1
// if-goto IF_TRUE
@SP
M=M-1
A=M
D=M
@IF_TRUE
D;JNE
// goto IF_FALSE
@IF_FALSE
0;JMP
// label IF_TRUE
(IF_TRUE)
// push argument 0
@0
D=A
@ARG
D=D+M
@addr
M=D
@addr
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// return
@LCL
D=M
@endFrame
M=D
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
M=M+1
D=M
@SP
M=D
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
@retAddr
A=M
0;JMP
// label IF_FALSE
(IF_FALSE)
// push argument 0
@0
D=A
@ARG
D=D+M
@addr
M=D
@addr
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// call Main.fibonacci 1
@Main.fibonacci$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)
// push argument 0
@0
D=A
@ARG
D=D+M
@addr
M=D
@addr
A=M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
// call Main.fibonacci 1
@Main.fibonacci$ret.3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.3)
// add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// return
@LCL
D=M
@endFrame
M=D
@endFrame
D=M
@5
A=D-A
D=M
@retAddr
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
M=M+1
D=M
@SP
M=D
@endFrame
M=M-1
A=M
D=M
@THAT
M=D
@endFrame
M=M-1
A=M
D=M
@THIS
M=D
@endFrame
M=M-1
A=M
D=M
@ARG
M=D
@endFrame
M=M-1
A=M
D=M
@LCL
M=D
@retAddr
A=M
0;JMP
