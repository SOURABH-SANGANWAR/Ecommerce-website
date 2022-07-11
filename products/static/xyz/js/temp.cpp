// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
    // Function to return Breadth First Traversal of given graph.
    vector<int> bfsOfGraph(int V, vector<int> adj[]) {
        set<int>myMap;
        queue<int>myQueue;
        vector<int>Ans;
        myMap.insert(0);
        myQueue.push(0);
        cout<<"done1"<<endl;
        while(myQueue.empty()==false){
            int node=myQueue.front();
            cout<<node<<endl;
            myQueue.pop();
            for(auto i:adj[node]){
                cout<<i<<endl;
                if(myMap.find(i)==myMap.end()){
                    myMap.insert(i);
                    myQueue.push(i);
                }
            }
            Ans.push_back(node);
        }
        return Ans;
    }
};

// { Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    while (tc--) {
        int V, E;
        cin >> V >>

            E;

        vector<int> adj[V];

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            // 		adj[v].push_back(u);
        }
        // string s1;
        // cin>>s1;
        Solution obj;
        vector<int> ans = obj.bfsOfGraph(V, adj);
        for (int i = 0; i < ans.size(); i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends