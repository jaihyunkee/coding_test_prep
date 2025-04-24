#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    unordered_map<string, int> type_count;

    // 종류별 개수 세기
    for (const auto& cloth : clothes) {
        string type = cloth[1];
        type_count[type]++;
    }

    int combinations = 1;
    for (const auto& pair : type_count) {
        combinations *= (pair.second + 1);  // 안 입는 경우 포함
    }

    return combinations - 1;  // 아무것도 안 입는 경우 제외
}
