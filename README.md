# Learning python
In this repository I'm going to put some of my small projects while I'm learning python in Yasan academy
## Table of contents
|Project name|Short description|
|:---|:---|
|[Hoop](#Hoop)|A simple game|
|[Search by first characters](#Search-by-first-characters)|A search machine for names that works with first chars of the last and the first names
|[To-Do](#to-do)|A to-do list|
<div style="text-align: justify">
<a name="Hoop"/>

## Hoop
In this game which is an old game in my country you have to say "Hoop" after every X.
Basically you're saying hoop whenever the number can be divided by X.
By the way you have to specify this X at first.

### Example:
If we want to play it with X = 3
It's going to be like this: 1, 2, *, 4, 5, *, etc.

### Notes:
You only have 5 seconds to answer

If you either told * in the wrong spot or you told it after 5 seconds you'll lose

The academy says that the idea to create this game in python was for somebody else.

<a name="Search-by-first-characters"/>

## Search by first characters
In this project you have to specify two characters, the first one is going to be the first character of first name and the second one is going be the first character of the last name. Then the program is going to find a name based on the data you gave to it.

### Example:
Az an example you have entered "a" and "b", the program is going to give you "Ali Bahonar"

### Notes:
You can change the list (names) for different results but it was just a pre-made one for testing.

<a name="To-Do"/>

## To-Do
As the names suggests its a to-do list which you can interact with via commands.
### Table of commands:
|Command name|Short description|
|:---|:---|
|[Help](#Help)|Opens this repository for help|
|[Add](#Add)|Adds things to the to-do list|
|[List](#List)|Gives you the to-do list|
|[Save](#Save)|Saves the list|

### Commands:
<a name="Help"/>

#### Help:
It opens this page that you're looking at so you can read the readme for help
<a name="Add"/>

#### Add:
It adds a thing to the to-do list.
But what if you wanted to add not just one but 3 different items, then you can use a feature to do it!
For doing it just add m= and then the number of things that you want to add then you can add them without needing to type the command every time. just like the code below.
##### Example:
```
Command: add m=3
Add task: a
Add task: b
Add task: c
```

This is also another example for the simpler form
##### Example:
```
Command: add
Add task: a
```
<a name="List"/>

#### List:
It gives you a list of all of the task (ToDos' list)

<a name="Save"/>

#### Save:
It saves the ToDos' list into a file named database.py and after the program opened another time it will read the saved list
</div>