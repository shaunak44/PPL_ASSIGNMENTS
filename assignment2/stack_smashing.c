#include <stdio.h>
void function(char *str){
    char buff[16];
    strcpy(buff, str);
}

int main()
{
    char str[256];
    for(int i = 0; i < 255; i++) {
        str[i] = 'a';
    }
    function(str);

    return 0;
}
