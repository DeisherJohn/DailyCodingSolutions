/*#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Find product of list
#   Daily Problem #: 2
#   Author: John Deisher
#   Date Started: 5/7/19
#   Date Finished: 5/7/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

Follower Answer: 

Use a doubly linked list of nodes that carry the product of the nodes before and after them. 
once it is built it only requires one pass to get the list back of all nodes with no division
"""
*/

#include <vector>
#include <iostream> 

using namespace std;

vector<int> get_product(vector<int> v){
    vector<int> return_vector;
    int right_product = 1;
    return_vector.push_back(1);

    for(int i = 0 ; i < v.size() - 1 ; i++){
        //int new_product = left_product[i-1] * v[i-1];
        return_vector.push_back(return_vector[i] * v[i]);
    }

    for(int i = v.size() - 1 ; i >= 0 ; i--){
        right_product *= v[i];
        return_vector[i-1] *= right_product;
    }
    return return_vector;

}

int main(){
    vector<int> v;

    for (int i = 1; i < 6; ++i)
    {
        /* code */
        v.push_back(i);
    }

    vector<int> new_v = get_product(v);

    for (int i = 0; i < new_v.size(); ++i)
    {
        /* code */
        cout << new_v[i] << ", ";
    }
    cout << endl;

    
    return 0;
}