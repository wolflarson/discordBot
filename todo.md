# ToDo

## global

- we should have a way to test every command quickly.
- we need to do more input validation. url encode everything I think.
## !play

- some commands might be !play youbue.com?asdfadf" this would play audio
## !jokes

- we should have an array of types of jokes it can send. currently only chuck norris jokes are supported
- some of the joke apis have search features. we could search for a string with a sub command !joke search <term>
## !earthporn

- !earthporn will grab a top photo from /r/earthporn and post it in chat. the image not just the link

- it would be cool if we could figure out how to pull out the more complicated tasks into their own file. dar says we should figure out how to import them like a module.

## !google

- we need to do some input validation perhaps urlencode?
## !ddg

- !ddg <string> drops the first link in the response from duckduckgo in the chat

## idle timer

- !last <username> track how long it has been since a user was active in the server (voice or text) and report that with a

## ping / pong

 - responds with pong / ping

## !hn

 - grabs the top news from hacker news

## !btc

- right now we have a magic number, we should find a way to get rid of that
- We should support multiple exchanges
- we should support converting to other currency

## !date

 - gives date and time (do timezones?)

## !hello

 - sends a compliment to the person who sent the message. (Call them out by name.)
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