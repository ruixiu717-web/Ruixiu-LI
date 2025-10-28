#Defining a 2-dimensional list for the keys to be pressed
progression = [
    [48, 52, 55],   # C major
    [43, 47, 50],   # G major
    [45, 48, 52],   # A minor
    [41, 45, 48]    # F major
]

# Single looping structure for accompaniment
for chord in progression:
    playNote(chord, beats=2)     # play the chord for 2 beats
    rest(0.5)                    # short rhythmic gap
    playNote(chord, beats=1)     # repeat same chord briefly
    rest(0.5)                    # let melody breathe
