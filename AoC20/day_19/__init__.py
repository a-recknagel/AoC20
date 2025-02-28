
def parse_rules(inp):
    r = {}
    for line in inp.split("\n"):
        k, v = line.split(":")
        if v.startswith(' "'):
            r[int(k)] = v[2]
        else:
            r[int(k)] = [[*map(int, s.strip().split())] for s in v.split("|")]
    ret = [None] * (max(r.keys()) + 1)
    for k, v in sorted(r.items()):
        ret[k] = v
    return ret
    # return [v for k, v in sorted(r.items())]


class Idx:
    def __init__(self):
        self.val = 0

    def __add__(self, other):
        self.val += other
        return self


def match(rule_idx, rules, inp, current):
    if current.val >= len(inp):
        return False
    for option in rules[rule_idx]:
        if option in ["a", "b"]:
            if inp[current.val] == option:
                current += 1
                return True
            return False
        bak = current.val
        for r_i in option:
            if match(r_i, rules, inp, current):
                pass
            else:
                current.val = bak
                break
        else:
            return rule_idx != 0 or current.val >= len(inp)
    return False


def solve(content, rules):
    for row in content.split("\n"):
        if match(0, rules, row, Idx()):
            print(row)
            yield True


# example_data_c = """\
# 0: 2 1
# 1: 3 | 3 1
# 2: 3 4 | 3 2 4
# 3: "a"
# 4: "b"
#
# aaabbba
# aaabbbaa
# aaabba
# aba
# abaaa\
# """

example_data_c = """\
0: 1
1: 2 | 2 1
2: "a"

aa\
"""


example_data_a = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb\
"""

example_data_b = """\
42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba\
"""

data = """\
25: 6 54 | 28 122
52: 27 54 | 25 122
44: 118 122 | 30 54
37: 122 97 | 54 98
38: 122 22 | 54 3
77: 54 34 | 122 7
17: 122 124 | 54 47
1: 54 79 | 122 119
13: 122 121 | 54 15
29: 122 3 | 54 97
24: 54 97 | 122 62
80: 122 1 | 54 21
62: 54 54 | 122 54
5: 54 61 | 122 119
28: 54 57 | 122 36
101: 122 48 | 54 44
81: 120 54 | 14 122
14: 54 96 | 122 38
18: 40 122 | 76 54
27: 122 93 | 54 103
4: 123 122 | 90 54
65: 122 87 | 54 22
113: 54 | 122
23: 122 127 | 54 62
117: 71 54 | 119 122
53: 35 54 | 126 122
26: 122 52 | 54 108
125: 54 33 | 122 4
10: 74 122 | 53 54
84: 54 19 | 122 109
123: 122 114 | 54 115
42: 70 122 | 26 54
16: 122 39 | 54 98
63: 98 54 | 51 122
39: 54 122
76: 122 83 | 54 101
61: 122 3 | 54 39
50: 122 85 | 54 95
78: 22 122 | 3 54
114: 122 122
64: 122 122 | 122 54
40: 122 81 | 54 55
92: 127 122 | 97 54
119: 122 51
57: 98 54 | 114 122
3: 113 122 | 54 54
97: 122 113 | 54 122
7: 122 37 | 54 59
74: 54 46 | 122 56
2: 122 67 | 54 50
48: 43 122 | 65 54
124: 54 94 | 122 36
82: 54 98 | 122 64
93: 59 122 | 116 54
96: 115 122 | 97 54
98: 54 54
60: 51 54 | 22 122
72: 122 98 | 54 3
106: 39 54 | 39 122
41: 51 54 | 97 122
31: 18 54 | 69 122
91: 122 62 | 54 127
120: 105 122 | 19 54
56: 60 122 | 78 54
47: 16 122 | 91 54
88: 97 113
30: 22 122 | 115 54
71: 51 54 | 39 122
87: 122 122 | 54 122
21: 122 102 | 54 73
43: 122 22 | 54 127
35: 54 23 | 122 90
51: 113 113
90: 122 62 | 54 87
32: 54 127 | 122 97
115: 122 54 | 54 113
55: 54 84 | 122 89
73: 122 51 | 54 39
36: 22 54 | 114 122
68: 122 87 | 54 98
34: 118 54 | 32 122
95: 54 87
83: 122 117 | 54 20
33: 99 54 | 29 122
19: 122 127 | 54 98
46: 54 112 | 122 79
89: 54 72 | 122 66
110: 54 51 | 122 98
109: 64 54 | 22 122
9: 54 107 | 122 5
12: 54 80 | 122 45
104: 54 100 | 122 32
15: 75 122 | 63 54
69: 122 49 | 54 12
8: 42
75: 97 54 | 3 122
108: 122 77 | 54 125
103: 122 88 | 54 24
111: 3 54 | 39 122
70: 122 58 | 54 10
20: 122 105 | 54 68
0: 8 11
122: "a"
79: 62 54 | 22 122
102: 87 122 | 97 54
105: 98 54 | 98 122
49: 13 54 | 2 122
112: 54 39 | 122 62
58: 9 122 | 17 54
11: 42 31
107: 66 122 | 110 54
86: 54 106 | 122 82
99: 127 122 | 39 54
22: 54 122 | 122 54
118: 54 3 | 122 64
67: 122 59 | 54 111
126: 78 54 | 92 122
121: 54 41 | 122 38
66: 22 113
94: 54 39
6: 88 122 | 29 54
127: 122 54
116: 54 39 | 122 87
59: 54 51
85: 64 122 | 97 54
100: 98 122 | 62 54
54: "b"
45: 86 122 | 104 54

