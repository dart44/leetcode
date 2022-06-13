/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = (nums, target) => {
  const map = new Map();
  for (let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];
    if (map.has(diff)) {
      return [map.get(diff), i];
    }
    map.set(nums[i], i);
  }
  return [];
};

// var twoSum = (nums, target) => {
//   for (i = 0; i < nums.length; i++) {
//     for (j = i + 1; j < nums.length; j++) {
//       if (nums[i] + nums[j] === target) {
//         return [i, j];
//       }
//     }
//   }
//   return [-1, 1];
// };

// Jest Tests
// describe('Test Function', () => {
//   // let object;
//   // beforeEach(() => {
//   //   object = new MyClass();
//   // });

//   it('Test Case 1', () => {
//     expect(twoSum([2, 7, 11, 15], 9)).toStrictEqual([0, 1]);
//   });
//   it('Test Case 2', () => {
//     expect(twoSum([3, 2, 4], 6)).toStrictEqual([1, 2]);
//   });
//   it('Test Case 3', () => {
//     expect(twoSum([3, 3], 6)).toStrictEqual([0, 1]);
//   });
// });

console.log(twoSum([2, 7, 11, 15], 9));
