# Learning python
In this repository I'm going to put some of my small projects while I'm learning python in Yasan academy
## Table of contents
|Project name|Short description|
|:---|:---|
|[Hoop](#Hoop)|A simple game|
|[Search by first characters](#Search-by-first-characters)|A search machine for names that works with first chars of the last and the first names|
|[To-Do](#to-do)|A to-do list|
|[Functional calculator](#functional-calculator)|A really simple calculator full of functions|

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
|[Status](#Status)|Lets you mark item as done or not done|
|[Remove](#Remove)|It removes items|
|[Save](#Save)|Saves the list|
|[Clear](#Clear)|Clears the terminal|
|[Database](#database)|Command related to database management|

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

<a name="Status"/>

#### Status:
You can mark things done or not done, by default items are created as not done but you can change that.
With the command "status check" or "status done" you can mark them as done and with the command "status" you can mark them as not done.
but after these commands you have to tell the program which items you're going to mark, you have these options below.

##### (their index):
You can put their index in it and it will select just that item for you.
###### tip:
The list command also gives you items' index.
##### all:
It will simply select all of them.
##### from and to:
If the from command is used with the "to" command the index after the "from" command will specify the selection starting point and the index after the "to" command will specify the selection ending point.
##### from:
If "from" is used alone the program is going to select from the index after the "from" command till the end.
##### to:
If "to" is used alone the program is going to select from the beginning till the index after the "to" command.

<a name="Remove"/>

#### Remove:
It removes items you want.
For selecting the items you can enter these command after the remove command.

##### (their index):
You can put their index in it and it will select just that item for you.
###### tip:
The list command also gives you items' index.
##### all:
It will simply select all of them.
##### from and to:
If the from command is used with the "to" command the index after the "from" command will specify the selection starting point and the index after the "to" command will specify the selection ending point.
##### from:
If "from" is used alone the program is going to select from the index after the "from" command till the end.
##### to:
If "to" is used alone the program is going to select from the beginning till the index after the "to" command.

<a name="Save"/>

#### Save:
It saves the ToDos' list into a file named database.py or something else if you have changed your database and after the program opened another time it will read the saved list
##### Note:
The program will open database.py as its database at first but you can change it later.

<a name="Clear"/>

#### Clear:
It clears the commands you have entered

<a name="Exit"/>

#### Exit:
This command closes the program

<a name="Database">

#### Database:
This command has the following commands you can access them by typing each one after the database command
By the way you can enter db instead of database they are the same like "db switch databasename" instead of "database switch databasename"
##### Restore:
It changes the current unsaved to-do list to the last saved version of the database
##### Switch:
With this command you can switch between databases and have multiple to-dos
You just have to type the name of a pre-made database after the switch command just like this example below:
```
Command: database switch databasename
```
###### Note:
You can make databases with the "database new" command
##### New:
With this command you can make more databases than the default and have multiple to-do lists
###### Note:
After you make a database the program will switch from the current database to the one newly created
You can also switch between databases with the "database switch" command
##### Saveas:
It will create a database with your to-do list in the current directory
###### Note:
It won't switch to the newly created database automatically

<a name="Functional calculator">

## Functional calculator
It's a really simple calculator that as the name suggests it's full of functions and hopefully it also functions too :)

You just have to enter the index of the operation you want and then you just have to enter the first and the second number and it will give you the answer

### Note:
For getting the list of operations you can enter "list" instead of the index of an operation.

You can also replace "list" with "exit" for exiting from the program and "clear" or "cls" for cleaning the terminal.
</div>
