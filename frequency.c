#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char input[1000];
    int alpha_count[26] = {0};
    int i = 0;
    int alpa = 0;

    printf("문자열을 입력하세요: ");
    fgets(input, sizeof(input), stdin); 

    while (input[i] != '\0') { 
        if (input[i] >= 'a' && input[i] <= 'z') { 
            alpa = input[i] - 'a';
            alpha_count[alpa] += 1;
        } else if (input[i] >= 'A' && input[i] <= 'Z') { 
            alpa = input[i] - 'A'; 
            alpha_count[alpa] += 1;
        }
        i++;
    }

    for (int j = 0; j < 26; j++) {
        printf("%c : %d\n", j + 'a', alpha_count[j]); 
    }

    return 0;
}