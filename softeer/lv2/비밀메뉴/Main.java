package softeer.lv2.비밀메뉴;

import java.io.*;
import java.util.*;

public class Main {

    static int secrets[] = new int[101];
    static int user[] = new int[101];

    static Deque<Integer> window = new ArrayDeque<>();

    public static boolean checkOneToOne() {

        int i = 0;
        for (Integer w : window)
            if (w != secrets[i++]) return false;
        
        return true;
    }

    // 슬라이딩 윈도우
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 비밀키 초기화
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++)
            secrets[i] = Integer.parseInt(st.nextToken());

        // 유저 입력키 초기화
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            user[i] = Integer.parseInt(st.nextToken());

        // 문제에서 이야기해준 엣지 케이스 예외처리
        if (n < m) {
            bw.write("normal");
            bw.flush();
            bw.close();
            br.close();
            return;
        }

        // 슬라이딩 윈도우를 위한 세팅
        boolean check = false;
        for (int i = 0; i < m; i++)
            window.offer(user[i]);

        // 슬라이딩 윈도우 탐색
        for (int i = 0; i <= n-m; i++) {
            // bw.write(String.format("i : %d\n", i));
            if (checkOneToOne()) {
                check = true;
                break;
            } else {
                if (i == n-m) break;
                
                // Deque를 Queue처럼 FIFO
                window.poll();
                window.offer(user[i+m]);
            }
        }

        if (check) bw.write("secret");
        else bw.write("normal");
        bw.flush();
        bw.close();
        br.close();
    }
}
