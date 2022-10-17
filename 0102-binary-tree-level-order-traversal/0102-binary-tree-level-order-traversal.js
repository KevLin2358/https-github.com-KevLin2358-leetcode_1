/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */

var levelOrder = function(root) {
    
    if(!root) return [];
    
    let result = [];
    let deque = [root];
    
    while(deque.length > 0){
        const length = deque.length;
        let level = [];
        
        for(let i = 0; i < length; i++){
            const current = deque.shift();
            level.push(current.val);
            
            if(current.left) deque.push(current.left);
            if(current.right) deque.push(current.right);
        }
        result.push(level)
    }
    return result;
};