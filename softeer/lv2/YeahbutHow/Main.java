package softeer.lv2.YeahbutHow;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String T = br.readLine();

        // 자바에서는 스택 보다 큐를 권장!!
        Deque<Character> dq = new ArrayDeque<>();
        for (int i = 0; i < T.length(); i++) {
            // 자바에서 문자열 접근을 하기 위해선 T[i]가 아닌, T.charAt(i)이다.
            if (T.charAt(i) == '(') 
                // 스택의 push는 왼쪽에서 오른쪽으로 채워짐
                /*
                    A push -> [A]
                    B push -> [B][A]
                    C push -> [C][B][A]
                */

                // 큐의 offer는 FIFO이므로 순서대로 채워짐. 즉, 우리가 보기 편한 순서대로
                /*
                    A offer -> [A]
                    B offer -> [A][B]
                    C offer -> [A][B][C]
                */
                dq.offer('(');
            else {
                dq.offer('1');
                dq.offer(')');
                if (i != T.length()-1)
                    dq.offer('+');
            }
        }

        // Deque는 배열처럼 인덱스로 접근할 수 없음 -> 잘못된 접근 방식
        // for (int i = 0; i < S.size(); i++)
            // bw.write(String.valueOf(S[i]));
        
        while(!dq.isEmpty())
            // 큐에서 pop하는 방법은 poll이고, 스택의 pop은 동일하게 pop이다.
            bw.write(String.valueOf(dq.poll()));

        // for each로 해당 타입으로 접근하는 것은 가능 -> 이상 없는 접근 방식
        // for (Character c : dq)
        //     bw.write(String.valueOf(c));
        
        bw.flush();
        bw.close();
        br.close();
    }
}
