// https://school.programmers.co.kr/learn/courses/30/lessons/42586?language=cpp

#include <string>
#include <vector>
#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    queue<int> day;
    answer.push_back(1);
    
    for(int i=0;i<progresses.size();i++){
        day.push((99-progresses[i])/speeds[i] + 1);
    }
    
    int count = 0;
    int check = day.front();
    
    while(!day.empty()){
        day.pop();
        
        if(check >= day.front()&&!day.empty()){
            answer[count]++;
        }
        
        else if(check < day.front() && !day.empty()){
            answer.push_back(1);
            count++;
            check = day.front();
        }
    }
    return answer;
}
