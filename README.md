# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

### My Reflection

For this assignment, I learned how linear search and binary search work in Python and how their performance changes
depending on the size of the dataset. I also learned more about time complexity and why choosing the right algorithm
matters.

The biggest challenge for me was understanding binary search. Linear search was pretty straightforward because it
checks one item at a time. With binary search, I had to keep track of the low, high, and middle indexes. I worked
through the logic step by step to understand how the search area gets smaller after each comparison. Testing empty
lists and missing values also helped me understand why edge cases are important.

I think linear search is better for smaller datasets or when the data is not sorted. Binary search is more efficient
for larger sorted datasets because it eliminates half of the remaining values each time. However, sorting data
beforehand requires extra work.

A real-world example for me is inventory management. When dealing with thousands of inventory items, having organized
data makes it much easier to find specific products quickly.
