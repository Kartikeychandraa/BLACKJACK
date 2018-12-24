# BLACKJACK
My Blackjack is the numeric version of original one , it is also connected to database for records.
# INTRODUCTION
Blackjack, also known as twenty-one, is a comparing card game between usually several players and a dealer, where each player in turn competes against the dealer, but players do not play against each other. It is played with one or more decks of 52 cards, and is the most widely played casino banking game in the world.The objective of the game is to beat the dealer .
# RULES TO PLAY
	Reach a final score higher than the dealer without exceeding 21
	Pass stop taking cards from dealer
	HIT take another card  from dealer
# HOW TO PLAY
# SCREEN 1:-
 
You need to open the START.py file to start this game.this page give`s a splash screen that give the information about who created this game .you have to hover cursor on the creator image to start the game
# SCREEN 2:-
 


Welcome to the main page of the game Enter two players detail like their name and age.
Details would be  typed  on the right textboxes 
The RULES button at the bottom left corner will tell you the game rules or how to play the game 
The SUBMIT button at the bottom right corner will save your details in database and next page will appear
The  FOR ADMIN button at the bottom center will show all players ever played this game
But this is only for administrator 
SUB SCREEN (HELP):-
 
This screen provides you rules of the game
SUB SCREEN (ADMIN):-
 
This screen tells you all players ever played this game

# SCREEN 3:-
 
This is the main game press  HIT to take card from dealer ,press PASS to STAY on the total cards added
If both numbers  are same and pressed pass by both player then game is draw
Press exit to play again

 



If player 1has greater score than player 2 and both press pass then player 1will win the blackjack
Press exit to play again

 
If player 2has greater score than player 1 and both press pass then player2 will win the blackjack
Press exit to play again


 
# DATABASE:-
Databaa.db is the file that contain my database 
Table name is game
I have player _1 ,age_1,player_2,age_2 are the column in the table game
Where all my datatypes are varchar2() with the limit of 20 in name columns and 3 as a limit on a age columns.
 query used :-
cur.execute("create table if not exists game(player_1 varchar(20),age_1 varchar(3),player_2 varchar(20),age_2 varchar(3))")
To insert data  I have used 
cur.execute("insert into game values(?,?,?,?)",(a,a1,b,b1))
To display data I have used 
cur.execute("select * from game")
adm=cur.fetchall()

