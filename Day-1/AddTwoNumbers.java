/*
 Add Two Numbers
Add digits from both linked lists along with carry
and store the result in a new linked list.
*/
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode();
        ListNode  curr = dummy;

        int carry = 0;
        while(l1!= null|| l2 != null|| carry!=0){
            int x = (l1!=null) ?  l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            int sum = x+y+carry;
            carry = sum/10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            if(l1!= null) l1 = l1.next;
            if(l2!= null) l2 = l2.next ;
        }
        return dummy.next;
        
    }
}
/*
Time Complexity: O(max(m,n))
Space Complexity: O(max(m,n))
 */
