20 PRINT WUMPUS
30 C=1
40 W=20
45 B=13
46 P=7
50 IF C=1 THEN X=2
60 IF C=1 THEN Y=5
70 IF C=1 THEN Z=14
80 IF C=2 THEN X=1
90 IF C=2 THEN Y=3
100 IF C=2 THEN Z=12
110 IF C=3 THEN X=2
120 IF C=3 THEN Y=4
130 IF C=3 THEN Z=10
140 IF C=4 THEN X=3
150 IF C=4 THEN Y=5
160 IF C=4 THEN Z=8
170 IF C=5 THEN X=1
180 IF C=5 THEN Y=4
190 IF C=5 THEN Z=6
200 IF C=6 THEN X=5
210 IF C=6 THEN Y=7
220 IF C=6 THEN Z=15
230 IF C=7 THEN X=6
240 IF C=7 THEN Y=8
250 IF C=7 THEN Z=20
260 IF C=8 THEN X=4
270 IF C=8 THEN Y=7
280 IF C=8 THEN Z=9
290 IF C=9 THEN X=8
300 IF C=9 THEN Y=10
310 IF C=9 THEN Z=19
320 IF C=10 THEN X=3
330 IF C=10 THEN Y=9
340 IF C=10 THEN Z=11
350 IF C=11 THEN X=10
360 IF C=11 THEN Y=12
370 IF C=11 THEN Z=18
380 IF C=12 THEN X=2
390 IF C=12 THEN Y=11
400 IF C=12 THEN Z=13
410 IF C=13 THEN X=12
420 IF C=13 THEN Y=14
430 IF C=13 THEN Z=17
440 IF C=14 THEN X=1
450 IF C=14 THEN Y=13
460 IF C=14 THEN Z=15
470 IF C=15 THEN X=6
480 IF C=15 THEN Y=14
490 IF C=15 THEN Z=16
500 IF C=16 THEN X=15
510 IF C=16 THEN Y=17
520 IF C=16 THEN Z=20
530 IF C=17 THEN X=13
540 IF C=17 THEN Y=16
550 IF C=17 THEN Z=18
560 IF C=18 THEN X=11
570 IF C=18 THEN Y=17
580 IF C=18 THEN Z=19
590 IF C=19 THEN X=9
600 IF C=19 THEN Y=18
610 IF C=19 THEN Z=20
620 IF C=20 THEN X=7
630 IF C=20 THEN Y=16
640 IF C=20 THEN Z=19
650 IF W=X THEN GOTO 680
660 IF W=Y THEN GOTO 680
670 IF W=Z THEN GOTO 680
680 PRINT C, X, Y, Z
691 IF X=B THEN PRINT BAT
692 IF Y=B THEN PRINT BAT
693 IF Z=B THEN PRINT BAT ELSE PRINT NOBAT
701 IF X=P THEN PRINT PIT
702 IF Y=P THEN PRINT PIT
703 IF Z=P THEN PRINT PIT ELSE PRINT NOPIT
711 IF X=W THEN PRINT WUMP
712 IF Y=W THEN PRINT WUMP
713 IF Z=W THEN PRINT WUMP ELSE PRINT NOWUMP
720 PRINT MOVE
730 INPUT T
740 IF T=0 THEN GOTO 760
750 IF T=1 THEN GOTO 760 ELSE GOTO 730
760 INPUT M
770 IF M=X THEN GOTO 800
780 IF M=Y THEN GOTO 800
790 IF M=Z THEN GOTO 800 ELSE GOTO 760
800 IF T=0 THEN GOTO 840
810 IF W=M THEN GOTO 910
820 W=W-1
830 GOTO 850
840 C=M
850 IF C=W THEN GOTO 890
860 IF C=P THEN GOTO 890
870 IF C=B THEN C=10
880 GOTO 50
890 PRINT DEAD
900 GOTO 920
910 PRINT WIN
920 END