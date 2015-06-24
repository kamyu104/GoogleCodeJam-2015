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

void cor(vector<pair<int, int>> *direction_ptr) {
    auto& direction = *direction_ptr;
    int k = 0;
    sort(direction.begin(), direction.end());
    for (int i = 0; i < direction.size(); ++i) {
        while (k > 0 && direction[i].second >=
               direction[k - 1].second) {
            --k;
        }
        direction[k++] = direction[i];
    }
    direction.resize(k);
}

double get(const int Y, const double t0,
           const pair<int, int> p) {
    return (t0 * p.second + p.first) / (Y - p.second);
}

void relax(const int i, const int j,
           const double F,
           vector<vector<double>> *f) {
    (*f)[i][j] = min((*f)[i][j], F);
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

    vector<pair<int, int>> left, right;
    for (int i = 0; i < N; ++i) {
        (P[i] < 0 ? left : right).emplace_back(pair<int, int>(abs(P[i]), S[i]));
    }
    cor(&left), cor(&right);  // O(NlogN)
    vector<vector<double>> f(left.size() + 1,
                             vector<double>(right.size() + 1,
                             numeric_limits<double>::max()));
    f[0][0] = 0;

    double ans = numeric_limits<double>::max();
    for (int i = 0; i <= left.size(); ++i) {
        for (int j = 0; j <= right.size(); ++j) {
            double ma = 0, F = f[i][j];
            for (int k = j; k < right.size(); ++k) {
                ma = max(ma, get(Y, F, right[k]));
                relax(i, k + 1, F + 2 * ma, &f);
            }
            if (i == left.size()) {
                ans = min(ans, F + ma);
            }

            ma = 0;
            for (int k = i; k < left.size(); ++k) {
                ma = max(ma, get(Y, F, left[k]));
                relax(k + 1, j, F + 2 * ma, &f);
            }
            if (j == right.size()) {
                ans = min(ans, F + ma);
            }
        }
    }
    return ans;
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
