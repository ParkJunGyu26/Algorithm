package softeer.lv1.개표;

import java.io.*;
import java.util.*;

public class Main {

    // 몫의 개수 = +
    // 나머지 개수 = |
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < T; i++) {
            int n = Integer.parseInt(br.readLine());
            String answer = "";

            for (int j = 0; j < n/5; j++)
                answer += "++++ ";
            for (int j = 0; j < n%5; j++)
                answer += "|";

            System.out.println(answer);
        }
    }
}