#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int answer = INT_MAX;
vector<int> arr, hubo;
int visited[10] = {0};
int n, m, k;

int min(int a, int b) {
    if (a > b) return b;
    return a;
}

void dfs() {
    if (hubo.size() == arr.size()) {
        int total = 0;
        
        int index = 0;
        for (int i = 0; i < k; i++) {
            int cnt = 0;
            while (true) {
                if (cnt + hubo[index % hubo.size()] > m) {
                    total += cnt;
                    break;
                }
                cnt += hubo[index % hubo.size()];
                index++;
            }
        }

        answer = min(total, answer);
        return;
    }

    for (int i = 0; i < arr.size(); i++) {
        if (visited[i] == 0) {
            visited[i] = 1;
            hubo.push_back(arr[i]);
            dfs();
            visited[i] = 0;
            hubo.pop_back();
        }
    }
}

// O(N) = 10!
int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> n >> m >> k;
    
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        arr.push_back(tmp);
    }

    dfs();

    cout << answer;

   return 0;
}