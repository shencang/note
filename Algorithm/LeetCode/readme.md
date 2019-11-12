# 力扣

[直达链接](https://leetcode-cn.com/problemset/all/)

## 1.给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标

```text
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
```

* 示例:

```text
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
```

```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length-1; i++) {
            for (int j = nums.length-1; j >= 0; j--) {
                if ((nums[i] + nums[j]) == target) {
                    if (i!=j){
                        return new int[]{i, j};
                    }

                }
            }
        }

        return null;
    }
}
```

## 2.给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字

```text
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
```

* 示例：

```text
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
```

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode rootNode = new ListNode(0);
        ListNode result =  rootNode;
        int num = 0;
        int sumVal;
        while (l1 !=null||l2 !=null||num!=0){
            sumVal = (l1 != null ?l1.val:0)+(l2 != null ?l2.val:0)+num;
            num = sumVal/10;
            ListNode sumNode = new ListNode(sumVal%10);
            result.next= sumNode;
            result = sumNode;
            if(l1 != null) l1 = l1.next;
            if(l2 != null) l2 = l2.next;

        }
        return rootNode.next;
    }
}
```

## 3.给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度

* 示例 1:

```text
    输入: "abcabcbb"
    输出: 3
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
```

* 示例 2:

```text
    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
```

* 示例 3:

```text
    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
```

```java
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(),result =0;
        Map<Character,Integer>map  = new HashMap<>();
        for (int i=0 ,j =0;j<n;j++){
            if (map.containsKey(s.charAt(j))){
               // i = map.get(s.charAt(j))>i?map.get(s.charAt(j)):i;
                i = Math.max(map.get(s.charAt(j)),i);
            }
            result = Math.max(result, (j - i + 1));
            map.put(s.charAt(j),j+1);
        }
        return result;

    }
}

```

## 4.给定两个大小为 m 和 n 的有序数组 nums1 和 nums2

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

* 示例 1:

```text
    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0
```

* 示例 2:

```text
    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5
```

**(扯犊子流解法，用Collections居然给过，就是运算有点慢，实际效率不高达不到log（n+m），后续重写吧)**
**请参考官方给的解法**

```java

class Solution {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        List<Integer> numList = new ArrayList<>();
        for (int i : nums1) {
            numList.add(i);
        }
        for (int i : nums2) {
            numList.add(i);
        }
        Collections.sort(numList);
        return numList.size() % 2 == 0 ? ((numList.get(numList.size() / 2-1) + numList.get(numList.size() / 2 )) / 2.0) : numList.get(numList.size() / 2 );


    }
}
```

## 5.给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000

* 示例 1：

```text
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
```

* 示例 2：

    输入: "cbbd"
    输出: "bb"

```java
package 其他测试题;

import java.lang.reflect.Array;
import java.util.*;
import java.io.*;
import java.lang.*;

public class FindWay {
    public static void main(String[] args) {
        System.out.println("test");
        Solution solution = new Solution();
        System.out.println(solution.longestPalindrome("babad"));

    }


}


class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() < 1) {
            return "";
        }
        int begin = 0, end = 0;
        for (int i = 0; i < s.length(); i++) {
            int sl1 = nextChar(s, i, i);
            int sl2 = nextChar(s, i, i + 1);
            int sl = Math.max(sl1, sl2);
            if (sl > end - begin) {
                begin = i - (sl - 1) / 2;
                end = i + sl / 2;
            }

        }
        return s.substring(begin, end + 1);
    }

    public static int nextChar(String s, int left, int right) {
        int leftNum = left;
        int rightNum = right;
        while (leftNum >= 0 && rightNum < s.length() && s.charAt(leftNum) == s.charAt(rightNum)) {
            leftNum--;
                  rightNum++;
        }
        return rightNum - leftNum - 1;

    }
}

```

## 6.将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列

```text
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

    L   C   I   R
    E T O E S I I G
    E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
```

* 示例 1:

```text
    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"
```

* 示例 2:

```text
    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"


解释:

    L     D     R
    E   O E   I I
    E C   I H   N
    T     S     G

```

```java
class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1) {
            return s;
        }
        StringBuilder result = new StringBuilder();
        int gen = numRows * 2 - 2;

        for (int i = 0; i < numRows; i++) {

            for (int j = 0; j + i < s.length(); j += gen) {
                result.append(s.charAt(j + i));
                if (i != 0 && i != numRows - 1 && j + gen - i < s.length()) {
                    result.append(s.charAt(j + gen - i));
                }
            }
        }
        return result.toString();

    }

}
```

## 7.给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转

* 示例 1:

```text
    输入: 123
    输出: 321
