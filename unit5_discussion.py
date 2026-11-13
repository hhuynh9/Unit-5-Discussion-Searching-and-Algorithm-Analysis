
"""
====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Check each item in order. In the worst case all n items are checked: O(n).
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            # Discard the left half (including mid).
            low = mid + 1
        else:
            # Discard the right half (including mid).
            high = mid - 1

    # Repeated halving takes O(log n) comparisons in the worst case.
    return -1


def linear_search_count(lst, target):
    """Count comparisons so the difference is visible without timing noise."""
    checks = 0

    for i in range(len(lst)):
        checks += 1
        if lst[i] == target:
            return i, checks

    return -1, checks


def binary_search_count(lst, target):
    """Count the middle-element comparisons in binary search."""
    low, high = 0, len(lst) - 1
    checks = 0

    while low <= high:
        mid = (low + high) // 2
        checks += 1

        if lst[mid] == target:
            return mid, checks

        if lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, checks


def compare_searches(scores, target):
    """Print the results and number of elements checked by each algorithm."""
    lin_index, lin_checks = linear_search_count(scores, target)
    bin_index, bin_checks = binary_search_count(scores, target)

    assert lin_index == linear_search(scores, target)
    assert bin_index == binary_search(scores, target)
    assert lin_index == bin_index  # These examples use unique, sorted values.

    print(f"Searching for {target} in {len(scores):,} scores")
    print(f"  Linear search: index {lin_index}, {lin_checks:,} comparisons")
    print(f"  Binary search: index {bin_index}, {bin_checks:,} comparisons")
    print("  Result: found" if lin_index != -1 else "  Result: not found (-1)")


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ==============================
    # TODO (Student): SMALL DATASET
    # ==============================
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_scores = [55, 67, 72, 81, 90, 95]
    print("Scores:", small_scores)

    compare_searches(small_scores, 81)
    compare_searches(small_scores, 100)

    # Both methods return the same index for 81 and -1 for missing 100.

    # ==============================
    # TODO (Student): LARGE DATASET
    # ==============================
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_scores = list(range(1, 100001))

    compare_searches(large_scores, 99999)
    compare_searches(large_scores, 100001)

    # Linear search can inspect all 100,000 items (O(n)).
    # Binary search keeps halving the list, using about 17 checks (O(log n)).
    # For large sorted data, the fewer comparisons make binary search efficient.

    # ==============================
    # TODO (Student): EDGE CASES
    # ==============================
    # Demonstrate at least two edge cases.
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # With no items, neither search enters its loop and both return -1.
    compare_searches([], 81)

    # A one-item list can find its only value at index 0.
    compare_searches([81], 81)

    # A one-item list returns -1 when the target is different.
    compare_searches([81], 90)

    # These test the first and last valid positions in a sorted list.
    compare_searches(small_scores, 55)
    compare_searches(small_scores, 95)

    print("\n=== REAL-WORLD APPLICATION ===")
    print("A storeroom could search for an item ID in an inventory list.")
    print("Linear search works on unsorted lists; binary search requires sorted IDs.")
    print("Keeping IDs sorted takes preparation but speeds up repeated searches.")


    # Test searching for an item in the storeroom inventory.
    inventory_ids = [101, 205, 310, 415, 520, 625, 730]

    print("\nSearching for inventory item 520:")
    compare_searches(inventory_ids, 520)

    print("\nSearching for missing inventory item 999:")
    compare_searches(inventory_ids, 999)


if __name__ == "__main__":
    main()
