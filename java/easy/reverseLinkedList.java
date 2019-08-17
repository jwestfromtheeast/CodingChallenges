// Leetcode 206
class Solution {
    // Recursive solution with helper function
    private ListNode reverseListR(ListNode head, ListNode newHead) {
        if (head == null) {
            return newHead;
        }
        ListNode next = head.next;
        head.next = newHead;
        return reverseListR(next, head);
    }
    public ListNode reverseListR(ListNode head) {
        return reverseListR(head, null);
    }
    
    // Convert that to an iterative solution (to ensure we never exceed the call stack)
    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode newHead = null;
        while (head != null) {
            ListNode next = head.next;
            head.next = newHead;
            newHead = head;
            head = next;
        }
        return newHead;
    }
}