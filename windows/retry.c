#include <Windows.h>
#include <stdio.h>
#include <sleep.h>
int main(){
	while(1){
  	if(GetKeyState('A') & 0x8000/*Check if high-order bit is set (1 << 15)*/){
      printf("%s", randquote);
      sleep(0.25);
  		}
  	}
}
