#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>

using namespace std;

int n;
char graph[25][25] = {0};
int visited[25][25] = {0};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
vector<int> infos;
string tmp;

int bfs(int xx, int yy) {
    queue<pair<int, int>> q;
    q.push(make_pair(xx, yy));
    int cnt = 1;

    while(!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (-1 < nx && nx < n && -1 < ny && ny < n && graph[ny][nx] == '1' && visited[ny][nx] == 0) {
                visited[ny][nx] = 1;
                q.push(make_pair(nx, ny));
                cnt++;
            }
        }
    }
    
    return cnt;
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> tmp;
        for (int j = 0; j < n; j++)
            graph[i][j] = tmp[j];
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (graph[i][j] == '1' && visited[i][j] == 0) {
                visited[i][j] = 1;
                infos.push_back(bfs(j, i)); // (x, y)
            }
        }
    }

    sort(infos.begin(), infos.end());
    cout << infos.size() << "\n";
    for (auto info : infos)
        cout << info << "\n";

   return 0;
}