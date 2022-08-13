# infosoftassignment

Problem 3 Debug Calender Design

Binary Search
The basic idea is that we need to do a binary search to find the location for the start and end when adding an event.

For example, the current calendar is [[10, 20], [25, 35], [50, 60], [61, 63]]
and we want to add an event with time [21, 24]

We need to search the location for start time 21 between all the end times in the current calendar [20, 35, 60, 63].
The suitable location should be the left-hand side of the smallest value that is larger than the input start time.
Thus, it is index 1 in this case.

Then, we need to compare

-the input start time with the end time of previous node
-the input end time with the start time of next node



The error was found in the insert method of the node class wherein the comparison symbols were not correct.
