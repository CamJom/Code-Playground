// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

const array = [1, 3, 7, 10]
const input = 17

const calc = (a, k) => {
  const ans = []

  for (let i = 0; i < a.length; i++){
    for (let j = i + 1; j < a.length; j++){
      if (a[i] + a[j] === k) {
        ans.push(i)
        ans.push(j)
      }
    }
  }
  return ans
}

console.log(calc(array,input))

