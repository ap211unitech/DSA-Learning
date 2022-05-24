// class Solution
// {
//     int dp[1001][1001];
//     string answer(string s, int n)
//     {

//         int c = 0;

//         for (int i = 0; i < n; i++)
//         {
//             for (int j = 0; j < n; j++)
//             {
//                 if (j + c < n)
//                 {
//                     if (c == 0)
//                         dp[j][j + c] = 1;
//                     else if (c == 1)
//                     {
//                         if (s[j] == s[j + c])
//                         {
//                             dp[j][j + c] = 1;
//                         }
//                         else
//                         {
//                             dp[j][j + c] = 0;
//                         }
//                     }
//                     else
//                     {
//                         if (s[j] == s[j + c])
//                         {
//                             if (dp[j + 1][j + c - 1] == 1)
//                             {
//                                 dp[j][j + c] = 1;
//                             }
//                             else
//                             {
//                                 dp[j][j + c] = 0;
//                             }
//                         }
//                     }
//                 }
//             }
//             c += 1;
//         }

//         int initial = 0;
//         int length = 0;

//         for (int i = 0; i < n; i++)
//         {
//             int start = -1;
//             int end = -1;
//             for (int j = i; j < n; j++)
//             {
//                 if (dp[i][j] == 1)
//                 {
//                     if (start == -1)
//                         start = i;
//                     end = j;
//                 }
//             }
//             if (end - start + 1 > length)
//             {
//                 length = end - start + 1;
//                 initial = i;
//             }
//         }

//         return s.substr(initial, length);
//     }

// public:
//     string longestPalindrome(string s)
//     {
//         memset(dp, 0, sizeof(dp));
//         return answer(s, s.size());
//     }
// };
