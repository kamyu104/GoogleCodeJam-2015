// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 World Finals - Problem C. Pretty Good Proportion
 * https://code.google.com/codejam/contest/5224486/dashboard#s=p2
 *
 * Time:  O(NlogN)
 * Space: O(N)
 *
 */

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>
#include <limits>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::pair;
using std::numeric_limits;
using std::make_pair;
using std::sort;
using std::swap;
using std::abs;

const int PRECISION = 1000000;

int64_t gcd(int64_t x, int64_t y) {
    while (y > 0) {
        int64_t z = x % y;
        x = y, y = z;
    }
    return x;
}

bool smaller(int64_t x1, int64_t y1,
             int64_t x2, int64_t y2) {
    if (x1 / y1 < x2 / y2) {
        return true;
    } else if (x1 / y1 > x2 / y2) {
        return false;
    } else {
        x1 %= y1, x2 %= y2;
        if (x2 == 0) {
            return false;
        } else if (x1 == 0) {
            return true;
        } else {
            return smaller(y2, x2, y1, x1);
        }
    }
}

void check(const int64_t F, const vector<int>& sum,
           int p, int q,
           int64_t *bestx, int64_t *besty,
           int *ans) {
    if (p > q) {
        swap(p, q);
    }
    int64_t dx = q - p, dy = sum[q] - sum[p];
    int64_t x = abs(dy * PRECISION - dx * F), y = dx * PRECISION;
    int64_t g = gcd(x, y);
    x /= g, y /= g;
    if (smaller(x, y, *bestx, *besty)) {
        *bestx = x, *besty = y;
        *ans = p;
    } else if (!smaller(*bestx, *besty, x, y) && p < *ans) {
        *ans = p;
    }
}

int pretty_good_proportion() {
    int N;
    double tmp;
    cin >> N >> tmp;
    int64_t F = static_cast<int64_t>(tmp * PRECISION + 0.5);
    string s;
    cin >> s;

    vector<int> sum(N + 1);
    for (int i = 0; i < N; ++i) {
        sum[i + 1] = sum[i] + ((s[i] == '1') ? 1 : 0);
    }
    vector<pair<int64_t, int>> p(N + 1);
    for (int i = 0; i < N + 1; ++i) {
        p[i] = make_pair(static_cast<int64_t>(sum[i]) * PRECISION -
                         static_cast<int64_t>(i) * F,
                         i);
    }
    sort(p.begin(), p.end());  // Time: O(nlogn)

    int64_t bestx = 2, besty = 1;  // best ans is bestx / besty
    int ans = numeric_limits<int>::max();
    for (int i = 0; i < N; ++i) {
        check(F, sum, p[i].second, p[i + 1].second,
              &bestx, &besty, &ans);
    }
    return ans;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": "
             << pretty_good_proportion() << endl;
    }
    return 0;
}