```

* 示例 2:

```text
    输入: -123
    输出: -321
```

* 例 3:

```text
    输入: 120
    输出: 21
```

```text
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
```

暴力翻转法：

```java
class Solution {
    public int reverse(int x) {
        String temp=x<0? String.valueOf(-x):String.valueOf(x);

        StringBuilder result = new StringBuilder();
        for (int i = temp.length() - 1; i >= 0; i--) {
            result.append(temp.charAt(i));
        }
        try {
            return x > 0 ? Integer.parseInt(result.toString()) : -Integer.parseInt(result.toString());
        } catch (java.lang.NumberFormatException e) {
            return 0;
        }
    }
}

```

弹出和推入数字 & 溢出前进行检查法：

```java
class Solution {
    public int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int lowLev = x % 10;
            x /= 10;
            if (rev > Integer.MAX_VALUE / 10 || (rev == Integer.MAX_VALUE / 10 && lowLev > 7)) return 0;
            if (rev < Integer.MIN_VALUE / 10 || (rev == Integer.MIN_VALUE / 10 && lowLev < -8)) return 0;
            rev = rev * 10 + lowLev;
        }
        return rev;
    }
}
```

## 8.请你来实现一个 atoi 函数，使其能将字符串转换成整数

```text
首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
```

* 示例 1:

```text
    输入: "42"
    输出: 42
```

* 示例 2:

```text
    输入: "   -42"
    输出: -42
    解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
```

* 示例 3:

```text
    输入: "4193 with words"
    输出: 4193
    解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
```

* 示例 4:

```text
    输入: "words and 987"
    输出: 0
    解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
         因此无法执行有效的转换。
```

* 示例 5:

```text
    输入: "-91283472332"
    输出: -2147483648
    解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
         因此返回 INT_MIN (−231) 。
```

```java
class Solution {
public int myAtoi(String str) {
        if (str == null || str.length() == 0)
            return 0;
        //1.跳过空字符
        int i = 0;
        while (i < str.length() && str.charAt(i) == ' ') {
            i++;
        }
        //此时,i指向第一个不为空的字符 或者 i越界
        if (i == str.length())
            return 0;
        //2.判断数字的符号
        int flag = 1;
        char ch = str.charAt(i);
        if (ch == '+') {
            i++;
        }
        if (ch == '-') {
            flag = -1;
            i++;
        }
        //3.找出数字部分
        int res = 0;
        for (; i < str.length(); i++) {
            ch = str.charAt(i);
            if (ch < '0' || ch > '9')
                break;
            res = res * 10 + ch - '0';
            //溢出判断
            if (flag > 0 && i + 1 < str.length() && str.charAt(i + 1) >= '0' && str.charAt(i + 1) <= '9' && res > Integer.MAX_VALUE / 10)
                return Integer.MAX_VALUE;
            if (flag > 0 && i + 1 < str.length() && str.charAt(i + 1) >= '0' && str.charAt(i + 1) <= '9' && res == Integer.MAX_VALUE / 10 && str.charAt(i + 1) - '0' > Integer.MAX_VALUE % 10)
                return Integer.MAX_VALUE;
            if (flag < 0 && i + 1 < str.length() && str.charAt(i + 1) >= '0' && str.charAt(i + 1) <= '9' && -res < Integer.MIN_VALUE / 10)
                return Integer.MIN_VALUE;
            if (flag < 0 && i + 1 < str.length() && str.charAt(i + 1) >= '0' && str.charAt(i + 1) <= '9' && -res == Integer.MIN_VALUE / 10 && -(str.charAt(i + 1) - '0') < Integer.MIN_VALUE % 10)
                return Integer.MIN_VALUE;
        }
        return res * flag;
    }
}
```

## 9.回文数

```text
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
```

* 示例 1:

```text
    输入: 121
    输出: true
```

* 示例 2:

```text
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

* 示例 3:

```text
    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
```

* 进阶:

你能不将整数转为字符串来解决这个问题吗？

```java
class Solution {
      public boolean isPalindrome(int x) {
            if (x < 0||x%10==0&&x!=0) {
                return false;
            }
            int temp = 0;
            while (x > temp) {
                temp = temp * 10+x%10;
                x/=10;

            }
            return x==temp||x==temp/10;
        }
}
```

## 10.给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配

```text
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
```

* 说明:

```text
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
```

* 示例 1:

```text
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```

* 示例 2:

```text
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```

* 示例 3:

```text
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
```

* 示例 4:

```text
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
```

* 示例 5:

```text
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```

* 题解1：（官方）：

