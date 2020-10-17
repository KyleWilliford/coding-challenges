package leetcode.linkedlist;

import lombok.extern.slf4j.Slf4j;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Slf4j
class MergeTwoLinkedLists {

    public static void main(String[] args) {
        MergeTwoLinkedLists mergeTwoLinkedLists = new MergeTwoLinkedLists();
        ListNode l1 = mergeTwoLinkedLists.buildLinkedList(Arrays.asList(1, 2, 4));
        logger.info("{}", l1);
        ListNode l2 = mergeTwoLinkedLists.buildLinkedList(Arrays.asList(1, 3, 4));
        logger.info("{}", l2);
        ListNode merged = mergeTwoLinkedLists.mergeTwoLists(l1, l2);
        logger.info("{}", merged);
        List<Integer> nums = new ArrayList<>();
        while (merged != null) {
            nums.add(merged.val);
            merged = merged.next;
        }
        logger.info("{}", nums);
    }

    private ListNode buildLinkedList(List<Integer> nums) {
        ListNode prev = null;
        ListNode head = new ListNode();
        ListNode cur = head;
        for (Integer n : nums) {
            if (cur == null) {
                cur = new ListNode();
            }
            cur.val = n;
            if (prev != null) {
                prev.next = cur;
            }
            prev = cur;
            cur = null;
        }
        return head;
    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        } else if (l2 == null) {
            return l1;
        }
        ListNode head = l2;
        if (l1.val < l2.val) {
            l2 = l1;
            l1 = head;
            head = l2;
        }
        while (l1 != null) {
            if (l2.next == null) {
                l2.next = l1;
                break;
            } else if (l2.val <= l1.val && l1.val <= l2.next.val) {
                ListNode temp = l1.next;
                l1.next = l2.next;
                l2.next = l1;
                l1 = temp;
//                logger.info("l1 {}", l1);
//                logger.info("l2 {}", l2);
//                logger.info("head {}", head);
            } else {
                l2 = l2.next;
            }
        }
        return head;
    }
}