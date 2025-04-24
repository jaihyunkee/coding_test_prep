#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    int mem = -1;
    
    for (int i = 0; i < arr.size(); i++) {
        if (mem != arr[i]) {
            answer.push_back(arr[i]);
        }
        mem = arr[i];
    }
    
    return answer;
}