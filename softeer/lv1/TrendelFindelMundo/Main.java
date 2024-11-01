package softeer.lv1.TrendelFindelMundo;

import java.io.*;
import java.util.*;

public class Main {

    static int arr[][] = new int[1001][1001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++)
                arr[i][j] = Integer.parseInt(st.nextToken());
        }

        int target = 1000;
        int answer_x, answer_y;
        answer_x = answer_y = 0;
        for (int i = 0; i < n; i++)
            if (target > arr[i][1]) target = arr[i][1];

        for (int i = 0; i < n; i++) {
            if (target == arr[i][1]) {
                answer_x = arr[i][0];
                answer_y = arr[i][1];
                break;
            }
        }

        bw.write(String.format("%d %d", answer_x, answer_y));
        bw.flush();
        bw.close();
        br.close();
    }
}
