#include <iostream>
#include <vector>

using namespace std;

int answer = 0;
int n, m, mx, my;
int graph[4][4] = {0};
int visited[4][4] = {0};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
vector<pair<int, int>> route;

void dfs(pair<int, int> now, pair<int, int> target, int order) { // (현재 위치, 목표 지점, 현재 순서)
    if (now == target) {
        if (order == m-1) answer++;
        return ;
    }

    int x = now.first;
    int y = now.second;
    for (int i = 0; i < 4; i++) {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (-1 < nx && nx < n && -1 < ny && ny < n && graph[ny][nx] == 0 && visited[ny][nx] == 0) {
            visited[ny][nx] = 1;
            if (nx == route[order+1].first && ny == route[order+1].second) 
                dfs(make_pair(nx, ny), target, order+1);
            else
                dfs(make_pair(nx, ny), target, order);
            visited[ny][nx] = 0;
        }
    }
}

int main(int argc, char** argv)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) cin >> graph[i][j];

    for (int i = 0; i < m; i++) {
        cin >> my >> mx;
        route.push_back(make_pair(mx-1, my-1));
    }

    visited[route[0].second][route[0].first] = 1;
    dfs(route[0], route[m-1], 0);

    cout << answer;

   return 0;
}