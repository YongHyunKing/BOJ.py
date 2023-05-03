#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

string s;
int n = 0;
int d = 1;
vector<int> sa;
vector<int> group;
vector<int> tmp;

bool cmp(int a, int b){
    if (group[a] == group[b]) return group[min(a+d,n)] < group[min(b+d,n)];
    
    return group[a]<group[b];
}

int main(){
    ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

    cin>>s;
    n = s.size();

    for(int i=0;i<n;i++){
        sa.push_back(i);
        group.push_back(int(s[i]));
        tmp.push_back(0);
    }
    
    group.push_back(-1);
    s.push_back('$');

    while(d<n){
        sort(sa.begin(),sa.end(),cmp);
        // for(int i=0;i<n;i++) cout<<sa[i]<<' ';
        // cout<<'\n';
        for(int i=0;i<n-1;i++) tmp[i+1]=tmp[i] + cmp(sa[i],sa[i+1]);
        for(int i=0;i<n;i++) group[sa[i]] = tmp[i];
        
        if(tmp[n-1]==n-1) break;

        d<<=1;
    }

    vector<int> lcp(n-1);
    int k=0;
    for(int i=0;i<n;i++, k=max(k-1,0)){
        if(group[i]==n-1) continue;

        int j = sa[group[i]+1];
        while(s[i+k]==s[j+k]) k++;
        lcp[group[i]] = k;
    }

    long long ans = n - sa[n-1];
    for(int i=0;i<n-1;i++) ans+= n - sa[i] - lcp[i];
    cout<<ans;

}
