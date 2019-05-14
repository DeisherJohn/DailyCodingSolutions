/*#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Serialize binary tree
#   Daily Problem #: 3
#   Author: John Deisher
#   Date Started: 4/25/19
#   Date Finished: 4/25/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), 
which serializes the tree into a string, 
and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

   Tree Structure

                root
            /             \
           left            right
        /       \
    left.left   null
"""*/

#include <string>
#include <iostream> 
#include <list>

using namespace std;

class node{
public:
    string value;
    node *left;
    node *right;

    node(){
        value = "NULL";
        left = NULL;
        right = NULL;

    }
    ~node();

    void Build_Node(string val, node * left_node, node * right_node){
        value = val;
        left = left_node;
        right = right_node;
    }
};

string serialize(node * root){
    string myString = "";
    string leftString = "";
    string rightString = "";

    if (root->left != NULL){ 
        leftString = serialize(root->left);
    } else {
        leftString = "NULL";
    }
    if (root->right != NULL){ 
        rightString = serialize(root->right);
    } else {
        rightString = "NULL";
    }

    myString = root->value + ";" + leftString + ";" + rightString;
    return myString;
}

node * deserialize(string * s){
    if (s->size() == 0){
        return NULL;
    }

    string myString = "";
    node * myNode = new node();
    while(s->size() > 0){
        if(s->at(0) == ';'){
            //end of name
            if(myString != "NULL"){
                myNode->value = myString;
                myString = "";
            } else {
                return NULL;
            }
            s = &s->replace(0,1,"");
            myNode->left = deserialize(s);
            s = &s->replace(0,1,"");
            myNode->right = deserialize(s);
            return myNode;
        } else {
            myString += s->at(0);
            s = &s->replace(0,1,"");
        }
        
    }
    return myNode;
}


int main(int argc, char const *argv[])
{
    node * root = new node();
    node * left = new node();
    node * right = new node();
    node * leftleft = new node();

    
    leftleft->Build_Node("leftleft", NULL, NULL);
    left->Build_Node("left", leftleft, NULL);
    right->Build_Node("right", NULL, NULL);
    root->Build_Node("root", left, right);

    //cout << root->right->value << endl;

    serialize(root);
    string data = serialize(root);
    string * testSent = &data;
    node * newRoot = deserialize(testSent);

    if (newRoot->left->left->value == root->left->left->value){
        cout << "Tree structures match" << endl;
    } else {
        cout << "Trees did not match" << endl;
    }
    return 0;
}