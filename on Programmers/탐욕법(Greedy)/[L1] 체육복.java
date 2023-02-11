// https://school.programmers.co.kr/learn/courses/30/lessons/42862?language=java

import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        Set<Integer> lost_p = new HashSet<>();
        Set<Integer> rese_p = new HashSet<>();
        
        for (int i : lost) {
            lost_p.add(i);
        }
        
        for (int i : reserve) {
            if (lost_p.contains(i)) {
                lost_p.remove(i);
            } else {
                rese_p.add(i);
            }
        }
        
        for (int i : rese_p) {
            if (lost_p.contains(i - 1)) {
                lost_p.remove(i - 1);
            } else if (lost_p.contains(i + 1)) {
                lost_p.remove(i + 1);
            }
        }
        
        return n - lost_p.size();
    }
}
