# ToDo

## global

- we should have a way to test every command quickly.
- logging: just count to 30 rename all older files by one and delete any over 30.  stat the file and grab the timestapm from when it was creatdd and use that instead of now()
- we should catch ctrl+c (exit) and rotate the log file at close?
## !play

- some commands might be !play youbue.com?asdfadf" this would play audio
## !jokes

- we should have an array of types of jokes it can send. currently only chuck norris jokes are supported
- some of the joke apis have search features. we could search for a string with a sub command !joke search <term>
## !earthporn

- !earthporn will grab a top photo from /r/earthporn and post it in chat. the image not just the link

## !google

## !ddg

- !ddg <string> drops the first link in the response from duckduckgo in the chat
 - this is not working. it seems they encode the results in the html to prevent exactly what I'm doing. needs more looging into

## !last - idle timer

- !last <username> track how long it has been since a user was active in the server (voice or text) and report that with a

## !hn

 - grabs the top news from hacker news

## !btc

- We should support multiple exchanges
- we should support converting to other currency

## !date

 - gives date and time (do timezones?)

## !hello

 - sends a compliment to the person who sent the message. (Call them out by name.)

## !yt

 - searches youtube
## admin features

to do this we need to learn how to check the role of the requester.
 - !kick
 - !ban
 - !unban
 - !mute
 - !unmute
 - !invite - create new invite link
 - !users - list users in the current room / server
 - !tell <user> - waits for <user> to post something then tells them a message on behalf of X user. public to everyone.