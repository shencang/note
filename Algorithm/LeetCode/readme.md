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

