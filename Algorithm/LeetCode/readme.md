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