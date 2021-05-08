# boggle

The game of Boggle is played on a grid of letters. Players compete to find as many words as possible within a given time limit, based on words from a dictionary. 

Rules:

1. Words must be in a specified dictionary.

2. Letters are in a rectangular grid, N x M.

3. Words can be formed by going to adjacent lerrers horizontally, vertically, or diagonally.

4. The letter at a grid square can be used at most once in a given word.

5. A letter in a grid square can be used in multiple, different words.

For the purposes of this exercise, assume there's a dictionary "object", with a single method in whatever language you choose

bool IsWord(string) 

Write a function that takes an NxM grid of letters, and a dictionary object, and returns all of the words in that grid

Given the board

H N S E 

A R G U

B R U S

F E T I

and the usual english dictionary in /usr/share/dict/words on a mac, and either there or in /usr/dict/words on a linux machine

Examples:

1. sugar is not a valid word, even though they are all connected, you can only get sugra or usgra with this board

2. true is a word (even though the line of the letters goes criss-cross)

3. sis is not a valid word, since it would have to use the same 's' twice

4. brush is not a valid word, since the s and h are not adjacent



Q&A:

Do I use the given 4x4 board or generate new one?
the priblem should work for an NxM grid, I just rivided a 4x4 grid as an example for clarification

Do I have to iterate over all the words in dict? and invoke isWord(str)  ?
you need to find all the words, that are in the dict, that can be found in the grid

Do I need to output time taken to find all the available words?
don't worry about outputting the time, if we have working code we can use the unix time function. in reality, we'd want to assign som computational load factor to each operation, and see how it goes. Do think about how you might optimize, but don't spend time optimizing

Are unit tests expected?
think about how to test the code... if you have time to write some unit tests, great, if not, we can discuss how you'd test it

Do you have any time/space complexity restrictions?
no time/space complexity restrictions, but do think about the complexity. I'll ask about it :slightly_smiling_face:

Basic Algorithm isWord(string):

It is graph traversal problem. we will use Breadth First Search(BFS)

Time Complexity: O(V+E)
Space Complexity: O(V)


1. Iterate over grid until 1st char of given string is found
2. put [row, col] in queue
3. grid[row, col] = '_' to avoid cycles
4. while queue not empty
5. search in all 8 directions for next char of given string
6. if found, increase word_index count
7. grid[row, col] = '_' to avoid cycles
8. repeat the process until all chars of given string is found or we go out space in grid
