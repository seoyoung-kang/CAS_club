S = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

def sbox(input):
    return S[input]

def permutation1(list): 
    per_list = [list[12], list[13], list[14], list[15], list[0], list[1], list[2], list[3],list[4], list[5], list[6], list[7],list[8], list[9], list[10], list[11]]
    return per_list

def permutation2(list): 
    per_list = [list[15], list[0], list[1], list[2], list[3],list[4], list[5], list[6], list[7],list[8], list[9], list[10], list[11],list[12], list[13], list[14],]
    return per_list

def input_to_binary_list(input): # 입력을 이진 리스트로 변환하는 함수 ex) 0xaf --> [1,0,1,0,1,1,1,1] 리스트의[0]이 Most Significant Bit 

    binary_str = format(input, '08b') #입력을 8비트의 이진수로 변환
    binary_list = [int(bit) for bit in binary_str] #변환한 8비트의 이진수를 리스트에 넣기
    
    return binary_list 

def encryption(plaintext, key): # plaintext와 key를 입력받아 암호문 return 

    bin_list = input_to_binary_list(plaintext) # plaintext를 이진 리스트로 변환
    
    # round 1 
    Round1_list = permutation1(bin_list) # 리스트를 입력으로 받아 permutation

    S_BOX1 = Round1_list[0]*8 + Round1_list[1]*4 + Round1_list[2]*2 + Round1_list[3] 
    S_BOX2 = Round1_list[4]*8 + Round1_list[5]*4 + Round1_list[6]*2 + Round1_list[7] 
    S_BOX3 = Round1_list[8]*8 + Round1_list[9]*4 + Round1_list[10]*2 + Round1_list[11] 
    S_BOX4 = Round1_list[12]*8 + Round1_list[13]*4 + Round1_list[14]*2 + Round1_list[15] 

    out_sbox = sbox(S_BOX1)*4096 + sbox(S_BOX2)*256 + sbox(S_BOX3)*16 + sbox(S_BOX4) #sbox 치환된 8비트 값
    cipher_1 = out_sbox ^ key # 치환된 8비트 와 key 8비트 xor

    # round 2
    Round2_list = permutation2(cipher_1) # 리스트를 입력으로 받아 permutation

    S_BOX1 = Round2_list[0]*8 + Round2_list[1]*4 + Round2_list[2]*2 + Round2_list[3] 
    S_BOX2 = Round2_list[4]*8 + Round2_list[5]*4 + Round2_list[6]*2 + Round2_list[7] 
    S_BOX3 = Round2_list[8]*8 + Round2_list[9]*4 + Round2_list[10]*2 + Round2_list[11] 
    S_BOX4 = Round2_list[12]*8 + Round2_list[13]*4 + Round2_list[14]*2 + Round2_list[15] 

    out_sbox = sbox(S_BOX1)*4096 + sbox(S_BOX2)*256 + sbox(S_BOX3)*16 + sbox(S_BOX4) #sbox 치환된 8비트 값
    cipher = out_sbox ^ key # 치환된 8비트 와 key 8비트 xor
         
    return cipher # 암호문 return 

ciphertext = encryption(0x6B,0xFF)#palintext ,key) 
print(hex(ciphertext))  #암호문을 16진수로 출력


