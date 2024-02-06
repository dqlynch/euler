#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;


int MOD = 1000000007;


void scannum(int &number)
{
    bool negative = false;
    int c;

    number = 0;
    c = getchar_unlocked();
    if (c == '-') {
        negative = true;
        c = getchar_unlocked();
    }

    for (; (c >= '0' && c <= '9'); c = getchar_unlocked()) {
        number = number * 10 + c - '0';
    }

    if (negative) {
        number *= -1;
    }
}


struct Node {
    int data;
    vector<int> siblings;
};


class Tree {
  private:
    int n;
    vector<Node> nodes;     // n nodes, in idx 1 -> n inclusive
    vector<int> parents;    // parent[node] is index of parent
    vector<int> ordered;    // All nodes in traversal order

  public:
    Tree(int num_nodes) : n(num_nodes), nodes(vector<Node>(n+1)) {}

    void populate(const vector<pair<int, int>>& edges) {
        for (const auto& [x, y] : edges) {
            nodes[x].data = x;
            nodes[x].siblings.push_back(y);
            nodes[y].data = y;
            nodes[y].siblings.push_back(x);
        }
    }

    void hang(int root_index) {
        parents = vector<int>(n+1, 0);
        ordered.reserve(n);

        // BFS to determine parenthood + an ordering of all nodes
        queue<pair<int, int>> bfs_q;   // node, parent
        bfs_q.push({1, 0});
        while (!bfs_q.empty()) {
            auto [node, parent] = bfs_q.front();
            bfs_q.pop();

            parents[node] = parent;
            ordered.push_back(node);

            for (int sibling : nodes[node].siblings) {
                if (sibling != parent) {
                    bfs_q.push({sibling, node});
                }
            }
        }
    }

    void hang() {
        hang(1);    // Default hang from node 1
    }

    const vector<Node>& get_nodes() { return nodes; }
    const vector<int>& get_parents() { return parents; }
    const vector<int>& get_ordered() { return ordered; }
};

uint64_t solve_query(const vector<int>& ordered,
                     const vector<int>& parents,
                     const vector<int>& query) {
    if (query.size() <= 1) {
        return 0;
    }

    int n = parents.size() - 1;
    uint64_t query_sum = 0;                 // sum of nodes in query
    vector<char> in_query(n + 1, false);    // fast membership check
    for (int x : query) {
        query_sum += x;
        in_query[x] = true;
    }
    vector<uint64_t> lineage(n + 1, 0);  // lineage[x] = sum(nodes in query who are descendants of x, including x)
    uint64_t ans = 0;

    for (auto it = ordered.rbegin(); it != ordered.rend(); ++it) {
        int x = *it;
        int parent = parents[x];

        if (in_query[x]) {
            lineage[x] += x;
        }
        lineage[parent] = lineage[parent] + lineage[x];

        uint64_t contr = (lineage[x] % MOD * (query_sum - lineage[x]) % MOD);
        ans = (ans + contr) % MOD;
    }

    return ans;
}

int main() {
    flockfile(stdin); // Use a single lock while reading all input
    int n, q;
    scannum(n);
    scannum(q);
    vector<pair<int, int>> edges;
    edges.reserve(n-1);
    for (int i = 0; i < n - 1; ++i) {
        int x, y;
        scannum(x);
		scannum(y);
        edges.push_back({x, y});
    }

    vector<vector<int>> queries(q);
    queries.reserve(q);
    for (int i = 0; i < q; ++i) {
        int k, x;
        scannum(k);
        for (int j = 0; j < k; ++j) {
            scannum(x);
            queries[i].push_back(x);
        }
    }
    funlockfile(stdin);

    // Populate edges into a tree so we can order from a root node
    Tree tree(n);
    tree.populate(edges);
    tree.hang();

    for (const auto& query : queries) {
        printf("%llu\n", solve_query(tree.get_ordered(), tree.get_parents(), query));
    }

    return 0;
}
