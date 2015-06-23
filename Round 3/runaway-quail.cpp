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

void cor(vector<pair<int, int>> *a_ptr) {
    auto& a = *a_ptr;
    int k = 0;
    sort(a.begin(), a.end());
    for (int i = 0; i < a.size(); ++i) {
        while (k > 0 && a[i].second >= a[k - 1].second) {
            --k;
        }
        a[k++] = a[i];
    }
    a.resize(k);
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

    vector<pair<int, int>> a, b;
    for (int i = 0; i < N; ++i) {
        (P[i] < 0 ? a : b).emplace_back(pair<int, int>(abs(P[i]), S[i]));
    }
    cor(&a), cor(&b);  // O(NlogN)
    vector<vector<double>> f(a.size() + 1,
                             vector<double>(b.size() + 1,
                             numeric_limits<double>::max()));
    f[0][0] = 0;

    double ans = numeric_limits<double>::max();
    for (int i = 0; i <= a.size(); ++i) {
        for (int j = 0; j <= b.size(); ++j) {
            double ma = 0, F = f[i][j];
            for (int k = j; k < b.size(); ++k) {
                ma = max(ma, get(Y, F, b[k]));
                relax(i, k + 1, F + 2 * ma, &f);
            }
            if (i == a.size()) {
                ans = min(ans, F + ma);
            }

            ma = 0;
            for (int k = i; k < a.size(); ++k) {
                ma = max(ma, get(Y, F, a[k]));
                relax(k + 1, j, F + 2 * ma, &f);
            }
            if (j == b.size()) {
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
