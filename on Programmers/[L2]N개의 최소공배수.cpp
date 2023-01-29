//https://school.programmers.co.kr/learn/courses/30/lessons/12953

#include <string>
#include <vector>

using namespace std;

int gcd(int x, int y){
    if(x == 0) return y;
    
    return gcd(y%x,x);
}

int lcm(int x, int y){
    return x*y / gcd(x,y);
}

int solution(vector<int> arr) {
    int answer = 0;
    answer = arr[0];
    for(int i=1;i<arr.size();i++){
        answer = lcm(answer,arr[i]);
    }
    
    return answer;
}
