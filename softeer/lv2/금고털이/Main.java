package softeer.lv2.금고털이;

import java.io.*;
import java.util.*;

class Treasure{
    int weight, price;

    public Treasure(int w, int p) {
        weight = w;
        price = p;
    }
}

public class Main {

    static List<Treasure> info = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int w = Integer.parseInt(st.nextToken()); // 현재 무게
        int n = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int m = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());

            info.add(new Treasure(m, p));
        }

        // p를 기준으로 내림차순 정렬
        Collections.sort(info, (a, b) -> Integer.compare(b.price, a.price));

        int answer = 0;
        int index = 0;
        while (w > 0 && index < info.size()) {
            if (w >= info.get(index).weight) {
                answer += info.get(index).price * info.get(index).weight;
                w -= info.get(index).weight;
            } else {
                answer += info.get(index).price * w;
                w = 0;
            }
            index++;
        }

        bw.write(String.valueOf(answer));
        bw.flush();
        bw.close();
        br.close();
    }
}
