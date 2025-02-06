import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import math

PITCH_CLASS_TABLE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Distance from nut to bridge in %.
scale_length = 100
# Number of frets to show.
frets = np.arange(1, 25)
# Harmonics to show nodes of.
harmonics = [2, 3, 4, 5, 6, 7, 8, 9]
# Root note of string.
root_note = "E"


def main():
    plt.rc("font", size=10)
    plt.rc("font", family="monospace")

    _, ax = plt.subplots(figsize=(18, 3.6), layout="constrained")

    # Figure styling.
    ax.axhline(1, alpha=1, color="darkorange", linewidth=1, label="frets")
    ax.axhline(0, alpha=1, color="darkblue", linewidth=1, label="flageolets")
    ax.set_xlim([0, scale_length])
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.set_ylim([-0.5, 1.5])
    ax.set_xlabel("Distance from nut to bridge (%)")
    ax.get_yaxis().set_visible(False)
    bbox_style = dict(facecolor="white", edgecolor="none", boxstyle="round, pad=0.1")
    plt.title(
        f"Fretboard locations of first 9 flageolets on {root_note} string with notes and detune (ct)"
    )
    plt.legend()

    root_idx = PITCH_CLASS_TABLE.index(root_note)

    # Reverse harmonics as multiples are drawn on top of eachother.
    for harmonic in reversed(harmonics):
        for numerator in range(1, harmonic):
            distance = scale_length * numerator / harmonic
            num_semitones = freq_ratio_to_semitones(harmonic)
            rounded_num_semitones = round(num_semitones)

            # Calculate nearest equally tempered note.
            pitch_class_idx = (root_idx + rounded_num_semitones) % 12
            pitch_class = PITCH_CLASS_TABLE[pitch_class_idx]

            # Calculate cent offset from nearest equally tempered note.
            num_cents = 100 * (num_semitones - rounded_num_semitones)
            rounded_num_cents = round(num_cents)

            ax.plot(
                distance,
                0,
                color="black",
                marker="|",
                ms=1000,
                alpha=0.22,
                markeredgewidth=1,
            )
            ax.text(
                distance,
                0,
                rf"${harmonic}f_0$"
                + "\n"
                + f"{pitch_class}"
                + "\n"
                + f"{rounded_num_cents:+}",
                horizontalalignment="center",
                verticalalignment="center",
                bbox=bbox_style,
            )

    # Mark frets with a single dot.
    marked_frets = [3, 5, 7, 9, 15, 17, 19, 21, 27, 29, 31, 33]
    # Mark octaves with two dots.
    marked_octaves = [12, 24, 36]

    for fret in frets:
        # Use equal temperament for fret spacing calculations.
        distance = scale_length - scale_length / 2 ** (fret / 12)
        pitch_class_idx = (root_idx + fret) % 12
        pitch_class = PITCH_CLASS_TABLE[pitch_class_idx]

        ax.plot(
            distance, 1, color="gray", marker="|", ms=70, alpha=1, markeredgewidth=1
        )
        ax.text(
            distance,
            1,
            f"{fret}" + "\n" + f"{pitch_class}",
            horizontalalignment="center",
            verticalalignment="center",
            bbox=bbox_style,
        )

        if fret in marked_frets:
            ax.text(
                distance,
                0.5,
                f"●",
                horizontalalignment="center",
                verticalalignment="center",
            )

        if fret in marked_octaves:
            ax.text(
                distance,
                0.5,
                f"●●",
                horizontalalignment="center",
                verticalalignment="center",
            )

    plt.savefig("flageolets.png", bbox_inches="tight", dpi=200)
    plt.show()


def freq_ratio_to_semitones(freq_ratio):
    """Convert a frequency ratio to tonal distance in semitones."""
    num_semitones = 12 * math.log(freq_ratio, 2)

    return num_semitones


if __name__ == "__main__":
    main()
