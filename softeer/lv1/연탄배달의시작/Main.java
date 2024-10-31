package softeer.lv1.연탄배달의시작;

import java.io.*;
import java.util.*;

public class Main {

    static int[] arr = new int[1001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        int target = arr[1] - arr[0];
        int answer = 1;

        for (int i = 2; i < n; i++) {
            if (arr[i] - arr[i-1] < target) {
                target = arr[i] - arr[i-1];
                answer = 1;
            } else if (arr[i] - arr[i-1] == target) answer++;
        }

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
        br.close();
    }
}