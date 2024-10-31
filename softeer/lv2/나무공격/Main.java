package softeer.lv2.나무공격;

import java.io.*;
import java.util.*;

public class Main {
    
    // 위한 2차원 '전역'배열
    static int[][] arr = new int[101][101];

    // 5개의 행을 반복해서 1이 있는 경우 0으로 초기화
    public static void attack(int start, int end) {
        for (int i = start; i <= end; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == 1) {
                    arr[i][j] = 0;
                    break;
                }
            }
        }
    }

    // 전역변수
    static int n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 전역변수 n과 m을 공백을 이용한 초기화
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        // 2차원 배열 초기화
        for (int i = 0; i < n; i++) {
            // i번째 행에 해당하는 것을 모두 문자열로 입력
            st = new StringTokenizer(br.readLine());

            // 해당 문자열을 j개로 분리해서 2차원 배열에 값을 할당
            for (int j = 0; j < m; j++)
                arr[i][j] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        int L1 = Integer.parseInt(st.nextToken());
        int R1 = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int L2 = Integer.parseInt(st.nextToken());
        int R2 = Integer.parseInt(st.nextToken());

        attack(L1-1, R1-1);
        attack(L2-1, R2-1);

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (arr[i][j] == 1) answer++;
            }
        }

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
        br.close();
    }
}
