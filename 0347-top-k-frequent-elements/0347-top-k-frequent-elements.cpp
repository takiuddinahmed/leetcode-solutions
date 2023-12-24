class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        map<int, int> vts;
        priority_queue<pair<int, int>> pq;
        vector<int> ans;
   
        for(int i=0; i<nums.size();i++)
        {
            vts[nums[i]]++;
        }

        for(auto &it : vts)
        {
            pq.push(make_pair(it.second, it.first));
        }

        while(k>0 && !pq.empty())
        {
            ans.push_back(pq.top().second);
            pq.pop();
            k--;
        }
        return ans;
    }
};