# 力扣
### 锻炼做做题

[直达链接](https://leetcode-cn.com/problemset/all/)


1.给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]

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


2.给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807

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
3.给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

    输入: "abcabcbb"
    输出: 3 
    解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:

    输入: "bbbbb"
    输出: 1
    解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:

    输入: "pwwkew"
    输出: 3
    解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
         请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


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


4.给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

    nums1 = [1, 3]
    nums2 = [2]
    则中位数是 2.0

示例 2:

    nums1 = [1, 2]
    nums2 = [3, 4]
    则中位数是 (2 + 3)/2 = 2.5

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

       
       
5.给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。
示例 2：

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
6.将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

    L   C   I   R
    E T O E S I I G
    E   D   H   N

之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

示例 1:

    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"

示例 2:

    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"

解释:
    
    L     D     R
    E   O E   I I
    E C   I H   N
    T     S     G


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


7.给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

    输入: 123
    输出: 321

 示例 2:

    输入: -123
    输出: -321

示例 3:

    输入: 120
    输出: 21

注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

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



8.请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：

假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

 示例 1:

    输入: "42"
    输出: 42

示例 2:

    输入: "   -42"
    输出: -42
    解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例 3:

    输入: "4193 with words"
    输出: 4193
    解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例 4:

    输入: "words and 987"
    输出: 0
    解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
         因此无法执行有效的转换。
     
示例 5:

    输入: "-91283472332"
    输出: -2147483648
    解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
         因此返回 INT_MIN (−231) 。

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


9.回文数

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

    输入: 121
    输出: true
 示例 2:
 
    输入: -121
    输出: false
    解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

    输入: 10
    输出: false
    解释: 从右向左读, 为 01 。因此它不是一个回文数。
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

