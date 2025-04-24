#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) {
    vector<int> answer;
    for (int i = 0; i < arr.size(); i++) {
        int repeat = arr[i];
        for (int j = 0; j < repeat; j++){
            answer.push_back(repeat);
        }
    }
    return answer;
}