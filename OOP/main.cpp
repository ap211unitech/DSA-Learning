#include <bits/stdc++.h>

using namespace std;

class Human
{

public:
    static int count;
    Human()
    {
        count++;
    }
    void display()
    {
        cout << "Count " << count << endl;
    }
};

int Human::count = 0;

int main()
{
    Human Arjun;
    Arjun.display();

    Human Arun;
    Arun.display();

    Human Aru;
    Aru.display();

    return 0;
}