#include <stdio.h>

int main()
{
    int casos;
    int i;
    scanf("%d", &casos);

    for (i; i < casos; i++)
    {
        long long n;
        scanf("%lld", &n);
        printf("%lld\n", n*(n+1)*(n+2)/6);
    }
    return 0;

}