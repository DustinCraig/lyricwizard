# Dustin Craig
# July 21, 2020
# LyricWizard - Single day Python project to create a wordmap of any song using the GeniusLyrics API
import lyricsgenius as lg
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS


TOKEN = ''
genius = lg.Genius(TOKEN, skip_non_songs=True, excluded_terms=[
                   "(Remix)", "(Live)"], remove_section_headers=True, verbose=False)


def get_song(songname='', artist=''):
    """get_song will search lyricsgenius for a specific song by a specific artist. Returns the song lyrics, or None if there were invalid parameters"""
    try:
        song = genius.search_song(songname, artist)
        return song.lyrics
    except:
        return None


while True:
    try:
        userinput = input(
            'Enter a song and an artist (separated by a comma) or quit to exit: ').split(',')
        if len(userinput) == 1 and userinput[0].lower() == 'quit':
            break
        if len(userinput) != 2:
            raise Exception()
    except:
        print('Invalid input')
        continue

    song = userinput[0]
    artist = userinput[1]

    if not len(song) or not len(artist):
        print('Invalid input')
        continue

    lyrics = get_song(song, artist)

    if lyrics is None:
        print('Invalid artist or songname ', song, artist)
    else:
        wordcloud = WordCloud(width=800, height=800, background_color='white',
                              ).generate(lyrics)
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.title(song)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        plt.show()
