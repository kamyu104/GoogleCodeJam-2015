// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 World Finals - Problem A. Costly Binary Search
 * https://code.google.com/codejam/contest/5224486/dashboard#s=p0
 *
 * Time:  O(NlogN)
 * Space: O(N)
 *
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <utility>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::max;
using std::min;

// 1 <= N <= 10^6
const int MAX_N = 1e6;

// O(log2(N) * max(cost)) ~= 20 * 9 = 180
const int MAX_TIMES = 180;

// left[t][p]: the farest position left to p which forms the range
//             [left[t][p], p) we can cover in time up to t
int left[10][MAX_N + 1];

// right[t][p]: the farest position right to p which forms the range
//              [p, right[t][p]) we can cover in time up to t
int right[10][MAX_N + 1];

int costly_binary_search() {
    string S;
    cin >> S;
    const int n = S.length();
    for (int p = 0; p <= n; ++p) {
        left[0][p] = p;
        right[0][p] = p;
    }

    // Given t time, check if there is a point where
    // we'll be able to produce the entire array.
    for (int t = 1; t <= MAX_TIMES; ++t) {
        for (int p = 0; p <= n; ++p) {
            left[t % 10][p] = left[(t - 1) % 10][p];
            right[t % 10][p] = right[(t - 1) % 10][p];
        }
        for (int p = 0; p < n; ++p) {
            const int tt = t - (S[p] - '0');
            if (tt >= 0) {
                const int l = left[tt % 10][p];
                const int r = right[tt % 10][p + 1];
                // --(t-S[p])--   --(t-S[p])--
                // [l          ]p[           r]
                left[t % 10][r] = min(left[t % 10][r], l);
                right[t % 10][l] = max(right[t % 10][l], r);
            }
        }

        for (int p = n; p > 0; --p) {
            // ------------t------------
            //       ------t------
            // ---------t---------
            // [lp   [l(p-1)      ](p-1)]p
            left[t % 10][p - 1] = min(left[t % 10][p - 1], left[t % 10][p]);
        }
        for (int p = 0; p < n; ++p) {
            // -------t-------------
            //   -----t----
            //   ----------t--------
            // [p[(p+1)    ][rp     ]]r(p+1)
            right[t % 10][p + 1] = max(right[t % 10][p + 1], right[t % 10][p]);
        }

        if (right[t % 10][0] == n) {
            // Found the min time which covers the entire array.
            return t;
        }
    }
    return MAX_TIMES;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": "
             << costly_binary_search() << endl;
    }
    return 0;
}
