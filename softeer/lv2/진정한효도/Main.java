package softeer.lv2.진정한효도;

import java.io.*;
import java.util.*;

public class Main {

    static int[][] arr = new int[3][3];

    public static int min(int a, int b) {
        if (a > b) return b;
        return a;
    }

    public static int max(int a, int b) {
        if (a > b) return a;
        return b;
    }

    public static int findMinRow(int x) {
        int MAX = max(max(arr[0][x], arr[1][x]), arr[2][x]);
        int MIN = min(min(arr[0][x], arr[1][x]), arr[2][x]);
        
        return MAX-MIN;
    }

    public static int findMinColumn(int y) {
        int MAX = max(max(arr[y][0], arr[y][1]), arr[y][2]);
        int MIN = min(min(arr[y][0], arr[y][1]), arr[y][2]);
        
        return MAX-MIN;
    }

    public static int findMinAnswer(int x, int y) {
        int row = findMinRow(x); // 열 고정, 행 변경
        int column = findMinColumn(y); // 열 변경, 행 고정

        return min(row, column);
    }

    // max 값 - min 값
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (int i = 0; i < 3; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++)
                arr[i][j] = Integer.parseInt(st.nextToken());
        }

        int answer = 100;
        for (int i = 0; i < 3; i++)
            answer = min(answer, findMinAnswer(i, i));

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
        br.close();
    }
}
