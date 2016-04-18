# arg1 = 1c0111001f010100061a024b53535009181c
# arg2 = 686974207468652062756c6c277320657965
# output = 746865206b696420646f6e277420706c6179

import sys

def xor(arg1, arg2):
    hex1 = arg1.decode('hex')
    hex2 = arg2.decode('hex')
    temp = ""
    for index in xrange(len(hex1)):
        temp += chr(ord(hex1[index]) ^ ord(hex2[index]))

    return temp.encode('hex')

def main():
    print "##################################"
    print xor(sys.argv[1], sys.argv[2])
    print "##################################"

main()
