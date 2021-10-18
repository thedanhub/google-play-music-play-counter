# Google Play Music play counter

Some months ago Google dropped the Google Play Music service, but allowed users to download their takeout file. This includes the actual music files, and a bunch of CSV files with song metadata (such as song title, artist, rating, play count etc).

The problem with this takeout file is that it generates _separate_ CSV files for each track, such as this:

```
Title,Album,Artist,Duration (ms),Rating,Play Count,Removed,Playlist Index
"Instant Crush (feat. Julian Casablancas)","Random Access Memories","Daft Punk","337525","0","79","","40"
```

This makes it difficult to see global statistics for your music collection, in case you care to do so. I was curious to see which songs I was listening the most back when I was using Google Play Music, so I created this script simply to loop over all the individual CSV files and prepare an ordered list of your tracks, sorted by number of play counts.

## Example output
```
[1] 79 - Instant Crush (feat. Julian Casablancas), Daft Punk [Random Access Memories]
[2] 35 - Get Lucky (feat. Pharrell Williams), Daft Punk [Random Access Memories]
[3] 34 - Lose Yourself to Dance (feat. Pharrell Williams), Daft Punk [Random Access Memories]
[4] 24 - Ob-La-Di, Ob-La-Da, The Beatles [The Beatles (White Album)]
[5] 21 - Know Your Enemy, Green Day [21st Century Breakdown]
[6] 20 - ¡Viva La Gloria!, Green Day [21st Century Breakdown]
[7] 19 - All Alone On Christmas, Darlene Love [Underground Garage Presents: Christmas a Go-Go]
[8] 18 - 21 Guns, Green Day [21st Century Breakdown]
[9] 16 - The Static Age, Green Day [21st Century Breakdown]
[10] 15 - Give Life Back to Music, Daft Punk [Random Access Memories]
[11] 15 - On The Wing, Owl City [Ocean Eyes]
[12] 14 - Touch (feat. Paul Williams), Daft Punk [Random Access Memories]
[13] 13 - Giorgio by Moroder, Daft Punk [Random Access Memories]
[14] 13 - Within, Daft Punk [Random Access Memories]
[15] 12 - Vanilla Twilight, Owl City [Ocean Eyes]
[16] 11 - The Saltwater Room, Owl City [Ocean Eyes]
[17] 10 - Fireflies, Owl City [Ocean Eyes]
[18] 9 - The Tip Of The Iceberg, Owl City [Ocean Eyes]
[19] 9 - Peacemaker, Green Day [21st Century Breakdown]
[20] 8 - Songbird, Oasis [Heathen Chemistry]
```

Lots of Daft Punk, as it should be.
