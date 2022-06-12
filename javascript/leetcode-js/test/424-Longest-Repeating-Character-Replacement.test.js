/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var characterReplacement = function (s, k) {
  let map = new Map();
  let maxLength = 0;
  let left = 0;

  for (right = 0; right < s.length; right++) {
    map.has(s[right])
      ? map.set(s[right], map.get(s[right]) + 1)
      : map.set(s[right], 1);

    while (right - left + 1 - Math.max(...map.values()) > k) {
      map.set(s[left], map.get(s[left]) - 1);
      left++;
    }
    maxLength = Math.max(maxLength, right - left + 1);
  }
  return maxLength;
};
// Jest Tests
describe('Test Function', () => {
  // let object;
  // beforeEach(() => {
  //   object = new MyClass();
  // });

  it('Test Case 1', () => {
    expect(characterReplacement('ABAB', 2)).toBe(4);
  });
  it('Test Case 2', () => {
    expect(characterReplacement('AABABBA', 1)).toBe(4);
  });
  it('Test Case 3', () => {
    expect(characterReplacement('ABABABA', 2)).toBe(5);
  });
  it('Test Case 4', () => {
    expect(characterReplacement('ABBB', 2)).toBe(4);
  });
  it('Test Case 5', () => {
    expect(characterReplacement('ABBA', 2)).toBe(4);
  });
  it('Test Case 6', () => {
    expect(characterReplacement('XAPCCCARF', 4)).toBe(7);
  });
});
