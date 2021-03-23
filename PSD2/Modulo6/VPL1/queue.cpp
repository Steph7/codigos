#include "queue.h"
#include "iostream"
#include "vector"

using namespace std;

struct Node {
  int key;
  Node* next;
};

Queue::Queue() {
  // TODO
  vector<Node> Fila;
}

void Queue::push(int k) {
  // TODO
  Node* no = new Node;
  no->key = k;
}

void Queue::pop() {
  // TODO
}

int Queue::front() const {
  return 0; // TODO
}

int Queue::back() const {
  return 0; // TODO
}

int Queue::count() const {
  return 0; // TODO
}