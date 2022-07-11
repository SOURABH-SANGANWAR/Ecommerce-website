
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution {
  public:
vector<int> bfsOfGraph(int V, vector<int> adj[]) {
       unordered_map<int, bool> umap;
       cout<<"start"<<(umap[0]!=true)<<endl;
       vector<int> ans;
       queue<int> q;
       cout<<"start"<<(umap[0]!=true)<<endl;
       q.push(0);
       while(!q.empty())
       {
        cout<<"start"<<(umap[0]!=true)<<endl;
           int node=q.front();
           q.pop();
           ans.push_back(node);
           cout<<node<<endl;
           for(auto i: adj[node])
           {cout<<i<<endl;
               if(umap[i]!=true)
               {
                   q.push(i);
                   umap[i]=true;
               }
           }
           cout<<"end"<<(umap[0]!=true)<<endl;
       }
       return ans;
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