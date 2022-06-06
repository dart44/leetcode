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
 * @param {TreeNode} subRoot
 * @return {boolean}
 */
    let sameTree = (root, subRoot) => {
        if (!root && !subRoot) {
            return true;
        }
        if (!root || !subRoot || root.val != subRoot.val) {
            return false;
        }
        return sameTree(root.left, subRoot.left) && sameTree(root.right, subRoot.right)
    }

    let isSubtree = (root, subRoot) => {
        if (sameTree(root, subRoot)) {
            return true;
        }
        if (root && root.left && isSubtree(root.left, subRoot)) {
            return true;
        }
        if (root && root.right && isSubtree(root.right, subRoot)) {
            return true;
        }
        return false;
    };