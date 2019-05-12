/*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Program: Find sum in list
    Daily Problem #: 1
    Author: John Deisher
    Date Finished: 5/13/19
    Notes: complete in a single pass, 
          idea for solution comes from Google Mock interview video on youtube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
*/


#include <iostream> 
#include <vector> 
#include <unordered_set> 
#include <set> 
#include <ctime>
#include <chrono>

#define COUNT 10000000

using namespace std;

bool findSum_unorderedset(vector<double> input, int sumToFind){
    unordered_set<double> complement_list;

    for (double i = 0; i < input.size(); ++i){
        if(complement_list.find(input[i]) != complement_list.end()){
            return true;
        } else {
            complement_list.insert(sumToFind - input[i]);
        }
    }

    return false;
}

bool findSum_set(vector<double> input, int sumToFind){
    set<double> complement_list;

    for (double i = 0; i < input.size(); ++i){
        if(complement_list.find(input[i]) != complement_list.end()){
            return true;
        } else {
            complement_list.insert(sumToFind - input[i]);
        }
    }

    return false;
}

int main(){
    vector<double> testList; 

    for (double i = 0; i < COUNT; ++i){
        testList.push_back(i);
    }

    auto start = std::chrono::system_clock::now();

    bool test1 = findSum_set(testList, COUNT + COUNT /2);

    auto mid = std::chrono::system_clock::now();

    bool test2 = findSum_unorderedset(testList, COUNT + COUNT /2);

    auto end = std::chrono::system_clock::now();

    cout << "Test are done on data set of " << COUNT << " items" << endl;
    std::chrono::duration<double> elapsed_seconds1 = mid-start;
    cout << "Using Set: " << elapsed_seconds1.count() << endl;

    std::chrono::duration<double> elapsed_seconds2 = end-mid;
    cout << "Using Unordered Set: " << elapsed_seconds2.count() << endl;

    if(test1 and test2){
        cout << "Match Found" << endl;
    } else {
        cout << "No Match Found" << endl;
    }
    return 0;
}

/*
sets have a find time complexity of O(log(n)) meaning that the overall complexity of 
using a set would be O(n*log(n))

Unordered sets have a find complexity of O(1) which is much better, leading to 
a much better overall time complexity of O(n) 

Output:

-------MATCH POSSIBLE -----------
Test are done on data set of 10000000 items
Using Set: 20.2891
Using Unordered Set: 12.6996
Match Found
[Finished in 35.0s]

------- NO MATCH POSSIBLE ---------
Test are done on data set of 10000000 items
Using Set: 27.5014
Using Unordered Set: 18.2943
No Match Found
[Finished in 47.9s]

*/