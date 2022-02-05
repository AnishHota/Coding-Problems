class Solution {
public:
    int getSum(int a, int b) {
        unsigned int x,y,sum,carry;
        x=a;
        y=b;
        sum=x^y;
        carry=x&y;
        carry=carry<<1;
        x=sum;
        y=carry;
        while(carry!=0)
        {
            sum=x^y;
            carry=x&y;
            carry=carry<<1;
            x=sum;
            y=carry;
        }
        return sum;
    }
};
