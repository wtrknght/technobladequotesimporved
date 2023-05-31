#include <stdio.h>
int main(){
  if(GetKeyState('A') & 0x8000/*Check if high-order bit is set (1 << 15)*/){
    printf("HI");
    
    // Do stuff
  }
}
