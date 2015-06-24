// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 Round 3 - Problem C. Runaway Quail
 * https://code.google.com/codejam/contest/4254486/dashboard#s=p2
 *
 * Time  : O(N^3)
 * Space : O(N^2)
 *
 */

#include <iostream>
#include <vector>
#include <limits>
#include <algorithm>
#include <utility>

using std::cin;
using std::cout;
using std::ios;
using std::endl;
using std::vector;
using std::numeric_limits;
using std::pair;
using std::max;
using std::min;

void representive_quails(vector<pair<int, int>> *quails_ptr) {
    auto& quails = *quails_ptr;
    int k = 0;

    // Sort by position.
    sort(quails.begin(), quails.end());

    // Simplify quails by strictly decreasing speed.
    for (int i = 0; i < quails.size(); ++i) {
        while (k > 0 && quails[i].second >=
               quails[k - 1].second) {
            --k;
        }
        quails[k++] = quails[i];
    }
    // Only keep representive quails.
    quails.resize(k);
}

double catch_time(const int Y, const double t,
           const pair<int, int> quail) {
    return (t * quail.second + quail.first) / (Y - quail.second);
}

double runaway_quail() {
    int Y, N;
    cin >> Y >> N;
    vector<int> P(N), S(N);
    for (int i = 0; i < N; ++i) {
        cin >> P[i];
    }
    for (int i = 0; i < N; ++i) {
        cin >> S[i];
    }

    vector<pair<int, int>> left_quails, right_quails;
    for (int i = 0; i < N; ++i) {
        if (P[i] < 0) {
            left_quails.emplace_back(pair<int, int>(-P[i], S[i]));
        } else {
            right_quails.emplace_back(pair<int, int>(P[i], S[i]));
        }
    }
    representive_quails(&left_quails), representive_quails(&right_quails);
    vector<vector<double>> time(left_quails.size() + 1,
                             vector<double>(right_quails.size() + 1,
                             numeric_limits<double>::max()));
    time[0][0] = 0;

    // Dynamic programming
    double min_time = numeric_limits<double>::max();
    for (int i = 0; i <= left_quails.size(); ++i) {
        for (int j = 0; j <= right_quails.size(); ++j) {
            double t = 0, T = time[i][j];
            for (int k = j; k < right_quails.size(); ++k) {
                t = max(t, catch_time(Y, T, right_quails[k]));
                // Update time to catch right_quails[k],
                // and goes back to position zero.
                // It costs 2t.
                time[i][k + 1] = min(time[i][k + 1], T + 2 * t);
            }
            // No need to go back to position zero for the last one, it costs t.
            if (i == left_quails.size()) {
                min_time = min(min_time, T + t);
            }

            t = 0;
            for (int k = i; k < left_quails.size(); ++k) {
                t = max(t, catch_time(Y, T, left_quails[k]));
                // Update time to catch left_quails[k],
                // and goes back to position zero.
                // It costs 2t.
                time[k + 1][j] = min(time[k + 1][j], T + 2 * t);
            }
            // No need to go back to position zero for the last one, it costs t.
            if (j == right_quails.size()) {
                min_time = min(min_time, T + t);
            }
        }
    }
    return min_time;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(15);
        cout << "Case #" << test << ": " << runaway_quail() << endl;
    }
    return 0;
}
