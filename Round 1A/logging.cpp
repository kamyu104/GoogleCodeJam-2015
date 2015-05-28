// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 Round 1A - Problem C. Logging
 * https://code.google.com/codejam/contest/4224486/dashboard#s=p2
 *
 * Time  : O(N^2)
 * Space : O(N)
 *
 */

#include <iostream>
#include <vector>
#include <cmath>
#include <utility>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::pair;
using std::min;

const long double eps = 1e-15;

void logging() {
    int N;
    cin >> N;
    vector<pair<int, int>> coordinates;
    for (int i = 0; i < N; ++i) {
        int X, Y;
        cin >> X >> Y;
        coordinates.emplace_back(X, Y);
    }

    for (int i = 0; i < N; ++i) {
        vector<long double> angles;
        for (int j = 0; j < N; ++j) {
            if (j != i) {
                angles.emplace_back(
                        atan2l(coordinates[j].second - coordinates[i].second,
                               coordinates[j].first - coordinates[i].first));
            }
        }
        sort(angles.begin(), angles.end());

        int angle_count = angles.size();
        for (int i = 0; i < angle_count; ++i) {
            angles.emplace_back(angles[i] + 2 * M_PI);
        }

        int min_remove = N - 1;
        int start = 0, end = 0;
        for (int i = 0; i < angles.size() / 2; ++i) {
            while (start + 1 < angles.size() &&
                   angles[start] - angles[i] < eps) {
                ++start;
            }
            while (end < angles.size() &&
                   angles[end] - angles[i] < M_PI - eps) {
                ++end;
            }
            min_remove = min(min_remove, end - start);
        }
        cout << min_remove << endl;
    }
}

int main() {
    int T;
    cin >> T;
    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ":" << endl;
        logging();
    }
    return 0;
}
