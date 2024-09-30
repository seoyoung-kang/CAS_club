S = [0xc, 0x5, 0x6, 0xb, 0x9, 0x0, 0xa, 0xd, 0x3, 0xe, 0xf, 0x8, 0x4, 0x7, 0x1, 0x2]

def sbox(input):
    return S[input]

def permutation(list): 
    per_list = [list[4], list[5], list[0], list[1], list[6], list[7], list[2], list[3]]
    return per_list

def input_to_binary_list(input): # 입력을 이진 리스트로 변환하는 함수 ex) 0xaf --> [1,0,1,0,1,1,1,1] 리스트의[0]이 Most Significant Bit 

    binary_str = format(input, '08b') #입력을 8비트의 이진수로 변환
    binary_list = [int(bit) for bit in binary_str] #변환한 8비트의 이진수를 리스트에 넣기
    
    return binary_list 

def encryption(plaintext, key): # plaintext와 key를 입력받아 암호문 return 

    bin_list = input_to_binary_list(plaintext) # plaintext를 이진 리스트로 변환
    per_list = permutation(bin_list) # 리스트를 입력으로 받아 permutation
    
  
    left = per_list[0]*8 + per_list[1]*4 + per_list[2]*2 + per_list[3] # permutation된 리스트의 상위 4비트 sbox치환
    right = per_list[4]*8 + per_list[5]*4 + per_list[6]*2 + per_list[7] # permutation된 리스트의 하위 4비트 sbox치환
    
    out_sbox = sbox(left)*16 + sbox(right) #sbox 치환된 8비트 값
    
    cipher = out_sbox ^ key # 치환된 8비트 와 key 8비트 xor
     
    return cipher # 암호문 return 

ciphertext = encryption(0x6b,0xff) # plaintext = 0x6b key = 0xff
print(hex(ciphertext))  #암호문을 16진수로 출력


