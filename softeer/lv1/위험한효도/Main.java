package softeer.lv1.위험한효도;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        int now, time;
        now = time = 0;

        // ture : 뒤, false : 앞
        boolean dire = true;
        // false : 터치 후, true : 터치 전
        boolean touch = true;

        while (true) {
            if (touch) {
                if (now + a >= d) {
                    time += (d - now);
                    now += (d - now);
                    touch = false;
                } else {
                    now += a;
                    time += (a+b);
                }
            } else {
                if (now + b >= 2*d) {
                    time += (2*d - now);
                    now += (2*d - now);
                    break;
                } else {
                    now += b;
                    time += (a+b);
                }
            }
        }

        bw.write(String.valueOf(time));
        bw.flush();
        bw.close();
        br.close();
    }
}