# Sorting

## Heap Sort
## Merge Sort
General-purpose, and comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.

Stable.
**Data structure**	Array
**Worst-case performance**	O(n log n)
**Best-case performance**	Omega (n log n) **typical** Omega (n) natural variant
**Average performance**	{\displaystyle \Theta (n\log n)}\Theta (n\log n)
**Worst-case space complexity**	O(n) total withO(n) auxiliary, O(1)}O(1) auxiliary with linked lists[1]

## Quick Sort
Quick sort is the fastest-known, comparison-based sorting algorithm for lists in the average case.

Unstable.

### Steps:
1. Start with a list of n elements;
2. Choose a pivot element from the list to be sorted;
3. Partition the list into 2 unsorted sublists, such that all elements in one sublist are less than the pivot and all the elements in the other sublist are greater than the pivot;
4. Elements that are equal to the pivot can go in either sublist;
5. Sort each sublist recursively to yield two sorted sublists;
6. Concatenate the two sorted sublists and the pivot to yield one sorted list.

The average case complexity of quick sort is in O(nlog(n))
O(nlog(n)), because for each log(n) recursive call, the given list is iterated over.

### Worst-case O(n) situations
1. The array is already sorted in the same order
2. The array is already sorted in reverse order
3. All the elements in the array are the same

### MergeSort vs QuickSort
Merge: simple dividing, all work on merging. Stable.

Quick: all work on dividing, simple merging. Unstable.


## Counting Sort
## Radix Sort
## Insertion Sort

