DIRS = {"N": 1+0j, "E": 0+1j, "S": -1+0j, "W": 0-1j}
TURNS = {"R": 1j,  "L": -1j}


def solve(inp, way_point, move):
    states = {"boat": 0+0j, "way_point": way_point}
    for action, value in inp:
        if action in DIRS:
            states[move] += DIRS[action] * value
        elif action in TURNS:
            states["way_point"] *= TURNS[action] ** (value // 90)
        else:  # "F"
            states["boat"] += states["way_point"] * value
    return int(abs(states["boat"].real) + abs(states["boat"].imag))


example_data = """\
F10
N3
F7
R90
F11\
""".splitlines(keepends=False)


data = """\
F37
E1
S5
R180
S1
F37
L180
F38
S1
E2
L90
F48
N1
S5
E2
F53
E3
L90
F37
S3
F65
L90
F78
W3
S4
L90
F54
F61
E5
S1
L90
W2
L90
N3
F63
S3
E3
F83
R90
S2
W2
S5
E1
R90
W1
R90
W3
F52
E1
S4
E1
E4
R90
E4
F94
N5
F56
F17
L180
W2
S2
R90
S3
F49
R90
N4
E1
N3
F49
R90
S2
E3
F29
E2
R270
E5
L90
W3
F24
E2
S2
L90
F46
N1
F65
E1
N4
E5
R90
S4
L90
F51
R90
L180
W3
R90
L270
W4
S1
W1
L180
S1
F20
E5
L180
N2
F11
R180
N5
E2
N3
L90
F64
N3
W5
L90
W5
S2
F51
L90
F78
W1
R180
F84
R90
W3
L90
F59
S3
R90
R90
E2
F29
R90
F70
S1
F52
L90
N4
E1
F81
W3
F81
L90
E2
S1
F13
W2
N4
E1
F76
S2
F28
N4
W2
N1
R90
S5
R90
F81
W5
E1
L90
W3
F12
L90
W3
N5
F35
E4
L90
W4
S1
E1
F86
N2
E3
F29
L90
N2
F24
R90
F76
R90
E1
R90
E2
N1
F85
R90
N4
F62
R270
S3
W2
L90
N3
F36
R180
N5
F12
R90
F39
E3
N2
R90
W5
F5
W4
L90
F45
R180
F88
E3
F70
L90
N2
R90
F21
E3
R90
S4
F92
L90
N4
F87
N2
W5
N3
W1
S2
E2
L90
F26
W5
F96
W2
R180
E3
F71
R180
N1
E5
L90
S5
F73
S2
E3
R90
S5
F23
N5
R90
E4
L90
S5
R90
E1
N5
E4
F79
S1
F22
R90
F16
W4
F23
L180
F6
N5
F51
S3
R90
N1
R90
N2
F6
E4
F17
R90
F89
N3
R180
F42
F64
R180
W2
F88
E3
F54
E3
S3
E4
F66
L180
S5
W3
F47
E3
R90
S2
F41
R180
F83
N1
F8
W5
N5
W5
R180
F71
N5
F46
L90
N1
L90
W5
N4
F22
N2
L90
S4
F65
N3
W4
S5
S3
F93
E4
F78
R90
S5
W5
S1
F20
S1
W3
F14
L90
E5
S1
N2
F48
F38
W4
F61
N3
L270
W4
L180
F7
R180
S2
F3
L180
F10
E1
N2
F45
N1
W1
F48
W2
F53
R90
R90
F23
L180
F24
N4
L90
W1
S5
F5
L90
N1
F45
S4
W5
L180
E4
R90
S1
E4
S4
F16
N3
L90
F94
R90
N1
F4
S3
E4
S3
R270
F35
E4
N1
E4
R90
N5
F4
E4
F28
R90
S1
W4
R90
F36
R90
N2
S4
R90
F94
R270
F98
S2
F66
R90
F43
S4
W5
F1
R90
L90
W1
L90
F82
E4
F82
R90
N5
F49
F82
N5
F92
S2
R180
N1
F54
W2
R90
N4
S1
F3
R180
E1
F45
N4
E1
F67
F46
S1
S1
F5
R180
F78
N1
F22
L180
F37
E1
R90
W3
F59
E4
F16
L90
F90
W4
R90
E4
L180
N4
W5
F88
S2
L90
F58
W1
S1
W3
F75
E5
R90
E2
F73
R90
F1
R90
E5
L90
W2
F20
N1
E3
F98
S4
F95
S4
R90
W5
F65
W2
N4
R90
F57
W1
R90
N2
F65
N1
L90
N3
W2
F81
R90
F18
F48
E2
F56
R180
W2
S1
W1
F34
E2
F17
E4
N2
R90
W3
F63
N3
F74
R90
W1
N1
L90
S5
W5
F79
R270
F65
E1
S1
F8
L180
W2
R90
S5
W5
N4
R180
S5
L90
N1
W5
R90
F8
W3
F4
W2
S2
R90
N2
L90
S4
E5
F32
E2
R90
F52
R90
F85
E2
S1
F34
N5
F94
R90
N2
F81
R90
S3
W3
R90
E4
L90
N2
W5
N1
F98
F67
L90
N5
L180
R180
S1
R180
W4
L90
F56
E5
R90
F74
F18
F62
E4
F80
L180
S1
R90
F29
E1
N3
R270
W2
L90
N1
E5
F41
L90
N5
E5
F100
L180
F93
N2
E3
N5
E5
F81
N3
F6
E1
S2
F34
S5
E2
F50
W2
N3
F37
W1
N4
R180
S1
E3
S3
E5
R90
F29
W5
L90
F20
N5
N4
W2
R90
E5
F32
L90
F16
R180
W1
N4
F68
R180
F75
W1
S3
W4
S5
W2
S3
L270
F17
R180
W5
F84
E1
F38
L90
W4
F77
F7
L90
S1
L90
E2
N1
F36
N1
F91
N3
F38
S5
F58
E1
F83
L90
W1
L180
N4
W1
S2
L180
E1
F1
S2
F27
E3
R90
E1
R90
F17
E2
S4
R90
N5
F98
S2
L90
W3
R90
F19
R90
F66
W3
N1
E2
N1
L180
F33
W1
L90
F51
W3
N2
F48
E4
S4
L90
N3
E3
R90
S3
E4
R180
F97
F15
S1
R180
F81
S5
E2
L90
F49
W1
F30
W5
F30
W2
F40
W5
F55
N3
E4
S1
E3
N4
L90
F20
S5
F33
N4
E1
N5
L90
N4
W1
F7
E1
F85
W5
L180
W5
F40\
""".splitlines(keepends=False)
