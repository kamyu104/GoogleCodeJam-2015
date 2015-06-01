// Copyright (c) 2015 kamyu. All rights reserved.

/*
 * Google Code Jam 2015 Round 2 - Problem C. Bilingual
 * https://code.google.com/codejam/contest/8234486/dashboard#s=p2
 *
 * Time  : O(N * W)
 * Space : O(N + W)
 *
 */

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

using std::cin;
using std::cout;
using std::endl;
using std::istringstream;
using std::string;
using std::vector;
using std::unordered_map;
using std::unordered_set;
using std::swap;

bool dfs(int node, int sink,
        vector<bool> *used_ptr,
         vector<vector<int>> *E_ptr) {
    vector<bool>& used = *used_ptr;
    vector<vector<int>>& E = *E_ptr;

    if (used[node]) {
        return false;
    }
    used[node] = true;
    for (auto it = E[node].begin(); it != E[node].end(); ++it) {
        auto x = *it;
        if (x == sink || dfs(x, sink, &used, &E)) {
            E[x].emplace_back(node);
            swap(E[node].back(), *it);
            E[node].pop_back();
            return true;
        }
    }
    return false;
}

int bilingual() {
    int N;
    cin >> N;

    string ss; getline(cin, ss);
    unordered_map<string, int> values;
    auto get = [&values](string s) {
        if (values.count(s)) {
            return values[s];
        }
        return (values[s] = values.size());
    };

    // Parse lines.
    vector<unordered_set<int>> lines(N);
    for (int i = 0; i < N; ++i) {
        string line; getline(cin, line);
        istringstream in(line);
        string word;
        while (in >> word) {
            lines[i].emplace(get(word));
        }
    }

    // Init edges.
    int source = 0, sink = 1;
    vector<vector<int>> E(2 * values.size() + N);
    for (int i = 0; i < values.size(); ++i) {
        E[2 * i + N].emplace_back(2 * i + N + 1);
    }
    for (const auto &x : lines[0]) {
        E[source].emplace_back(2 * x + N);
    }
    for (const auto &y : lines[1]) {
        E[2 * y + N + 1].emplace_back(sink);
    }
    for (int i = 2; i < N; ++i) {
        for (const auto &x : lines[i]) {
            E[2 * x + N + 1].emplace_back(i);
            E[i].emplace_back(2 * x + N);
        }
    }

    // Run max flow.
    int flow = 0;
    vector<bool> used(E.size(), false);
    while (dfs(source, sink, &used, &E)) {
        ++flow;
        used = move(vector<bool>(E.size(), false));
    }
    return flow;
}

int main() {
    int T;
    cin >> T;

    for (int test = 1; test <= T; ++test) {
        cout << "Case #" << test << ": " << bilingual() << endl;
    }
}
