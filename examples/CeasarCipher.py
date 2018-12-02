#!/usr/bin/env pycal
Program := CeasarCipher
# CeasarCipher module written in pycal

og:string = `hal`
key:int   = 6

def encrypt(str, key) = 
    a := ord(`a`)
    return ''.join(chr((ord(char) - a + key) % 26 + a) for char in str.lower())

def decrypt(str, key) = 
    return encrypt(str, -key)

def solve(string, cur, lim) = 
    print(`Ceasar ${str(cur)}: ${encrypt(string, cur)}`)
    if cur != lim =
        solve(string, cur+1, lim)
    else =
        print(`done`)

Encrypted := encrypt(og, key)
Decrypted := decrypt(Encrypted, key)
print(`Original  --> ${og}`)
print(`Encrypted --> ${Encrypted}`)
print(`Decrypted --> ${Decrypted}`)
solve(og, 0, 26)