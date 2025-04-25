#include <vector>
using namespace std;

int count = 0;

void dfs(vector<int>& numbers, int target, int index, int current) {
    if (index == numbers.size()) {
        if (current == target) count++;
        return;
    }

    dfs(numbers, target, index + 1, current + numbers[index]);
    dfs(numbers, target, index + 1, current - numbers[index]);
}

int solution(vector<int> numbers, int target) {
    count = 0;
    dfs(numbers, target, 0, 0);
    return count;
}