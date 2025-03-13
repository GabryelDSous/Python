codigoBi1 = "01001101 01100101 00100000 01100100 01100101"
codigoBi2 = "01110011 01110101 01100001 00100000"
codigoBi3 = "01100010 01110101 01101110 01100100 01100001"
p1 = ''.join(chr(int(b,2)) for b in codigoBi1.split())
p2 = ''.join(chr(int(b,2)) for b in codigoBi2.split())
p3 = ''.join(chr(int(b,2)) for b in codigoBi3.split())
print(f"{p1}{p2}{p3}")