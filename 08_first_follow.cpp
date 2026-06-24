#include <bits/stdc++.h>
using namespace std;

map<string, vector<vector<string>>> G;
map<string, set<string>> FIRST, FOLLOW;
string start;

bool isNT(const string &s) {
    return G.find(s) != G.end();
}

/* ================= FIRST ================= */
set<string> computeFirst(string X) {

    if (!isNT(X)) {
        return {X};  // terminal
    }

    if (!FIRST[X].empty()) return FIRST[X];

    set<string> res;

    for (auto &prod : G[X]) {

        bool epsilonPossible = true;

        for (auto &sym : prod) {

            set<string> f = computeFirst(sym);

            for (auto &x : f) {
                if (x != "#")
                    res.insert(x);
            }

            if (f.find("#") == f.end()) {
                epsilonPossible = false;
                break;
            }
        }

        if (epsilonPossible)
            res.insert("#");
    }

    FIRST[X] = res;
    return res;
}

/* ================= FOLLOW ================= */
void computeFollow() {

    FOLLOW[start].insert("$");

    bool changed = true;

    while (changed) {
        changed = false;

        for (auto &[A, prods] : G) {

            for (auto &prod : prods) {

                for (int i = 0; i < prod.size(); i++) {

                    string B = prod[i];

                    if (!isNT(B)) continue;

                    set<string> firstBeta;
                    bool epsilon = true;

                    for (int j = i + 1; j < prod.size(); j++) {

                        set<string> f = computeFirst(prod[j]);

                        for (auto &x : f)
                            if (x != "#")
                                firstBeta.insert(x);

                        if (f.find("#") == f.end()) {
                            epsilon = false;
                            break;
                        }
                    }

                    int before = FOLLOW[B].size();

                    FOLLOW[B].insert(firstBeta.begin(), firstBeta.end());

                    if (epsilon || i == prod.size() - 1) {
                        FOLLOW[B].insert(FOLLOW[A].begin(), FOLLOW[A].end());
                    }

                    if (FOLLOW[B].size() != before)
                        changed = true;
                }
            }
        }
    }
}

/* ================= MAIN ================= */
int main() {

    cout << "Enter grammar (space-separated). End with empty line:\n";

    string line;

    while (getline(cin, line) && !line.empty()) {

        stringstream ss(line);

        string lhs, arrow;
        ss >> lhs >> arrow;  // A ->

        if (start.empty()) start = lhs;

        vector<string> prod;
        string token;

        while (ss >> token) {

            if (token == "|") {
                if (prod.empty()) prod.push_back("#");
                G[lhs].push_back(prod);
                prod.clear();
            }
            else {
                prod.push_back(token);
            }
        }

        if (prod.empty()) prod.push_back("#");
        G[lhs].push_back(prod);
    }

    if (G.empty()) {
        cout << "No grammar input.\n";
        return 0;
    }

    /* Compute FIRST */
    for (auto &[nt, _] : G)
        computeFirst(nt);

    /* Compute FOLLOW */
    computeFollow();

    /* Print FIRST */
    cout << "\nFIRST sets:\n";
    for (auto &[nt, s] : FIRST) {
        cout << "FIRST(" << nt << ") = {";
        int size = s.size(), i = 1;
        for (auto &x : s){
            if (i < size)
                cout << x << ", ";
            else
                cout << x;
            i++;
        }
        cout << "}\n";
    }

    /* Print FOLLOW */
    cout << "\nFOLLOW sets:\n";
    for (auto &[nt, s] : FOLLOW) {
        cout << "FOLLOW(" << nt << ") = {";
        int size = s.size(), i = 1;
        for (auto &x : s){
            if (i < size)
                cout << x << ", ";
            else
                cout << x;
            i++;
        }
        cout << "}\n";
    }

    return 0;
}