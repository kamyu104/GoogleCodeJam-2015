// Copyright (c) 2019 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 World Finals - Problem F. Crane Truck
 * https://code.google.com/codejam/contest/5224486/dashboard#s=p5
 *
 * Time:  O(N^2)
 * Space: O(N^2)
 *
 */

// [Analysis]
//  - N = 2000
//  - A: [0-2000, 0+2000], [] is the red area modified A
//  - B: ****[-2000-4001, 2000+4001]****
//    => ****(-6001, 6001)****,
//    * is repeated area modified by B with period pb = O(2B+1) at most 4001,
//    each circle B updates (-6001, 6001) from new computed start point,
//    run at most 4001 * 256 full circles to reach at initial point and stop
//    (increase every point by 256 in full non-periodic area)
//  - C: ****[-6001-2000, 6001+2000]****,
//    => ****[-8001, 8001]****, [] is the green area modified by C
//  - D: @@@@[-8001-(4001)^2, 8001+(4001)^2]@@@@,
//    => @@@@[-16016002, 16016002]@@@@
//    @ is repeated area with period pd = lcm(O(2B+1), O(2D+1)) at most 4001^2,
//    each circle D updates {-16016002, 16016002} from new computed start point,
//    run at most 4001^2 * 256 full circles to reach at initial point and stop,
//    (increase every point by 256 in full non-periodic area)
//  - E: @@@@[-16016002-2000, 16016002+2000]@@@@
//    => @@@@[-16018002, 16018002]@@@@, [] is the last area modified by E
// [Time]
//  - 1 + A + 256 * (1 + A + B) + C + 256 * (1 + A + B + C + B*D) + E
//    => O(256 * N^2)
// [Space]
//  - 1 + A + B + C + B*D + E <= 1 + (N + N + N + N^2 + N)
//    = N^2 + 4*N + 1= 4008001
//    => O(N^2)

#include <iostream>
#include <string>
#include <deque>
#include <vector>
#include <algorithm>
#include <utility>
#include <cassert>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::deque;
using std::vector;
using std::abs;
using std::pair;
using std::min;
using std::max;

const int64_t CIRCLE_SIZE = 1LL << 40;

uint64_t gcd(uint64_t a, uint64_t b) {  // Time: O((logn)^2)
    while (b != 0) {
        const auto tmp = b;
        b = a % b;
        a = tmp;
    }
    return a;
}

uint64_t lcm(uint64_t a, uint64_t b) {
    return a / gcd(a, b) * b;
}

struct Delta {
 public:
    explicit Delta(const string& instructions)
     : values(get_delta(instructions)) {
    }

    uint64_t count = 0LL;
    int64_t shift = 0LL;
    int64_t left = 0LL;
    int64_t right = 0LL;
    vector<pair<int64_t, uint8_t>> values;

 private:
    vector<pair<int64_t, uint8_t>> get_delta(const string& instructions) {
        deque<uint8_t> dq = {0};
        int64_t base = 0LL;
        // extend delta window
        for (const auto& c : instructions) {
            if (c == 'u') {
                --dq[shift - base];
            } else if (c == 'd') {
                ++dq[shift - base];
            } else if (c == 'b') {
                ++count;
                if (shift == base) {
                    dq.emplace_front(0);
                    --base;
                }
                --shift;
            } else if (c == 'f') {
                ++count;
                if (shift - base + 1 == dq.size()) {
                    dq.emplace_back(0);
                }
                ++shift;
            }
        }
        // shrink delta window
        left = -base;
        right = dq.size() - left - 1;
        while (left > 0) {
            if (dq[0] != 0) {
                break;
            }
            dq.pop_front();
            --left;
        }
        while (right > 0) {
            if (dq.back() != 0) {
                break;
            }
            dq.pop_back();
            --right;
        }
        vector<pair<int64_t, uint8_t>> result;  // save sparse delta window
        auto i = -left;
        for (const auto& v : dq) {
            if (v != 0) {
                result.emplace_back(i, v);
            }
            ++i;
        }
        return result;
    }
};

uint64_t simulate(const vector<pair<bool, Delta>>& deltas) {
    uint64_t result = 0;
    uint64_t period = 1ULL, left = 0ULL, right = 0ULL;
    for (const auto& kvp : deltas) {  // extend non-periodic area
        const auto& is_loop = kvp.first;
        const auto& delta = kvp.second;
        if (!is_loop || !delta.shift) {
            left += delta.left;
            right += delta.right;
        } else {
            period = lcm(period, abs(delta.shift));
            if (delta.shift < 0) {
                left += period;
            } else {
                right += period;
            }
        }
    }
    int64_t curr = left;
    vector<uint8_t> non_periodic_area(left + 1 + right);
    for (const auto& kvp : deltas) {
        const bool is_loop = kvp.first;
        const auto& delta = kvp.second;
        bool has_visited_non_periodic_area = false;
        while (true) {
            if (!has_visited_non_periodic_area &&
                0 <= curr && curr < non_periodic_area.size()) {
                has_visited_non_periodic_area = true;
            }
            const auto start = curr + delta.left;
            for (const auto& kvp : delta.values) {
                if (0 <= curr + kvp.first &&
                    curr + kvp.first < non_periodic_area.size()) {
                    non_periodic_area[curr + kvp.first] += kvp.second;
                }
            }
            curr += delta.shift;
            result += delta.count;
            if (!is_loop ||
                (0 <= curr && curr < non_periodic_area.size() &&
                 non_periodic_area[curr] == 0)) {  // stop looping
                break;
            }
            if (has_visited_non_periodic_area &&
                !(0 <= curr && curr < non_periodic_area.size())) {
                // pass through periodic area
                has_visited_non_periodic_area = false;
                int64_t rep = 0LL;
                if (delta.shift > 0) {
                    assert(curr >= non_periodic_area.size());
                    const auto target = -delta.right + CIRCLE_SIZE;
                    rep = (target - curr - 1) / delta.shift + 1;
                    curr += rep * delta.shift - CIRCLE_SIZE;
                } else {
                    assert(curr < 0);
                    const auto& target = (non_periodic_area.size() - 1) +
                                         delta.left - CIRCLE_SIZE;
                    rep = (curr - target - 1) / -delta.shift + 1;
                    curr += rep * delta.shift + CIRCLE_SIZE;
                }
                result += rep * delta.count;
            }
        }
    }
    return result;
}

int64_t crane_truck() {
    string P;
    cin >> P;

    vector<pair<bool, Delta>> deltas;
    uint64_t i = 0, j = P.find('(');
    while (i != P.length() && j != string::npos) {
        if (i != j) {
            deltas.emplace_back(false, Delta(P.substr(i, j - i)));
        }
        i = j + 1, j = P.find(')', j + 1);
        deltas.emplace_back(true, Delta(P.substr(i, j - i)));
        i = j + 1, j = P.find('(', j + 1);
    }
    if (i != P.length()) {
        deltas.emplace_back(false, Delta(P.substr(i)));
    }
    return simulate(deltas);
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": "
             << crane_truck() << endl;
    }
    return 0;
}
