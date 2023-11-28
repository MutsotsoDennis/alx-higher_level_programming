#!/usr/bin/python3
print(chr(90 - i) if i % 2 == 0 else chr(122 - i) for i in range(26))
