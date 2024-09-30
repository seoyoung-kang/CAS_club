S = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

def sbox(input):
    return S[input]

def permutation(list):
    per_list = [list[4], list[5], list[0], list[1], list[6], list[7], list[2], list[3]]
    return per_list 

def input_to_binary_list(input):

    binary_str = format(input, '08b')
    binary_list = [int(bit) for bit in binary_str]
    
    return binary_list

def encryption(plaintext, key):
    bin_list = input_to_binary_list(input)
    per_list = permutation(bin_list)
    left = per_list[0]*8 + per_list[1]*4 + per_list[2]*2 + per_list[3]
    right = per_list[4]*8 + per_list[5]*4 + per_list[6]*2 + per_list[7]
    out_sbox = sbox(left)*16+sbox(right)
    cipher = key ^ out_sbox
    return cipher

ciphertext = encryption(0x6b,0xff)
print(hex(ciphertext))

