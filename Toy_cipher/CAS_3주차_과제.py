S = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

def sbox(input):
    return S[input]

def permutation1(list): 
    per_list = [list[12], list[13], list[14], list[15], list[0], list[1], list[2], list[3],list[4], list[5], list[6], list[7],list[8], list[9], list[10], list[11]]
    return per_list

def permutation2(list): 
    per_list = [list[15], list[0], list[1], list[2], list[3],list[4], list[5], list[6], list[7],list[8], list[9], list[10], list[11],list[12], list[13], list[14]]
    return per_list

def input_to_binary_list(input): # 입력을 이진 리스트로 변환하는 함수 ex) 0xaf --> [1,0,1,0,1,1,1,1] 리스트의[0]이 Most Significant Bit 

    binary_str = format(input, '016b') #입력을 16비트의 이진수로 변환
    binary_list = [int(bit) for bit in binary_str] #변환한 16비트의 이진수를 리스트에 넣기
    
    return binary_list 

def list_split(list): # list를 입력받아 S-Box에 넣을 수 있도록 4개로 쪼개는 함수
    S_BOX1 = list[0]*8 + list[1]*4 + list[2]*2 + list[3] 
    S_BOX2 = list[4]*8 + list[5]*4 + list[6]*2 + list[7] 
    S_BOX3 = list[8]*8 + list[9]*4 + list[10]*2 + list[11] 
    S_BOX4 = list[12]*8 + list[13]*4 + list[14]*2 + list[15] 

    return S_BOX1, S_BOX2, S_BOX3, S_BOX4


def encryption(plaintext, key): # plaintext와 key를 입력받아 암호문 return 
    # round 1 
    XOR_LIST = plaintext ^ key
    cipher_1 = input_to_binary_list(XOR_LIST)

    Round1_list = permutation1(cipher_1) # 리스트를 입력으로 받아 permutation
    S_BOX1, S_BOX2, S_BOX3, S_BOX4 = list_split(Round1_list)

    cipher_1 = sbox(S_BOX1)*4096 + sbox(S_BOX2)*256 + sbox(S_BOX3)*16 + sbox(S_BOX4) #sbox 치환된 8비트 값

    # round 2
    XOR_LIST = cipher_1 ^ key
    cipher_2 = input_to_binary_list(XOR_LIST)

    Round2_list = permutation2(cipher_2) # 리스트를 입력으로 받아 permutation
    S_BOX1, S_BOX2, S_BOX3, S_BOX4 = list_split(Round2_list)

    cipher_2 = sbox(S_BOX1)*4096 + sbox(S_BOX2)*256 + sbox(S_BOX3)*16 + sbox(S_BOX4) #sbox 치환된 8비트 값

    cipher = cipher_2 ^ key
    return cipher # 암호문 return 

ciphertext = encryption(0xABCD,0xEFEF) #palintext ,key) 
print(hex(ciphertext))  #암호문을 16진수로 출력


