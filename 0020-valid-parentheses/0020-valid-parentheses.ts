function isValid(s: string): boolean {
    const closeMap = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    const stack = [];
    
    for (let i =0;i<s.length;i++){
        const p = s[i];
        if(closeMap[p] !== undefined){
            if(stack[stack.length-1] === closeMap[p]){
                stack.pop()
            }
            else return false;
        }
        else {
            stack.push(p);
        }
    }
    return stack.length === 0
};