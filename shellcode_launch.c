char shellcode[]="\x66\x81\xEC\x40\x04\x33\xDB……";//欲调试的十六//进制机器码"
void main()
{
  __asm
  {
  lea eax, shellcode
  push eax
  ret
}
