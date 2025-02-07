# Flageolet Map

While learning to play guitar, I stumbled upon the existence of [flageolets](https://en.wikipedia.org/wiki/String_harmonic), which are an alternative way to produce notes on the guitar. Flageolets are seen to be played at the 2nd, 5th, 7th, 9th and 12th frets, but are they actually located there? This flageolet map shows that they are offset slightly, except at fret 12. Moreover, this map shows all flageolet locations, even those located past the fretboard.

### Theory 

#### Vibration and natural harmonics

To investigate what flagiolets are, we need to dive into the physics of vibrating strings. An excited string tends to vibrate in modes (harmonics) that divide the length of the string into an integer ($1, 2, 3, 4, \dots$) number of divisions. The first division, i.e. the string as a whole, will vibrate with what we call the fundamental frequency. The fundamental frequency $f_0$ of a vibrating string depends on the length $L$ of the string, its tension $T$ and its density $\mu$ as follows: 

$$ f_0 = \frac{1}{2L} \sqrt{\frac{T}{\mu}} $$

This formula implies that the fundamental frequency of a vibrating string is inversely proportional to its length. As an aside, this also implies that tensioning the string increases the fundamental frequency and making it heavier decreases it, explaining comparatively long and heavy strings on bass guitars to produce sound an octave lower than usual. 

Given the fundamental frequency $f_0$ of any tensioned string, its harmonics will therefore vibrate at $f_0, 2f_0, 3f_0, 4f_0, \dots$ since the successive modes divide the string evenly into vibrating sections of $L, \frac{1}{2}L, \frac{1}{3}L, \frac{1}{4}L, \dots$, separated by nodes that appear to stand still. A flageolet is played on string instruments by pressing the finger lightly on these nodes. When the string is plucked this way, all harmonics without a node at the finger position are dampened, making the string vibrate at the resulting higher fundamental frequency and its respective harmonics.

#### Fretboard

Fretboards are constructed using [12-tone equal temperament](https://en.wikipedia.org/wiki/12_equal_temperament), which increases the frequency of every successive note by a factor of

$$ 2 ^ {1/12} $$

such that after 12 notes, we reach the same note on the next octave with 2 times the frequency of the previous octave. This tuning is not [pure](https://en.wikipedia.org/wiki/Just_intonation), meaning that intervals (except the octave) are never exact whole number ratios and every note is slightly off tune. An advantage of equal temperament is that the entire octave is divided into equal segments, which is also visible on the fretboard as every successive fret decreases the length of the string by a factor of

$$ 2 ^ {-1/12} $$

This implies that the 12th fret is located halfway between the nut and bridge and the spacing between each fret decreases exponentially, giving rise to the familiar fretboard.

So, where most notes on the fretboard are always slightly off tune, flagiolets are always exactly on tune. Only the octave frets ($12, 24, 36, \dots$) correspond exactly in frequency to some flagiolets ($2, 4, 8, 16, \dots$) as both are equal integer multiples of $f_0$.

#### Detune

Detune can be measured in [semitones](https://en.wikipedia.org/wiki/Semitone) (st) and more precisely in cents (ct), which is a 100th of a semitone. One semitone is the distance between two consecutive notes on the equally tempered chromatic scale, differing in frequency by a factor of $2 ^ {1/12}$, or $\frac{1}{12}th of an octave. The total number of semitones between two frequencies $f1$ and $f_2$ is therefore determined by their frequency ratio as follows:

$$ st = 12 \cdot log_2(\frac{f_1}{f_2}) $$

Assuming the first frequency represents a note on an equally tempered scale, every whole semitone away will also represent a note. Therefore, the signed cent offset of the second frequency from the nearest note is given by

$$ ct = 100 \cdot (st - round(st)) $$

which is the same measure as commonly seen on digital guitar tuners.
