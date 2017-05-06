#!/usr/bin/env python
i = 1
print "-" * 50
while i <= 12:
    n = 1
    while n <= 12:
        print "%4d" % (i * n),
        n += 1
    print ""
    i += 1
print "-" * 50
