/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* v = new ListNode(0);
        ListNode* n = v;
        int carry = 0;

        while(l1 != nullptr || l2 != nullptr || carry != 0)
        {
            int n1 = (l1 != nullptr) ? l1->val : 0;
            int n2 = (l2 != nullptr) ? l2->val : 0;
            int n3 = n1 + n2 + carry;
            
            carry = n3 / 10;
            n->next = new ListNode(n3 % 10);
            n = n->next;

            if(l1 != nullptr) l1 = l1->next;
            if(l2 != nullptr) l2 = l2->next;
        }
        return v->next;
    }
};