package softeer.lv2.지도자동구축;

import java.io.*;

public class Main {

    static int[] dp = new int[16];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        dp[0] = 2;

        int n = Integer.parseInt(br.readLine());
        for (int i = 1; i <= n; i++)
            dp[i] = dp[i-1]*2-1;

        bw.write(String.valueOf(dp[n]*dp[n]));
        bw.flush();
        bw.close();
        br.close();
    }
}
