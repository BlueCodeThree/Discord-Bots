# Discord Bots
This is a personal, fun project to create some discord bots. 

## Javascript Bot

Jan 2019

*DiscordBotJS.js*

To run, use terminal and run `node DiscordBotJS.js`

This Bot responds to programed commands, using a prefix. 
Some of the responses are pulled from a list of responses. The list
is shuffled so that it doesn't just use the first response in the list
but a random response. It then takes that response that has been said, 
and puts it somewhere in the second half of the list, so that the bot 
does not say the same response twice in a row. 

## Python Bot

Jan 2019 

*DiscordBotPY.py*

(Not yet in the repository, but making notes here...)

I built this bot after the Javascript bot, so it has the features of that bot.

This bot also has the ability to learn new commands from the user from within Discord. 
The new user inputs are then saved to a json file, and are able to be accessed by the bot. 

## Programming Tutor Bot

March 2019

*ProgrammingTutorBot.py*

This is a work in progress bot. The idea is for the bot to be able to show simple references to
things in multiple programming languages. 

For instance, if I wanted to find out about Javascript's "if" statements, the bot could respond:

```
if (answer === 'dog') { 
        // here is the stuff
        } else {
            // more stuff here
        }
```

I also added functionality to get the lyrics to the song you are currently listening (using Spotify) - but I still need  to make it so that each user in the room can do this, not just me.