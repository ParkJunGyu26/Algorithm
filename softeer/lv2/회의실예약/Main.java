package softeer.lv2.회의실예약;

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // room 이름을 오름차순으로 정렬이 필요함. 그래서 
        TreeSet<String> rooms = new TreeSet<>();

        // 각 회의실에 대한 시작 및 종료 시간 저장하는 해시맵
        HashMap<String, List<int[]>> schedule = new HashMap<>();

        // room set 초기화(입력값 할당)
        for (int i = 0; i < n; i++)
            rooms.add(br.readLine());

        // room에 대한 hashmap 빈 리스트로 초기화
        /*
         * Array는 c++의 일반 배열과 유사
         * (Array)List는 c++의 vector처럼 동적 배열과 유사
         */
        for (String room : rooms)
            schedule.put(room, new ArrayList<>());

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String roomName = st.nextToken();
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());

            // 해시맵에서 해당하는 room에 대한 key에 대해 value를 추가해주는 부분 (리스트로 {시작, 종료})
            // 리스트가 동적 할당이 가능하므로 add 메서드 사용
            schedule.get(roomName).add(new int[]{s, e});
        }

        // 결국엔 회의실 방에 대한 정보가 필요하므로 for each를 rooms으로
        for (String room : rooms) {
            // 문자열이라서 그냥 그대로 사용하고, '+'로 문자열끼리 붙이기
            bw.write("Room " + room + ":\n");

            // 첫 번째 회의실의 시간 정보를 모두 조회(value)
            List<int[]> times = schedule.get(room);

            // 람다로 오름차순 정렬(a와 b 중 a 기준으로 오름차순)
            /*
            자바의 정렬 비교는 다음 규칙을 따릅니다:

            음수(-) 반환 → a가 b보다 앞에 위치
            양수(+) 반환 → a가 b보다 뒤에 위치
            0 반환 → 순서 유지
            
            */
            Collections.sort(times, (a, b) -> a[0] - b[0]);

            // 회의실의 빈 시간 탐색
            List<int[]> available = findAvailableTime(times);

            if (available.isEmpty())
                bw.write("Not available\n");
            else {
                bw.write(available.size() + " available:\n");
                for (int[] time : available)
                    // 문자열 포맷팅에서 2글자로 출력해야되므로 0으로 메꿔줌
                    bw.write(String.format("%02d-%02d\n", time[0], time[1]));
            }

            // room이 마지막이 아닌 경우에 구분선 출력
            if (!room.equals(rooms.last()))
                bw.write("-----\n");
        }

        bw.flush();
        bw.close();
        br.close();
    }

    // 정수형 리스트를 반환해주는 함수. 매개변수로 정수형 리스트를 받음
    public static List<int[]> findAvailableTime(List<int[]> occupied) {
        // 반환해줄 정수형 리스트
        List<int[]> available = new ArrayList<>();
        
        // 시작시간은 9시이므로
        int current = 9;

        // 매개변수로 받은 회의실 시간을 모두 탐색
        for (int[] time : occupied) {
            // time[0]은 시작시간임. 그래서 현재 시간과 비교해나가기
            if (current < time[0])
                // 배열 리스트에 현재 시간부터, 회의실 시작 시간까지 추가해주기
                available.add(new int[]{current, time[0]});
            // 현재 시간은 회의실 종료 시간으로 초기화
            current = time[1];
        }

        // 현재 시간. 즉, 마지막으로 종료된 시간이 18시가 안되면 18시 전까지 사용하다는 뜻
        if (current < 18)
            // 그래서 사용가능한 회의 시간으로 현재 시간부터 18시까지 추가해주기
            // 동적 리스트라서 add로 리스트 값 추가 가능
            available.add(new int[]{current, 18});

        return available;
    }
}
