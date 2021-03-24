#include "queue.h"
#include "iostream"

using namespace std;

struct Node {
  int key;
  Node* next;
};

Queue::Queue() {
  this->front_ = NULL;
  this->back_ = NULL;
}

void Queue::push(int k) {
  Node* novo_no = new Node;
  novo_no->key = k;
  novo_no->next = NULL;

  if(front_ == NULL){
    front_ = novo_no;
    back_ = novo_no;    
  }
  else{
    back_->next = novo_no;
    back_ = novo_no;
  }
}

void Queue::pop() {
  Node* temp = front_;
  if(front_ == NULL) throw EmptyException();
  front_ = front_->next;

  //return temp->key;
}

int Queue::front() const {
  if(front_ == NULL) throw EmptyException();
  return front_->key;
  //return 0;
}

int Queue::back() const {
  Node* cabeca = front_;
  if(front_ == NULL) throw EmptyException();
  if(cabeca->next == NULL){
    return cabeca->key;
  }
  else{
    while(cabeca->next != NULL){
      cabeca = cabeca->next;
    }
    return cabeca->key;
  //return 0;
  }
  
}

int Queue::count() const {
  Node* cabeca = front_;
  int contador = 0;
  if(front_ == NULL){
    return contador = 0;
  }
  else if(front_ == back_){
    return contador = 1;
  }
  else{
    contador = 1;
    while(cabeca->next != NULL){
      cabeca = cabeca->next;
      contador++;
    }
    return contador;
  }
  
  
  //return 0;
}

bool Queue::estaVazio() {
  return (front_ == NULL);
}