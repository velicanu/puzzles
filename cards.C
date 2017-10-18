#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

float mean(vector<int> x) {
  float sum = 0 ;
  for(unsigned i = 0 ; i < x.size() ; ++i) {
    sum+=x[i];
  }
  return sum/(float)x.size();
}

float median(vector<int> x) {
  vector<int> y = x;
  sort(y.begin(), y.end());
  if(x.size() % 2 == 0) return y[x.size()/2];
  else                  return 0.5 * ( y[x.size()/2] +  y[(x.size()/2) + 1]);
}

int main() 
{
  vector<int> x;
  for(int i = 0 ; i<52 ; ++i) {
    if(i%2==0) x.push_back(1);
    else       x.push_back(-1);
  }
  vector<int> maxes;
  for(int j = 0 ; j < 10000 ; ++j) {
    int max = 0 , sum = 0;
    random_shuffle ( x.begin() , x.end() ) ;
    for(int i = 0 ; i < 52 ; ++i) {
      sum+=x[i];
      if(sum > max) max = sum;
    }
    maxes.push_back(max);
  }
  cout<<mean(maxes)<<endl;
  cout<<median(maxes)<<endl;
  return 0;
}


