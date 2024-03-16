Here's a simple warm-up exercise in JavaScript. Let's create a function that takes in an array of numbers and returns the sum of all the numbers in the array.

javascript
Copy code
function sumArray(numbers) {
  let sum = 0;
  for (let i = 0; i < numbers.length; i++) {
    sum += numbers[i];
  }
  return sum;
}

// Example usage:
const numbers = [1, 2, 3, 4, 5];
console.log(sumArray(numbers)); // Output: 15
In this code:

We define a function called sumArray which takes an array of numbers as input.
We initialize a variable sum to keep track of the sum and set it to 0.
We iterate through each element of the array using a for loop, adding each element to the sum variable.
Finally, we return the sum after all elements have been added up.
