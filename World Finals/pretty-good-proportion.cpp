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
#include <cmath>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;
using std::pair;
using std::make_pair;
using std::sort;
using std::swap;
using std::abs;
using std::round;

const int PRECISION = 1000000;

int64_t gcd(int64_t x, int64_t y) {
    while (y > 0) {
        x %= y;
        swap(x, y);
    }
    return x;
}

// No multiplication in comparison of fractions
// to avoid overflow.
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

// Find the minimum of abs(slope).
void check(const int64_t F, const vector<int>& sum,
           int p, int q,
           int64_t *min_x, int64_t *min_y,
           int *ans) {
    if (p > q) {
        swap(p, q);
    }
    int64_t dx = q - p, dy = sum[q] - sum[p];
    int64_t y = abs(dy * PRECISION - dx * F), x = dx * PRECISION;
    int64_t g = gcd(x, y);
    x /= g, y /= g;
    if (smaller(y, x, *min_y, *min_x)) {
        *min_x = x, *min_y = y;
        *ans = p;
    } else if (!smaller(*min_y, *min_x, y, x) && p < *ans) {
        // If they are the same slope,
        // update ans to the smallest p.
        *ans = p;
    }
}

int pretty_good_proportion() {
    int N;
    double f;
    cin >> N >> f;
    int64_t F = static_cast<int64_t>(round(f * PRECISION));
    string s;
    cin >> s;

    vector<int> sum(N + 1);
    for (int i = 0; i < N; ++i) {
        sum[i + 1] = sum[i] + ((s[i] == '1') ? 1 : 0);
    }
    vector<pair<int64_t, int>> p(N + 1);
    for (int i = 0; i < N + 1; ++i) {
        // Diff error e(i): #(1s) - i * f
        p[i] = make_pair(static_cast<int64_t>(sum[i]) * PRECISION -
                         static_cast<int64_t>(i) * F,
                         i);
    }
    // Time: O(nlogn)
    // Sort the pair (e(i), i) by diff error e(i)
    sort(p.begin(), p.end());

    //  ans is with the min(abs(min_y / min_x - f))
    int64_t min_x = 1, min_y = 1;
    int ans = N - 1;
    // Try out all neighboring pairs to find the points with
    // the smallest e(i) difference.
    // i.e. min(abs(slope)) of any neighboring pairs.
    for (int i = 0; i < N; ++i) {
        check(F, sum, p[i].second, p[i + 1].second,
              &min_x, &min_y, &ans);
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

