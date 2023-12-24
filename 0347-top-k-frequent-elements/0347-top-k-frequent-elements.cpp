class Solution {
public:
    int partition(vector<pair<int, int>>& vec, int l, int r) {
        int pivot = vec[r].first;  // Pivot value should be the frequency
        int j = l - 1;

        for (int i = l; i < r; i++) {
            if (vec[i].first > pivot) { 
                j++;
                swap(vec[i], vec[j]);
            }
        }

        swap(vec[j + 1], vec[r]);
        return j + 1;
    }

    void quickSelect(vector<pair<int, int>>& vec, int l, int r, int k) {
        if (l < r) {
            int part = partition(vec, l, r);
            if (part == k) {
                return;
            } else if (part < k) {
                quickSelect(vec, part + 1, r, k);
            } else {
                quickSelect(vec, l, part - 1, k);
            }
        }
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        int n = nums.size();
        unordered_map<int, int> mp;

        for (int i = 0; i < n; i++) {
            mp[nums[i]]++;
        }

        vector<pair<int, int>> vec;
        for (auto x : mp) {
            vec.push_back({x.second, x.first});
        }

        quickSelect(vec, 0, vec.size() - 1, k - 1);

        for (int i = 0; i < k; i++) {
            res.push_back(vec[i].second);
        }

        return res;
    }
};