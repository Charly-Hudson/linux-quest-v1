## Quest 2: Part 2 Moving things 

Now we need to move some things around, there are several zipped files that need unzipping too, if you remember from quest 1

You should move the files from where they are to where they need to be, each file has a specific folder(directory) 

(Just incase there are some permission issues use 'chmod 777 < file/folder name >' to un-restrict it )

|=====================|
|         Hint        |
|  printenv hintQ2P2  |
|                     |
|       Answer        |
| printenv answerQ2P2 |
|                     |
|=====================|

In the end it should look like this 

|================================================================|
|      Tree                  |          ls                       |
|  —quests                   |   /quests                         |
|    ⊢—quest1                |   /quests/quest1                  |
|    |   ⊢—file1             |   /quests/quest1/file1            |
|    |   |   ⊢—file1.txt     |   /quests/quest1/file1/file1.txt  |
|    |   ⊢—file2             |   /quests/quest1/file2            |
|    |       ⊢—file2.py      |   /quests/quest1/file2/file2.py   |
|    ⊢—quest2                |   /quests/quest2                  |
|    |   ⊢—game              |   /quests/quest2/game             |
|    |       ⊢—day.json      |   /quests/quest2/game/day.json    |
|    |       ⊢—score.json    |   /quests/quest2/game/score.json  |
|    ⊢—quest3                |   /quests/quest3                  |
|        ⊢—quest3            |   /quests/quest3/                 |
|                            |                                   |
|================================================================|

You should run 'Cat linux-quest-2p3.md'