/**
 * @param {number[]} height
 * @return {number}
 */
const maxArea = function (height) {
  let maxArea = 0;

  let left = 0;
  let right = height.length - 1;
  while (left < right) {
    let width = Math.min(height[left], height[right]);
    let length = right - left;
    let area = width * length;

    maxArea = Math.max(area, maxArea);

    if (height[left] < height[right]) {
      left++;
    } else if (height[right] <= height[left]) {
      right--;
    }
  }

  // Brute Force
  // for (let i = 0; i < height.length; i++) {
  //   for (let j = 1; j < height.length; j++) {
  //     let width = Math.min(height[i], height[j]);
  //     let length = j - i;
  //     let area = width * length;

  //     maxArea = Math.max(area, maxArea);
  //   }
  // }

  return maxArea;
};

// Jest Tests
describe('Test Functions', () => {
  // let object;
  // beforeEach(() => {
  //   object = new MyClass();
  // });

  it('Test Case 1', () => {
    let n = [1, 8, 6, 2, 5, 4, 8, 3, 7];
    expect(maxArea(n)).toBe(49);
  });
  it('Test Case 2', () => {
    let n = [1, 2];
    expect(maxArea(n)).toBe(1);
  });
});
