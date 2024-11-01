package softeer.lv2.팔단변속기;

import java.io.*;
import java.util.*;

public class Main {

    static int[] arr = new int[8];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 8; i++)
            arr[i] = Integer.parseInt(st.nextToken());

        boolean asc, des;
        asc = des = false;

        for (int i = 1; i < 8; i++) {
            if (arr[i] > arr[i-1]) asc = true;
            else des = true;
        }

        if (asc == des && asc == true) bw.write("mixed");
        else {
            if (asc == true) bw.write("ascending");
            else bw.write("descending");
        }

        bw.flush();
        bw.close();
        br.close();
    }
}
