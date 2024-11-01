package softeer.lv1.나무심기;

import java.io.*;
import java.util.*;

public class Main {

    static int arr[] = new int[101];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        Arrays.sort(arr, 0, n);

        int answer = 1;
        if (arr.length == 2)
            answer = arr[0] * arr[1];
        else
            answer = max(arr[0]*arr[1], arr[n-2]*arr[n-1]);

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
        br.close();
    }

    public static int max(int a, int b) {
        if (a > b) return a;
        return b;
    }
}
