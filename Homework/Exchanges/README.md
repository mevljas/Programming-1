# Changes
## Mandatory task
Write the function replace(s, i, j), which replaces the i-th and j-th element in the given s. The function changes the specified list and does not return anything.

Also write the function replaced(s, i, j), which returns a list containing the same elements as s, except that the i-th and j-th elements are replaced. The function does not change the specified list.

## Additional task
Write an edit(s) function that receives a list of s and returns a list of changes (i.e., a list of index pairs) needed to edit the list. For a list [5, 2, 8, 1] it can return, say, a sequence, [(0, 1), (2, 3), (1, 2), (0, 1)]. The function does not need to return the shortest possible sequence. The possible solutions are (literally) endless.

Tip: It will be easiest if you program a simple algorithm for editing lists and save changes while editing. Even bubble editing will suffice.

Of course, you are also challenged to put together the shortest possible sequence (although the task does not require it). Tip: will have len (s) - 1 changes.
