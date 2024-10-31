package softeer.lv1.근무시간;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        // 일반적인 입력 방법(스캐너) -> 최적화안됨
        Scanner scanner = new Scanner(System.in);
        
        int answer = 0;
        String total, start, end;
        
        for (int i = 0; i < 5; i++) {
            // 한 줄 통으로 입력받기
            total = scanner.nextLine();

            // 통으로 받은 것에서 split으로 띄어쓰기 기준으로 문자 나누기
            String[] tmp = total.split(" ");
            start = tmp[0];
            end = tmp[1];

            answer += (hourToMinute(end) - hourToMinute(start));
        }

        System.out.println(answer);
    }

    // 분으로 리턴 -> 시간 문제 나오면 분으로 통일시켜서 풀자.
    // 코테에서 java는 static 이용해서 함수, 전역변수 만듦
    public static int hourToMinute(String time) {
        // substring이 파이썬에서 리스트 슬라이싱과 비슷
        String hour = time.substring(0, 2);
        String minute = time.substring(3, 5);

        int total = Integer.parseInt(hour) * 60 + Integer.parseInt(minute);
        
        return total;
    }
}