baaabbaabababaaababaaaaababbbabaabbbabba
baabbbbbaababbabaaabbabb
abbabbaabbabbbaabbabaaaaaabaabbbabbabbaa
bababbaababaabbaaabbabbb
baaabbaababbbbaabbbaaaba
bababbaababbbbbbaabbbbbb
ababababbabbaababbaabbbabbaabababaaababbaabaaaabbbbbaaaa
bbabbabaaaaabaaabbaabbab
abbbaabbababaabbbaabaaab
bababaaaabbbbbaaaabbbbbb
bbabaabbbbabbaabbabaabbaabbbbbaa
babaabaaabaaabbbbbbabbababaaabbbaaaaababbaabaabb
abaaaaaabaaabbbabbbaaabaababaabaaabababaaabaabba
aabbbaaaababbaaaaababbbb
babaabbaaaaabaaabaabbbabbababbbb
aabbabbbbbabaaaabbaabbab
abbabaaaaaaaaaaaabaabbbbaaabbbabaaabbabb
aaababbbaabbabbbaaabaaba
babbaabbbabaaaaaaabbbbabbabaabbababbbbabaababbba
abababbbabbabbaabaaabbbbababbabb
aaaaabbbbbbbaaaabbbaaabb
baababaaababaaabbaabaaabaabbabbabbaaaabb
babaabbbababaabaaababbbb
babaabaababbbbbbaabbaaba
babaabbbbabaaaabbbabbbaaaabaaaba
bbbabbbabbbbbaabbbbaabba
aaaaaababbabbbaaaaabbabb
bbabbbaaaababaaaababaaab
baabaababbbbbbbaaaaababb
abaababbaaaabbbaaabbabababaababbbbaabaab
abbbbbaaaababaabbbbababa
aabbabababbbbbaabbaaabba
abbaaababaabbbaaaabbaaaabbbabbabbababababaaaaaaabaabaabaaaaabaabbaabaaabaababbbbbbaabbaa
abbabaaaaaaaababbbbaabba
bbabbbaaaaabaababbbbbaaabbaaaabababbbabaabbabaababaaababbaabbbbbaababbbb
abbabaabbbbbaababbabbbbaabbaaaab
baaaabababaabbabbbbbbaabbaaaaabbbabbbbba
abbbabbbbbabaabbaaabaabb
aaaaababbbbabbaabaababba
baabbbbaaaaabbababababba
bbbabbaaabbaaaaaabaabbaa
babbaabbbabbaabbaaababababaaabab
ababaabbbaaabaaabaaaababbbaababaaababaabbbbbabbaaabbaaaa
aabbbabaaaaaabaaaaabbbaa
aabaaabbbbbbbbbaaabababa
abbaabababbbaabbbabbbbaaaaaaabbaaaababababaabbbabbbababa
aabbbabbabbaaaaabbbaaabb
bbbabbbabbaabbbbbbbaaaba
bbabababaababbaaababbaab
abbabbbabbbbbaaaabbabaaabbabaabaababbaaaaaabbabb
abbbbaabbabaaababbabaaab
aabbbbabaaaabbbaabbaabbbbbaabaaaaaaaaabaaaabbbaabaabaaab
abaaabababbbbaabbbbbaaba
bbbbbabbbabbbaaabbaababaaaabbabbaaaaaaabaaaaaaaaabbabaaaabbabbaabbbbaaabaaaabbba
baabaabaabbbabbbbbaabaaaaaabbbaa
bbbaaaaabbbbbbaabbaabaabbbbbbbbbabbababaaabbbbbb
bababaabbabaabbabbbbbabababaaabb
abaabbabaabaaabbbbaaabba
babbaababbabbaababbbbaaa
aabaababbabaababaababbbb
aaababbaabbaaaaababaaabaaabbbabbbaaabababbbabbbb
aaaaaabaabaabbbaabaaabaa
babaabababbabaaaaaaababb
bbabaabbabaabbbaaaaaaabb
abbabbbbbaaabbaaaaabaaab
ababaaaabbabbbaabababaaaaababaabbbaabbaaaababbbb
babaaaaaababbbbaaabbbaaaabbbbbabbbababba
bbbbabbbaababbabaabaabba
babbabbbbaaaaabbbabbbaaaabaabaaa
aabaaabbaabbbbabbbbababa
babbabbaaaababbbaabbaaaa
aabaababbaaabbbbbbbaabbb
babaaaabbabaabbaabaaabababbaabbbbaaaabbb
bbaabbbbbbabbbababbbabba
bbbabaabbaabaabababbbaaa
bbabaabbbaababbaaaabbbababbaaabaaaaabababaaaabbabbbaaabb
ababaabababaabbbbbababaa
abbabbaabbbbabababbababb
baabbbbaaababbabaaabbaaa
ababaabaababababaaabbabb
babbbbaaabaabbbababbaaaa
aaaabbabbabaaabbbbbaabbb
babbababaabbbababbabababbababbba
aabbbabbbaaabbaabbbabaaa
aaaabbabbbbabbaaaaabbbba
aaabbaabaaaaabaababaabbaababaaaababaabababbbaaaababbabaa
babbabbabbaabbaaaaabbbbb
bbababbbaaaabaaaabbaababbbaabaabaababbbabbbbbbaabbbaababbbbbbaabaaaaabbbaabbbbabaabbbbba
aabbbabaaaaaabbbbbaabbaababbaaabaabaabbbaabaabbb
bababaababbbbbaaabbaabab
baaaaaababaaaaabbabbbbba
aaababbabaaaababbbabbbaabbbbaabb
bbabbbaabaaaababbaaaaaba
abbbbbaaaabbbbababbbaaba
bbbababbabbbaabbbbbbabaa
abbbbabaabababbbbabaabaabbbaabba
bbbbbbbaabbaabaabbbbaaaa
bbbbbaaabaabaaaabaababbb
abaaababbbbbbaaaaabbbaab
abaaaaabbbbaaaabaababbaa
baaaababbbabaabbaaabaaab
aaababbbaaabbaababaaaaaabbaaaabaaaaabbaa
bbabbaabbaaaababbbaababaaabbabba
abaaaaabbbbaaaabbaaabaab
ababbbaaabbabbabbabbaaab
baaabbbbaaabbaababaabbabababbabb
abbabbbbbbaaabbbbbaaaabb
baabbbaaabbbabbbbababbaabbbbbbbbabbaaaabbbaababbbaaaaabbbabaabbaaababbbbbabaaaba
aababbaabbbbbababbbbabbabbababbaabbaabbaaaaaaaab
bbbbaaabaaabababbbabbababbbaabab
bbaabababbaaabbbaaaababb
abbbaabbbaabbaabbaababba
aabababbbabbbbaabaaaaaabbbaabbabbabbabbb
babbbbbabbbbbbbaaaaaabaaababbbbaaaabbaaa
babaabbaaabbabababbbbbbb
bbbaabaaabaaaaabbabaaabbaabaabaa
babbababaabaababababaabaababaaab
bbaaaaababbabbabbbbbaabb
babbbabbabaaaabbabaabaaa
babbababbaabbaabbbaabaab
abbabaabbaaabaaaaabbbabbbbabbabaaababbbbbabaabba
bababbaabaabbbabbbabbbbb
babbbbbbbaaaaabbbbababaa
baaaaaababbabaabbaaaaaba
aabababbbbaababaabbaabaaaaaabaaabaababba
abaaababbaabbabbaaaaababaabbaabbabbaaaabbbbaababababaaba
bbbabbbababbbabbbbbaabaaaababbaababaaaaabaababaaabbaabababbaabab
aaababbbbbabaabaababbaab
bbbbaaabbbbabbbabbbbaaaa
bbbabbababaaababaaaababb
baabbbbbbbabaababababaabaabbaaaaaabbabaa
abbabbaaaaaabbbaababbbbb
bbaabbbbbaaabbbbbbbaabba
bbbaaaababbabbabbaababab
baaabbaababaabaaabbbabab
ababaaaaaabaaabbabaabbaa
aababaabbababbaababbababbbaabababaabbabababbabaaaaababaaaabbbaabaabaabaa
bbaababababbabbaababaaab
aaabababababbbbabbbaabab
aabaaaaabaaaaabbaaaaababaaabbaabbaabbbabbaababab
bbaaabaaaaabaabbabaaaaba
babbbbabbabbbbaaabbaaaaaabbaabbababababb
abbbbaabaaababbbbabbabbabbaabaaabbbbbbbbbaaaabaabbaaabab
abbaaaaaabbbbabbabaabbbbaaaabababbbbaaba
bababaaaababbbbaaaababbaababbaaababaaababababbbbaaabbbba
baaabbbbabaaaaabbbbbbbbb
bbbbbabbaaaabaabababbbbb
ababaaaaaaababbabaaaabba
abbbbaabbbaabbbabaaababa
abaaababbabababaaabaabaa
baaaababaaabaaabbaabaaab
abbbbabababbabbaaabbbabbaabaaabaaabababaabbbabab
babaaabaaabaabababbaaaab
bbabbabbbabbaabbaaaaaabababababbbaabababaaabaababbaabbab
abbaabbbbabaabaaaaababaa
bbaabbaaaaababbaabbbaabbbbabbabaaabbbababbaabbaaaabbbbaa
bbbbababbbbababbbbbabbaaaaaabaabbbbbaabb
babbabbbabbabbaaabbbbbaa
abababbbbbabbabbabbaaabb
bbaabbbabbbbababbbabbaaa
baabbabbbbbabbabbbabbbba
aabaababbabbbabbbababbbb
babbababbbabaababbbaabba
aaaabbababbbbaabbbabbabbbabaaabbbaababaabaababbb
abbbaabbabbbbbaababababb
abbaabaabbbabbaaababbabb
baabbabbbaabaaaaaaaaabba
bbaabababaaaaaabababaabaabaaaaabaabbbbbbabbbbaaa
babaabababbaaaababaababababbbaab
aaaaabbbbbabaabbbaababab
bbbbbaababbbbaabaaabbaba
abbabbaaababaabbbbbaabaabbababab
bbbabaabababbbabaaaababa
baaabbbababbaababbbbabba
aaaabbaabbaabbbabbbbaaaa
aabaaabbaabbaabbabbbbbab
bbbababbbababbaaabaaabba
abbbbbaaabbaaaaaabbaabba
babaaaababbbbababaaaabbb
baaabbbaaaababbabbbaaaaa
bbbababbababbaabbbabbbbb
aabbbbababaabbbaabaaaaaa
abaababbaaaaabaababbababababbbaaabaaaababbbaabbb
babaaaababbaabaabbbbaaaa
baabbabbabbbabbbaabaababbabaaaaa
babbbbbbabbbabbbaaabbabbaabababaaabaaaba
abbabbbaabbaabaabbaaaaaa
bbbabbaababbbbaabaaababb
abaabbabaababbaabbaaaabb
baabbabbbabbbabbabbbaaab
abbbbaabbababbaababaaaaaaababbaabbababaa
ababababbbbbabababaaaaaa
bbbaaaabbabbaabbbabbbabbbbababaa
bbbbbbbaabbabbbbbbbabbbb
baaaaaababbabbbabbbbbbbaaaaaaabbbaaababb
bbabbbababbaaabaaabbabaaabbabbbabbabbbaaababbbab
bbabbaabbbaaabbbabaaabbbabaabbaabbaaabba
abaaaaabbbaababbababbbabbbbabaabaabbaabbbbababbbababbaaaabaaabaabbaaabaa
bbabaabbaabbaabbaabaabbb
baabbaaabbabababbaababab
bbaababaaabbbaaababbbaba
babaaabaabaabaabaaabbaabbaaabbaabaabaaba
babaabbabaababaabbbaaaaa
bababbaaabababababaaaaba
aaaabbabbabbaababbaabbab
abbabababaaabbbaaaabaabbbbaabaabbababbbbbbbbaaabbaaababbabbbbaaabbaaabab
bababaabaaaabaaaabababbbabbaaaba
aabbbbabaabbaabbbbbabaabbaababbabbaaabababbbbbba
baabbabaaabbbbabbbaaabaa
bbbbbababababaabaaababaa
aabaabbaabaaaaabbbbbabababbababb
baabbabbaabbbbabbaaababa
aababbaabbaabababbaabaab
baababaabbbabbbaabaabaab
aaaaabaaaaaaaabaaabaaaab
abbabbabaabbabbbabaabbbabaababaababbbbbbaaabbaaaabaaabaa
aabbbbabbbaabababaababbb
aabaababbababaaaabbaabba
aabbaabbbabaabaabbabbbbb
bababaaaabbbbbaabbbaabbb
babbbaaababbbaaaaaaabbbb
aabbbabaabbbabaabbbaabbb
aaaabbaabbbbabbbbbabaabaabaaabaa
abbabbaaabbabbbaabbbaaba
ababaabbbbabababaaabbaaa
aaabababaaaaabaaaaaaabbbbbbbabababbaaabaabbbaaab
baaaababbaababaaabababaa
aaaabbaaabbbabbbbaaaabba
abaabbbbbaaaaaabaababbaaababbaabaabababa
abbabbbbababbbaabaabbaaabbbbbbaabbbbabaa
bbabbabbbbabaabbabbbaaab
aabbbababbbaaaabaabaabbb
bbbabaabbaaabbbbbaabaabb
ababaabaaaaaababaaabbaaa
baaaaaabbabbabbaabbbaaab
bbabaabaababaaaaabbabaaaabababba
aabbbaaaaaabbaabbbabbaabbaabaaaa
abaaabbbbbaaabbbbaaabbab
bbabbabbabaaabbbbabbbbbbabbbbbbaababaaaaabbbbbabaaababbabbbabaababaabbbbabbabbab
babaabaababababaaaabbbba
bbaabaaababbbbbbbaabaabb
baabbbabababaaaaaabbbbaabbbaabab
abbbaaaababaabbabaabbbabbabbaaabaaabbaababbbbaaa
abbbabaabaababaaabbaaaab
ababababaabbbbabbbbbbbabbbbabbbaaaaaaabbbaabbabaabaaaabb
abaaabbbabaabbababbaabaaaaaabbbaaaabbbba
baaaaabbababababbaaabbab
babaaabaaabbbaaabaaabbaa
babbbabbbabaabaabbbbbbbb
aabbbabbabaaababaaabbabb
bbaabbaaaaababbaaabbbaab
aabbbbabbbbabbbaaabaaaab
abaabbbaababababbabaaabbbabbbaba
abbaaaaabbabbbabbbaaabba
aabaababbaabbabbabbaabba
bbabbabbbabbbbaabaababba
bbabaabbbbabaabbbbbbaaaa
abbbbabaabbbaabbaaababbaabbbabbaaaaababb
bbaaabbbbabaabbaabbbbbbb
abaaaabababbaaababbbbbbaababbaab
abaabbbbababaaaabbbaaabb
aaabaabbaababbbbbbbaaaaaabbbaaba
aaaaababbaabbaabbabbabbb
aaaaaaabaabababbbbbaaaaa
bbbbbaaaababaaaaaaabbaba
ababbaaababbbaaaaaabbbba
babaabbbbbabababbaabaaab
aabbbababbbabaabaabbaaab
abbbabaaabbbaabbabbaabba
baabbaababaabbabaabaaaab
baabbabbaabaababbaababbb
bbbaaaabaabbbaaaaaaaaaaabaaabbbaabbaaaaaabbbaababaabababababbaabaaabbbab
baabbabaaaaabbaaabbbabba
babaaabbabbbaabbabbababa
bbabbabbaaababbbbbbaaabb
aaaaababbabababaaaaababa
babaabbbbbbbbbbababbbbbbbbbaaaabaababaaa
aaabababaababbaabaaababa
ababaabbbabaabaabbaaaaaa
aaaabaaaabbabaaababaabaabababaabbaabbbbbaabbbbba
baaaaaabbabaabaabbaababb
aaabababaaabababaabaabba
abbabaaaabbabbbbbbbbbabbaaaaabab
bababaaaaababbabbbbbbbbb
ababbaaabbbbababbaaaaaba
ababaaaabbbaabaabbaaabaa
baaabbaabbbaababbaabaaabaaaaabababaabaaabababaaa
aaabbaabbaabbabbbbbababbabaaaababaaabaab
bbbbbaaabbaabbaababababb
aabbbbabaaaaabbbbaabaabb
abbabbaaaabbaabaaaaababbabbabbbaabbbbbbaabbabaaababbaabaaabbabab
abbabbababbbbababbbaabaabbbaaababbbaaabb
bababbaaabaabbabababaaaaabbbabbbaaaaabbb
babbaabaaabbaabbbbaaabaa
ababbaaababababaabababbbbbaababaabbbbbbb
aababaabbbabbaabababababbbbabbbaaaabaaabaaabbabb
baabaaaabababaaaababbbbb
bbbbabbbabaaabbbbbbababa
bbabbbaaaabbbaaabaababbb
bbbabbabbaabbabbbaababbb
baabaabaaaaaababaabaaaab
aabaabbaabaabbbbaaaabaaabbaababbbbbababbbabbbababaaabaabbaabbaabababaaab
babbababbbbababbabbbbbaaaaabbbaa
bbaabbbaaabaaabbbaababba
bbabbbabbbbabbbabbbbaaababbabaaaababbaabaaabaabbabaaabaa
abbaabbbabbbbabbbaaabbaaaabaabba
baaaaabbbabaaabababaaabbbabababaaababaaabaaaabbaabbaaababababbbaabbbbaaa
babbbaaabaaabbbbbbababba
aabbbbabbaabaaaababbabbb
baabbbbababbbbbbbbbbaaba
baabbbabbbaabaaababbaabbabbbababbbabaaab
bbabbbababbabbbbababbaaabababbbbabaabbaa
aaabababbbbbababaabababbbbbabbbbbabbbaba
bbbbabbbbaabbbabbababaaabbbaaabaabbababb
ababbbbaababbbabbbababba
abbaaaaabaabaaaabbbbaaba
aaababababaabbabbbbbbaaaaaaababa
bbbabbbabaaabbbbbbabbaabbbbabaaa
bababaabbabbbabbaaabbbaa
abbbbabbaaaaabbbbababababbbbabbbaaaaabaaaabbaaaa
bbabbbaaaabaaabbaaaabbaabbabaaab
abbabaaaaaaaaaaaaaabbabb
babbbabbbbabaabaabaaaaba
babbaabaabaaabbbbbbbbbaa
ababbbbabbbbabbbbababaaaabbaaabbbbbaabba
aabaababababaabbbbbaaaaa
abbbbbaaabbbbabbaaaababa
aaabaaabaabbbaabaabababaaaabaaba
babbbabbbbaabaaabababbbbbabbababbaabaabb
babaabbbbbbabbabaaaabbbaabaaabaaaabaabba
bababaabbabaababbabbbabbbbbbababbabbaaaaaabbabaa
babaaaabaababaabbbbaabba
bbaabbbbbaaabbbaaabbbbabbbaaaaabbabbabbababbabaabaaabababbabbbba
baabbaabbbabbababbbabaaa
aaaaaaaaababbbababababbbbbabaaaabaaaaababaabbbbb
aaaabaaabaabbbbbbbabbbabbabbabaabbbbaaabaaaabbbbbabaabaa
aabaabababbbaabbbbabaabbbbaabababbabbabaaaabaabb
aabaababbbabaabababbbbab
bbaabbbabbbabbbabbabbbba
bbaaaaabaaaabbaaaaaaabba
bbaaaaabaababbaababbbabbabbabbaa
aaabaabbbabaabaaaaabbbabaabbbbbabbbaabaa
aaabbbaabbbbaaabababbbbbabbbbbbbbbbabbbaabbabbbbaaaaaababbbbabbaabbabbaaaababbbb
aababaabaabbababbababbba
babaaaaaaaaaaaabaabaabba
aaabbaabbabbaabbbaabbbbbaabbaaba
aaababbabbabbabbababbbbb
abaaabbbbbaabaaaabbaaaba
bbaababaababbbabaabbbaab
abbbaabbbaaabbbabaabbbbbaaaaaaabbaaaaabbbbbbabaaabbaaaba
babaaaabbabaaaaababbabaa
bbbbaaababbbbaabababbbbb
abbababbaabaababbbaaaaabaabaabbbbabbabaababababaaaaaabbababbabbbbabbaaaabbbbabaa
babaaababbabaaaabbaaaaba
bbabbabaabbbbababbbaaabb
bbaababaaaaabbbaaaabbaaa
babaaaaaaabaababbabbabbaabababbbaaabbbaaaabbbbbabbbbaaaa
babaabbababaaabbbaaaabbb
aabaababbabbbabababbbbaabaaabaaaaaabbababbbabaaaabaaaaabaaaababaaabbbaaabbaaabbb
abbbabaabbbaaaabaaabaabb
bbbbbbbaaaabababaabbbbbb
ababaaaabbababababbaaabb
abbabbabbabbaabbbaaaaabbaabababa
bbabbabaababbbabaaaababb
babbabbababaaabbabbaaaba
aabbaaababbaaabbbbaabaabbbbabbbaaabbbbababbbabbaaabaaaabaaaabaabaabbbaab
bbbbbbbaaabbbabbbbaaaabb
bbabbaabbbbaabaabbbaaaaa
bbbabaabbaabbaaabaaabaaabbbbbbbb
aaabababbaabbbbaaababbbb
abbbbbbbabaaaaaaabbbbababbababaa
bbbaaaabaabaaaaabbaabbab
bbbbabbbaaaababbaabaaaab
bbaaabbbababbbabbbbbabaa
aaaabbaaabaababbbbabbabbbbbbbaaaabbbbbba
aabbbabbaaaaabbbbaaabaab
abbabbbbbaaaaaabaaabbaaa
baaaabababbbbaabaababaaaabaaabbbbbbaaaababbababa
bbbbabbbbbbbabbbbabbabbb
abbabaaaaabbaabbabaaaaaa
abbabbaaaababbaaababaababbbaabbbabbaaaab
abbaabaaaaaaabaaaaabbbaa
bbbaaaabbaabaabaaabababa
bbbaababbbbabaaabbbabaabaabababa
baabaababbabababbbbaaaaa
baaaabababbaabbbbaabbbabbbbaabab
baabbbbaababbaaaabbaabbb
babbbbbbabbbbabbabbabbabaabaaabbaaabbbab
ababaabbbabbaabbabaababbbbbbbaba
baabbabbaaabababbaabaabb
ababababbbabbbabbbababaa
abbaababaabbbbbabbaaabbabbabaaab
babbbbaaababbbabbbababba
abababbbabaaababaabbbbbbbbabbbbbbaaaabbbaabaaababababbba
aabbaabbbabaabbbbabbbbab
baabbbbabbbbabbbbaaababa
aaababbbbbbabbaabbbaaabb
bbbaaababaabaaabaababbbabaaaaabaaaabbbaa
baaabaabbabbaaabbaaababa
bbabaabbaababaaaababbbbb
ababbbbababbabbababaabaaaaaaaaababababbbaabbbaab
bbbbbabaabbbaabbaaaaabba
aaabababbbabbaabbbaabaab
bbabbabbbabaabbabaababbb
aaaaaaababbabbabbabbabaa
abbabaaaaaaaaaaaababbbbb
babaababbaabbabbabbabbaabababbbaabaabbaa
aabbbbaaaababbbbabababbabbbababa
bbbabbaabbabaaaaaaabaaaa
bbabbabaabbaaaabbbaaaaaa
bbaabaaabbabaaaabbbbaabb
bbabbaababbabbaaabbbabbbababbaab
bbbbababbabbaabbaabbaaab
aaaabbababbabaaababbbbbbbbbbbababbbababbabbbaabaaaabbaba
abbbaaaababbbbbaaaabababababbaabaabbbbaabaabaabbbabababa
bbbbabbbbbbbabbbbbbbbbab
bbabababbbabaaaababababb
abbabaaaaaaabbbaaaabbbbb
baababaaabababbbbabbaaaa
bbabbabbbabbabbaabaaabba
aaabababbabaabbaaaabbbbb
abaaababbaabbbbaaaaabbaaaaaabaaabbabbbabbbabbbbb
bbaaabbbbbbababbabababba
bbbbaaabbbabbbabbabaaabbbabaabaaaaaaababbabababbbbbbabaababbabbb
babbbabbbaaabbabbbabaaabababbaba
bbbabbbbbbabbabbaababbbb
baaabaaabbaabbaabaaabbabbababbab
bbabaaaaabbabbaaabbabaab
abbaabaabaaaaabbbbbaabba
aabbbbbaaaabbbbaabaaabbbbbaaabbaaababbbaaabbbaababababbaaabbbaabbbabaaab
bbbabbbaabbbbababaaabbabaabaabbbbababbaaaaaaabbbaaabbbabaababbaabbaaabaaabababba
aaaaababbbbbbaaaabaababbabbbbabaaaabbaabaabaabbabbabbbbbaaaaabba
babbabbabaabbbababaaabaa
aabaaaaabbbbaaabababbaab
babaaabbbabaabbbaaabaaba
bababaaabbaabababbbbaabb
aabbbababbaabbbaabbababb
babaabaabbbbaabbaaaaabababaaababaababbabbabbabbaabbbbbaababbaabbaaaabaaa
aabbbbabaaababbabbaaaaaa
ababaabbabaababbbbbaaaaa
aaababbbbaabbbabbbabaabbaabbbabaabbaababaaabbaaa
bbbbaaabbbaabababaababbb
ababababaabababbbbababaa
baaabaaaabaaabbbabbbbbaababaaabaabaaaabaaabaabaaaaabaaaa
abaabbbabaaabaaaababbbababbbbbaaaabaabaa
bbaabaaabbbbbbbbbaaabaaababbbbbabababbaabaaaaaba
babbababaabaaaaaaabaabba
bbbabaaaabbaabbbaabaabbbaaabababaaababaabbbabaaabbbbaababaaaaaabbabbbaba
aabaaaaaaabbabbbaabbbbba
abbbbababbabaaaaaaaaaaaaaabbbaaababbabbabbbbabaa
aaababbabababaaaabbaabba
bbbbabababbabbbaabbbabab
aaababbbbaabaaaabbbaabbb
bbbaaaabaabaaabbbbaaabab
ababbbaabaabaabababbbbab
babaabababbabbbbbbbbabba
abbbabbbabaaabbaaaaaabbbabababbabaaaaaab
baaabbbbbababaababbbbbbb
aabbbaaaaabaaaaaabbababb
aaaaabaaabababababbbbaaa
ababaabbaaaabbababaaaaaa
bbbaaaabaaaabbaabaaabaab
baaabbbbbbbabbaaabbaaaaababbabbbbbbaabbbbbbabbbabbbaaaab
bbbbbaabaaaabbabaaaaaaaabbbabbbb
bbbaabaaaabbabbbabbaabaaaaabbbbbabbababbaabbbababbababab
bbabbabbbaabbaaaabbabbaaabbbabaababbabbaaaabbbab
baaabbbababbbabbaabaabbb
aaaabbaababababaaabbbbbb
abbbbbaabbbabaabbababbba
bbbbbbbababbaabbabaaabba
abbbaabbbabaababbbaaaaabaabbbbaa
babbaabaabbbbababaaabbab
baaabbbabaabbbbabbbbaaabaaabbabb
aabbbabbabbbbabbababaabababaabaabbaaabaabbbbbbbbaabababa
bbbaabaaababaaaabbaabbaaaabbbabaabababaa
bababbaababbababaabbabaa\
"""
