## Quest 2: Part 3 Editing Files, Renaming them 

Right now, we need to look at the files in quest 1, specifically file1.txt

When you look at this file you will see its actually PYTHON file not a .txt file

But how do we change it? 

|=====================|
|         Hint        |
|  printenv hintQ2P2  |
|                     |
|       Answer        |
| printenv answerQ2P2 |
|                     |
|=====================|

In the end your files should look like this:

|================================================================|
|      Tree                  |          ls                       |
|  —quests                   |   /quests                         |
|    ⊢—quest1                |   /quests/quest1                  |
|        ⊢—file1             |   /quests/quest1/file1            |
|            ⊢—file1.txt     |   /quests/quest1/file1/file1.txt  |
|        ⊢—file2             |   /quests/quest1/file2            |
|            ⊢—file2.py      |   /quests/quest1/file2/file2.py   |
|    ⊢—quest2                |   /quests/quest2                  |
|        ⊢—game              |   /quests/quest2/game             |
|            ⊢—day.json      |   /quests/quest2/game/day.json    |
|            ⊢—score.json    |   /quests/quest2/game/score.json  |
|    ⊢—quest3                |   /quests/quest3                  |
|        ⊢—quest3            |   /quests/quest3/                 |
|                            |                                   |
|================================================================|

Now lets go and run that file, to run python files its alittle different then using 'sudo' 

To run python files we need to use 'python3' because thats what currently installed on this EC2

the end result of running this file should be 

|===================|
|                   |
|    Hello world    |
|                   |
|===================|

You should should now be able to move onto 'cat linux-quest-2p4.md'