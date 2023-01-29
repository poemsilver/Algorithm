// https://school.programmers.co.kr/learn/courses/30/lessons/42579?language=cpp

#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    map<string,int> music; //장르별,재생횟수
    map<string,map<int,int>> mlist; //장르별, 노래별 몇 번 재생
    
    for(int i=0;i<genres.size();i++){
        music[genres[i]] += plays[i];
        mlist[genres[i]].push_back(plays[i],[i]); //장르별 (재생횟수,노래번호)
    }
    
    while(music.size()>0){ //0개 이상 배열인 상태에서 계속 반복 = 장르가 다 없어지면 중지
        
        string gen; //가장 재생많이 된 종류
        int max=0; //가장 많이 재생된 재생 수
        
        for(auto &k:music){
            if(max<k.second){
                max=k.second;
                gen=k.first;
            }
        }
        
    } 
    for (int i = 0; i < 2; i++){
            int val = 0, ind = -1;
            //노래중에서 제일높은것 찾기
            for (auto ml : musiclist[genre]) {
                if (val < ml.second) {
                    val = ml.second;
                    ind = ml.first;
                }
            }
            //만약 노래가 0~1곡밖에없다면 반복문 탈출
            if (ind == -1)    break;
            //리턴할 리스트에 노래번호 추가
            answer.push_back(ind);
            musiclist[gen].erase(ind);
        }
        //map 에서 사용한 장르삭제
        music.erase(gen);
    }
    return answer;
}
