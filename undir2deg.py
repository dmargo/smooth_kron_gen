import sys
d = {}
with open(sys.argv[1]) as f:
    for line in f:
        s,t = line.strip().split()
        d[s] = d.get(s,0) + 1
        d[t] = d.get(t,0) + 1
for v in d.values():
    print v
