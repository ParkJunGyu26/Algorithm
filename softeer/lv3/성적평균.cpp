#include<iostream>

#define MAX_SIZE 1000000

using namespace std;

int n, k, a, b;
int arr[MAX_SIZE] = {0};
int preSum[MAX_SIZE+1] = {0};

// 누적합
int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> k;
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    for (int i = 1; i <= n; i++)
        preSum[i] = arr[i-1] + preSum[i-1];

    for (int i = 0; i < k; i++) {
        cin >> a >> b;
        printf("%.2f\n", ((preSum[b]-preSum[a-1]) / (double)(b-a+1)));
    }

   return 0;
}