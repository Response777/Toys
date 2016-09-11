#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <queue>
using namespace std;

const int ls = 1;
const int rs = 0;
const int MAX_DEPTH = 15;
const int TARGET_LEVEL = 100000;

int rand(int seed)
{
    return (seed*17207+22721)%131027;
}


int move(char dir,int level)
{
    return rand(level+(dir=='L'?ls:rs))%(TARGET_LEVEL+1);
}

int levels[TARGET_LEVEL+1];
void bfs()
{
    // cout << "Let's try "
    std::vector<char>v;
    v.resize(TARGET_LEVEL+1);

    queue<int>Q;
    Q.push(1);

    for(int i=0;i<TARGET_LEVEL+1;i++)
        levels[i]=-1;

    int max_value = 0;
    int level = 1;
    levels[1]=0;

    while(level != TARGET_LEVEL and not Q.empty())
    {
        level = Q.front();
        Q.pop();

        max_value = max(max_value,level);

        int l = move('L',level);
        int r = move('R',level);

        if(levels[l]==-1)
        {
            Q.push(l);
            levels[l]=level;
            v[l]='L';
        }

        if(levels[r]==-1)
        {
            Q.push(r);
            levels[r]=level;
            v[r]='R';   
        }
    }

    cout << "level:" << level << endl;
    cout << "Max:  " << max_value << endl;
    while(level!=1)
    {
        cout<<levels[level]<<" , "<<v[level]<<endl;
        level=levels[level];
    }
}

void valid()
{
    int level = 1;
    char dirs[] = "RRLLLRLRRLRRRLRR";
    for(int i=0;i<MAX_DEPTH+1;i++)
    {
        level = move(dirs[i],level);
    }
    cout << level << endl;
}

void dfs(int level,int depth)
{
    if(depth==MAX_DEPTH)
    {
        if(level==TARGET_LEVEL)
        {
            cout << level << endl;
        }
        return;
    }

    dfs(move('L',level),depth+1);
    dfs(move('R',level),depth+1);
}

void play()
{
    char dir;
    int level = 1;
    while(level!=TARGET_LEVEL)
    {
        cin >> dir;
        level = move(dir,level);
        cout << "Level = " << level << endl;
    }
}

int main(int argc,char** argv)
{   
    // bfs();
    valid();
    // play();
    
    // There are only 2 solution for depth no more than 5, one is begined with L, and the other is begined with R
    // LRRRR & RLRRR
    // 1 26 39 10 45 // 1 90 39 10 45
    // +32 
    // cout << "begin with R" << endl;
    // dfs(move('R',1),0);

    // NOW it's updated so that it's 100000 levels.
    // ANSWER is RRLLLRLRRLRRRLRR

    // cout << "begin with L" << endl;
    // dfs(move('L',1),0);
    return 0;
}