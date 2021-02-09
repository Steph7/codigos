// Fonte código: https://youtu.be/30z6u2PpVI8
#include <iostream>
#include <queue>

using namespace std;

int main(){
    priority_queue<int> pq;

    pq.push(10);
    pq.push(30);
    pq.push(50);
    pq.push(70);

    cout << pq.top() << endl;
    cout << pq.size() << endl;
    
    return 0;
}