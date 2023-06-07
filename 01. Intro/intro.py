## ASCII
ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
print("".join(chr(o) for o in ords))

## HEX
byte = bytes.fromhex("63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d")
print(byte)

## BASE 64
import base64
byte = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
print(base64.b64encode(byte))

## BYTES AND BIG INTEGER
from Crypto.Util.number import *
print(long_to_bytes(11515195063862318899931685488813747395775516287289682636499965282714637259206269))

## XOR Starter
print("".join(chr(ord(x) ^ 13) for x in "label"))

## XOR PROPERTIES
def byte_xor(ba1, ba2):
    """ XOR two byte strings """
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key1 = bytes.fromhex(KEY1)

key2 = byte_xor(key1, bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"))
key3 = byte_xor(key2, bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"))
flag = byte_xor(key1, bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"))
flag = byte_xor(flag, key2)
flag = byte_xor(flag, key3)

print(flag.decode())

# atau
from pwn import xor
key1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
key1_2 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
key2_3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
key1_2_3_flag = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

key2 = xor(key1, key1_2)
key3 = xor(key2, key2_3)
key1_2_3 = xor(key3, key1_2)
flag = xor(key1_2_3_flag, key1_2_3)
print(flag.decode())

## FAVOURITE BYTE
from pwn import xor
text = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
byte = bytes.fromhex(text)
for i in range(256):
    # print(i, ": ", (xor(byte, i)).decode())
    flag = xor(byte, i).decode()
    if flag.startswith("crypto"):
        print(flag)

## YOU EITHER KNOW, XOR YOU DON'T
from pwn import xor
text = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
byte = bytes.fromhex(text)
partial_keys = xor(byte[:7], 'crypto{').decode() + 'y'
complete_keys = (partial_keys * (len(byte) // len(partial_keys) + 1))[:len(byte)]
ans = xor(complete_keys, byte)
print(ans.decode())

# atau
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) # oh, it says 'myXORke+y...'
print(xor(flag, 'myXORkey'.encode())) # try this? yay, it works! sometimes simpler is better