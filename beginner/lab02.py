import sys
from azapi import AZlyrics

def get_lyrics(title):
  print('Getting lyrics for {}'.format(title))
  api = AZlyrics('google')
  api.title = title

  lyrics = api.getLyrics()

  return lyrics

def print_lyrics(title):
  title = get_lyrics(title)
  print(title)

if __name__ == '__main__':
  try:
    title = sys.argv[1]
    song_lyrics = get_lyrics(title)
    print(song_lyrics)
  except:
    print('No song title was given')

