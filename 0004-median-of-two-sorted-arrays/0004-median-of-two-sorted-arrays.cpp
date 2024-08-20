class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int s1 = nums1.size();
        int s2 = nums2.size();

        int p1 = 0, p2 = 0;
        int m1 = -1, m2 = -1;
        
        for(int i = 0; i <= (s1 + s2) / 2; i++)
        {
            m2 = m1;
            if(p1 != s1 && p2 != s2)
            {
                m1 = (nums1[p1] > nums2[p2]) ? nums2[p2++] : nums1[p1++];
            }            
            else if (p1 < s1)
            {
                m1 = nums1[p1++];
            }
            else 
            {
                m1 = nums2[p2++];
            }
        }

        if((s1 + s2) % 2 != 0) return m1;
        else return (m1 + m2) / 2.0;

    }
};