## Google- Auto Complete
In order to improve the user experience of the Google search engine, the development team decided to allow completion
Of sentences from articles, documentation and information files on various technological topics.

>Initialtion

    The system loads all the data from\2021-archive\RFC to the data strucure (every line is a query):
    * Dict- contains {id: query}
    * Trie- contains suffix of queries, in the end of the query's suffix there is a key of the completed query in the dict


> CLI
    
    User typed a string and the system returned the five best completions

----------- 
----------- 
```
Completion Is Done By:
A complete string is a string whose user string is a sub-string.

If there is an one correction in user's string- the completion string is a text whose user's correction string is sub-srtring.

Defined correction: addition letter, deletion letter or replacement letter.

There is a score for each completion string
The 5 best completions returned are sentences with highest score.
```
 




