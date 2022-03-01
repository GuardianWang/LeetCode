#include <iostream>
#include <memory>
#include <unordered_map>
#include <string>

using namespace std;

// reserve
// size
// count: 1 or 0
// []
// erase
// find
// clear

int main()
{
    // using CharCounter = unordered_map<char, int>;
    using CharCounter = map<char, int>;
    CharCounter c2n;
    // reserve works for unordered_map
    // c2n.reserve(26);

    // counter
    string s = "aabbc";
    for (auto c : s) {
        if (0 == c2n.count(c)) {
            c2n[c] = 0;
        } 
        c2n[c] += 1;
    }
    
    // remove occurrence
    string s2 = "abc";
    for (auto c : s2) {
        if (c2n.find(c) != c2n.end()) {
            --c2n[c];
            if (0 == c2n[c]) {
                c2n.erase(c);
            }
        }
    }
    
    for (auto p : c2n) { 
        cout << p.first << " " << p.second << endl;
    }
    c2n.clear();

}
