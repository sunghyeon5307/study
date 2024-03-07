#include <stdio.h>

int partition(int list[], int left, int right)
{
    int pivot, low, high;
    int temp;
    low = left;
    high = right+1;
    pivot = list[left];
    do{
        do{
            low++;
        }while(pivot>list[low]);
        do{
            high--;
        }while(pivot<list[high]);
        if(low<high)
        {
            temp = list[low];
            list[low] = list[high];
            list[high] = temp;
        }
    }while(low<high);
    temp = list[high];
    list[high] = list[left];
    list[left] = temp;
    return high;
}

void quicksort(int list[], int left, int right)
{
    if(left<right)
    {
        int q = partition(list, left, right);
        quicksort(list, left, q-1);
        quicksort(list, q+1, right);
    }
}

int main()
{
    int list[] = {5,3,8,4,9,1,6,2,7};
    int i, n;
    n = sizeof(list)/sizeof(int);
    quicksort(list, 0, n-1);
    for(i=0; i<n; i++)
        printf("%d ", list[i]);
    printf("\n");
    return 0;
}