```java
class Solution {
      public boolean isMatch(String s, String p) {
        if (p.isEmpty()) {
            return s.isEmpty();
        }

        boolean first_match = (!s.isEmpty()) && (p.charAt(0) == s.charAt(0) || p.charAt(0) == '.');
        if (p.length()>=2&&p.charAt(1)=='*'){
            return (isMatch(s,p.substring(2))||(first_match&&isMatch(s.substring(1),p)));

        }else {
            return first_match&& isMatch(s.substring(1),p.substring(1));
        }

    }
}

```

* 题解2：（官方,动态规划，自底向上）：

```java
class Solution {
      public boolean isMatch(String text, String pattern) {
        boolean[][] dp = new boolean[text.length() + 1][pattern.length() + 1];
        dp[text.length()][pattern.length()] = true;

        for (int i = text.length(); i >= 0; i--){
            for (int j = pattern.length() - 1; j >= 0; j--){
                boolean first_match = (i < text.length() &&
                        (pattern.charAt(j) == text.charAt(i) ||
                                pattern.charAt(j) == '.'));
                if (j + 1 < pattern.length() && pattern.charAt(j+1) == '*'){
                    dp[i][j] = dp[i][j+2] || first_match && dp[i+1][j];
                } else {
                    dp[i][j] = first_match && dp[i+1][j+1];
                }
            }
        }
        return dp[0][0];
    }

}
```

## 11.盛最多水的容器

```text
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

```

![11](https://i.loli.net/2019/11/09/MuQWI3gLVa6lpxP.png)

* 示例:

```text
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
```

解法一，暴力法：

```java
class Solution {
     public int maxArea(int[] height) {
        int res= 0;
        for (int i=0;i<height.length;i++){
            for (int j=height.length-1;j>0;j--){
                if (j>i){
                    if (Math.min(height[i],height[j])*(j-i)>res){

                        res= Math.min(height[i],height[j])*(j-i);
                    }
                }


            }
        }
        return res;
    }
}
```

解法二，双向指针法：

```java
class Solution {
   public int maxArea(int[] height) {
        int res = 0, l = 0, r = height.length - 1;
        while (l < r) {
            res = Math.max(res, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return res;
    }
}
```

## 12.整数转罗马数字

罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

```text
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

```

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

```text
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。
```

* 示例 1:

```text
输入: 3
输出: "III"
```

* 示例 2:

```text
输入: 4
输出: "IV"
```

* 示例 3:

```text
输入: 9
输出: "IX"
```

* 示例 4:

```text
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.
```

* 示例 5:

```text
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

解法1：哈希法

```java

class Solution {
  public String intToRoman(int num) {
        StringBuilder res = new StringBuilder();
        int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] RomanValues = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        for (int i = 0; i < values.length; i++) {
            int temp = num / values[i];
            if (temp == 0) {
                continue;
            }
            for (int j = temp; j > 0; j--) {
                res.append(RomanValues[i]);
            }
            num -= (temp * values[i]);
            if (num == 0) {

                break;
            }

        }
        return res.toString();
    }
}

```

### 13. 罗马数字转整数

* 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

```text
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

* I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
* X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
* C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

* 示例 1:

```text
输入: "III"
输出: 3
```

* 示例 2:

```text
输入: "IV"
输出: 4
```

* 示例 3:

```text
输入: "IX"
输出: 9
```

* 示例 4:

```text
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```

* 示例 5:

```text
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```

```java
class Solution {
  public int romanToInt(String s) {
        Integer[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] RomanValues = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        Map<String,Integer > map = new HashMap<>();
        for (int i = 0; i < values.length; i++) {
            map.put(RomanValues[i],values[i]);
        }
        int res = 0;
        for (int i = 0; i < s.length();) {
            if (i + 1 < s.length() && map.containsKey(s.substring(i, i + 2))) {
                res += map.get(s.substring(i, i + 2));
                i += 2;
            } else {
                res += map.get(s.substring(i, i + 1));
                i++;
            }
        }
        return res;
    }
}


```

### 14. 最长公共前缀

```text
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
```

* 示例 1:

```text
输入: ["flower","flow","flight"]
输出: "fl"
```

* 示例 2:

```text
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
```

说明:

所有输入只包含小写字母 a-z 。

解法一：逐个匹配

```java
class Solution {
public String longestCommonPrefix(String[] strs) {
        if (strs==null||strs.length==0){
            return "";
        }
        String res= strs[0];


        for (String s :strs){
            while (s.indexOf(res)!=0){
                res = res.substring(0,res.length()-1);
                if (res.isEmpty()){
                    return "";
                }
            }

        }
        return res;
    }
}
```
