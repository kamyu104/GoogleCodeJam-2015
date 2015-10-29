// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 World Finals - Problem A. Costly Binary Search
 * https://code.google.com/codejam/contest/5224486/dashboard#s=p0
 *
 * Time:  O(N)
 * Space: O(N)
 *
 */

#include<iostream>
#include<string>
#include <algorithm>
#include <utility>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::max;
using std::min;

const int MAX_TIMES = 180;
const int MAX_N = 1e6;

int left[MAX_TIMES + 1][MAX_N + 1];
int right[MAX_TIMES + 1][MAX_N + 1];

int costly_binary_search() {
    string S;
    cin >> S;
    const int n = S.length();
    for (int j = 0; j < n + 1; ++j) {
        left[0][j] = j;
        right[0][j] = j;
    }
    for (int c = 1; c <= MAX_TIMES; ++c) {
        for (int j = 0; j < n + 1; ++j) {
            left[c][j] = left[c - 1][j];
            right[c][j] = right[c - 1][j];
        }
        for (int j = 0; j < n; ++j) {
            const int cc = (c + '0') - S[j];
            if (cc >= 0) {
                const int l = left[cc][j];
                const int r = right[cc][j + 1];
                left[c][r] = min(left[c][r], l);
                right[c][l] = max(right[c][l], r);
            }
        }

        for (int j = n; j > 0; --j) {
            left[c][j - 1] = min(left[c][j - 1], left[c][j]);
        }
        for (int j = 0; j < n; ++j) {
            right[c][j + 1] = max(right[c][j + 1], right[c][j]);
        }

        if (right[c][0] == n) {
            return c;
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
