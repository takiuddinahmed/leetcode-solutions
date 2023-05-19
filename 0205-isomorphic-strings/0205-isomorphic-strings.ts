function isIsomorphic(s: string, t: string): boolean {

    const map = {}
    const reverseMap = {}
    for (let i=0;i<s.length;i++){
        if(map[s[i]]){
            if (map[s[i]] !== t[i]) return false
        }
        if(reverseMap[t[i]]){
            if (reverseMap[t[i]] !== s[i]) return false
        }
        // console.log({map, reverseMap})
        map[s[i]] = t[i]
        reverseMap[t[i]] = s[i]
    }
    return true
};