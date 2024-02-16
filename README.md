# spoti-logger
A tool that retrieves information about spotify events, like current song playng.
Can also be used to mark as 'LIKED' a song simply pressing CTRL + ALT + p.
The songs played by spotify can be accessed in the file "songs.txt" (the program will create automatically if it doesn't exists)

At the start you can choose to pass data manually, intead of a json file in form of:

{
  "client-id":"your-client-id",
  "secret-id":"your-secret-id",
  "redirect-url":"your-redirect-url"
}

After selecting the option, the program starts to log the songs and listen to key pressed.

