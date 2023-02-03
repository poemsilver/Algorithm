// https://softeer.ai/practice/result.do?eventIdx=1&psProblemId=407&submissionSn=SW_PRBL_SBMS_21225#hold
#include<iostream>
#include<cmath>

using namespace std;

int main(int argc, char** argv)
{
    long long K,P;
    int N;
    long long nn = 1000000007;
    cin >> K;
    cin >> P;
    cin >> N;
    long long answer;

    while(N--) K = (K*P)%nn;
    
    cout << K << endl;
    
 return 0;
}
