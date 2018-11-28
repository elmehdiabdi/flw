#include<bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	while(t--){
		int n,x;
		cin>>n>>x;
		int ar[n];
		int sum = 0;
		for(int i=0;i<n;i++){
			cin>>ar[i];
			sum += ar[i];
		}
		cout<<sum<<" and "<<x<<endl;
	}
	return 0;
}