#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;
bool compare(const string &a, const string &b) {
    return a + b > b + a;  // a + b가 b + a보다 큰 순서로 정렬
}
string solution(vector<int> numbers) {
    // numbers의 각 원소를 문자열로 변환
    vector<string> strNumbers;
    for (int num : numbers) {
        strNumbers.push_back(to_string(num));
    }

    // 사용자 정의 비교 함수로 내림차순 정렬
    sort(strNumbers.begin(), strNumbers.end(), compare);

    // 만약 첫 번째 원소가 '0'이라면 모든 원소가 '0'이라는 의미이므로 "0"을 반환
    if (strNumbers[0] == "0") {
        return "0";
    }

    // 결과 문자열을 이어붙이기
    string result = "";
    for (string &str : strNumbers) {
        result += str;
    }

    return result;
}