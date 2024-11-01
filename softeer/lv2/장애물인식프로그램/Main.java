package softeer.lv2.장애물인식프로그램;

import java.io.*;
import java.util.*;

// x, y 이용
class Point {
    int x;
    int y;
    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

// 2차원 배열의 그래프(dfs 또는 bfs) -> bfs
public class Main {

    static int[][] graph = new int[26][26];
    static int[][] location = new int[26][26]; // 장애물에 영역 표시
    static int[] dx = new int[] {1, -1, 0, 0};
    static int[] dy = new int[] {0, 0, 1, -1};

    static List answer = new ArrayList<>();

    static int n;

    public static void bfs(int x, int y, int local) {
        Queue<Point> q = new LinkedList<>();

        location[y][x] = local;
        q.offer(new Point(x, y));

        while (!q.isEmpty()) {
            Point p = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = p.x + dx[i];
                int ny = p.y + dy[i];

                if (-1 < nx && nx < n && -1 < ny && ny < n && location[ny][nx] == 0 && graph[ny][nx] == 1) {
                    location[ny][nx] = local;
                    q.offer(new Point(nx, ny));
                }
            }
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine()); // 행 == 열

        // 2차원 그래프 초기화
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            for (int j = 0; j < n; j++)
                graph[i][j] = str.charAt(j) - '0';
        }

        // 정렬된 set -> cf) HashSet은 정렬 및 순서 보장은 안되지만, 중복은 제거해줌
        TreeSet<Integer> scope = new TreeSet<>();

        // 그래프에 영역 표시
        int local = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (graph[i][j] == 1 && location[i][j] == 0) {
                    scope.add(local);
                    bfs(j, i, local++);
                }
            }
        }

        // 해시 맵을 초기 세팅
        HashMap<Integer, Integer> hm = new HashMap<>();
        for (Integer s : scope)
            hm.put(s, 0);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // 0이 아닌 경우가 scope가 할당된 구간
                if (location[i][j] != 0) {
                    // key로 해당 value 값을 get
                    int tmp = hm.get(location[i][j]);
                    // value를 직접 +1 해서, 다시 put해서 value 업데이트
                    hm.put(location[i][j], tmp+1);
                }
            }
        }
        
        int index = 0;
        for (Integer s : scope)
            answer.add(hm.get(s));

        Collections.sort(answer);

        bw.write(String.valueOf(scope.size()));
        for (int i = 0; i < answer.size(); i++) {
            bw.write("\n");
            bw.write(String.valueOf(answer.get(i)));
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}
