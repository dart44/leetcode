/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let length = 1;
  let left = 0;
  let set = new Set();

  if (s === '') {
    return 0;
  }

  for (right = 1; right < s.length; right++) {
    if (s[left] === s[right] || set.has(s[right])) {
      left = left + 1;
      right = left;
      set.clear();
      continue;
    }

    set.add(s[left]);
    set.add(s[right]);
    length = Math.max(length, set.size);
  }

  return length;
};

// Jest Tests
describe('Test Function', () => {
  // let object;
  // beforeEach(() => {
  //   object = new MyClass();
  // });

  it('Test Case 1', () => {
    let n = 'abcabcbb';
    expect(lengthOfLongestSubstring(n)).toBe(3);
  });
  it('Test Case 2', () => {
    let n = 'bbbbb';
    expect(lengthOfLongestSubstring(n)).toBe(1);
  });
  it('Test Case 3', () => {
    let n = 'pwwkew';
    expect(lengthOfLongestSubstring(n)).toBe(3);
  });
  it('Test Case 4', () => {
    let n = '';
    expect(lengthOfLongestSubstring(n)).toBe(0);
  });
  it('Test Case 5', () => {
    let n = 'au';
    expect(lengthOfLongestSubstring(n)).toBe(2);
  });
  it('Test Case 6', () => {
    let n = 'dvdf';
    expect(lengthOfLongestSubstring(n)).toBe(3);
  });
});
