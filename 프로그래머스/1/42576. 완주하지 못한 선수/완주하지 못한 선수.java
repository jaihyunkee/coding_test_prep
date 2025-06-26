import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> map = new HashMap<>();
        
        
        for (String name : participant) {
            if (map.containsKey(name)) {
                int temp = map.get(name);
                temp += 1;
                map.put(name, temp);
            }
            else {
                map.put(name, 1);
            }
        }
        
        
        for (String name2: completion) {
            if (map.containsKey(name2)) {
                int temp = map.get(name2);
                if (temp == 1) {
                    map.remove(name2);
                } else {
                    map.put(name2, temp - 1);
                }
            }
        }
        
        for (String key: map.keySet()) {
            return key;
        }
        
        return answer;
    }
}