// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 Round 1B - Problem C. Hiking Deer
 * https://code.google.com/codejam/contest/8224486/dashboard#s=p2
 *
 * Time  : O(HlogH), H is number of hikers.
 * Space : O(H)
 *
 */

#include <iostream>
#include <vector>
#include <set>
#include <utility>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::vector;
using std::set;
using std::pair;
using std::tie;
using std::min;

int Encounters(vector<pair<int64_t, int64_t>> *H) {
    vector<int64_t> times;
    for (auto &h : *H) {
        h.first *= h.second;
        h.second *= 360;
        // Push the remaining time to end the trail.
        times.emplace_back(h.second - h.first);
    }
    sort(times.begin(), times.end());


    set<pair<int64_t, int>> when;
    for (int i = 0; i < static_cast<int>(H->size()); ++i) {
        const auto h = (*H)[i];
        when.emplace(h.second - h.first, i);
    }

    int answer = H->size();
    int overtake = H->size(), undertake = 0;
    vector<int> many(H->size(), 0);
    for (auto &x : times) {
        while (when.begin()->first <= x && undertake < answer) {
            int64_t time; int whom; tie(time, whom) = *when.begin();
            when.erase(when.begin());
            if (many[whom] == 0) {
                // Decrease the number of the encounters
                // which the deer has to overtake.
                --overtake;
            } else {
                // Increase the number of the encounters
                // which the deer undertakes.
                ++undertake;
            }
            ++many[whom];
            // Push the next time to end the trail.
            when.emplace(time + (*H)[whom].second, whom);
        }
        answer = min(answer, overtake + undertake);
        if (undertake >= answer) {
            break;
        }
    }

    return answer;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        int N;
        cin >> N;

        vector<pair<int64_t, int64_t>> H;
        for (int i = 0; i < N; ++i) {
            int D, K, M; cin >> D >> K >> M;
            for (int j = 0; j < K; ++j) {
                H.emplace_back(D, M + j);
            }
        }

        cout << "Case #" << test << ": " << Encounters(&H) << endl;
    }
}
