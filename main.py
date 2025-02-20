# Author: https://github.com/teuncm

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patches as patches
import math

PITCH_CLASS_TABLE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

# Number of frets to show.
frets = range(1, 25)
# Harmonics to show nodes of.
harmonics = range(2, 10)


def main():
    # print(get_harmonic_intensity(5.5, harmonics))
    for root_note in PITCH_CLASS_TABLE:
        plot_data(root_note)
        print("Finished", root_note, "string")

    print("Done!")


def plot_data(root_note):
    """Plot all fret and flagiolet data for the given root note."""
    # Figure styling.
    plt.rc("font", size=10)
    plt.rc("font", family="monospace")

    grayscale_cmap = plt.get_cmap("gray_r")

    _, ax = plt.subplots(figsize=(18, 3.8), layout="constrained")
    ax.axhline(1, alpha=1, color="darkorange", linewidth=1, label="frets", zorder=-1)
    ax.axhline(0, alpha=1, color="darkblue", linewidth=1, label="flageolets", zorder=-1)
    ax.set_xlim([0, 1])
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x * 100:.0f}"))
    ax.set_ylim([-0.5, 1.5])
    ax.set_xlabel("Distance from nut to bridge (%)")
    ax.get_yaxis().set_visible(False)
    plt.title(f"Locations of first 9 flageolets on {root_note}-string with detune (ct)")
    plt.legend()

    # Draw zero fret.
    draw_text(ax, 0, 1, f"0\n{root_note}")

    # Draw zero flageolet.
    draw_text(ax, 0, 0, f"$f_0$\n{root_note}")

    # Index of root note in pitch class table. Used later to calculate notes.
    root_idx = PITCH_CLASS_TABLE.index(root_note)

    existing_distances = set()
    for harmonic in harmonics:
        # Every nth harmonic has n-1 nodes on the string. Iterate through
        # all of them.
        for numerator in range(1, harmonic):
            distance = numerator / harmonic

            # Check for existing lower-order nodes.
            if distance in existing_distances:
                continue

            existing_distances.add(distance)

            # Calculate distance from root note.
            num_semitones = freq_ratio_to_semitones(harmonic)
            rounded_num_semitones = round(num_semitones)
            num_octaves = semitones_to_octaves(num_semitones)

            # Calculate nearest equally tempered note.
            pitch_class_idx = (root_idx + rounded_num_semitones) % 12
            pitch_class = PITCH_CLASS_TABLE[pitch_class_idx]

            # Calculate cent offset from nearest equally tempered note.
            num_cents = 100 * (num_semitones - rounded_num_semitones)
            rounded_num_cents = round(num_cents)

            # Draw flageolets.
            num_cents_str = "" if rounded_num_cents == 0 else f"\n{rounded_num_cents:+}"
            pitch_str = f"{pitch_class}$^{{{num_octaves}}}$"
            intensity = get_harmonic_intensity(harmonic)
            color = grayscale_cmap(intensity)
            ax.eventplot(
                [distance], lineoffsets=0, linelengths=3, linewidths=1, color=color
            )
            draw_text(ax, distance, 0, f"${harmonic}f_0$\n{pitch_str}{num_cents_str}")

    # Mark frets with a single dot.
    marked_frets = [3, 5, 7, 9, 15, 17, 19, 21, 27, 29, 31, 33]
    # Mark octaves with two dots.
    marked_octaves = [12, 24, 36]

    for fret in frets:
        # Use equal temperament for fret spacing calculations.
        distance = get_fret_position(fret)

        # Calculate distance from root note.
        num_octaves = semitones_to_octaves(fret)

        # Pitch class is simply the next note for each consecutive fret.
        pitch_class_idx = (root_idx + fret) % 12
        pitch_class = PITCH_CLASS_TABLE[pitch_class_idx]

        # Draw frets.
        octave_str = "" if num_octaves == 0 else f"$^{{{num_octaves}}}$"
        ax.eventplot(
            [distance], lineoffsets=1, linelengths=0.75, linewidths=1, color="black"
        )
        draw_text(ax, distance, 1, f"{fret}" + f"\n{pitch_class}{octave_str}")

        # Draw dot markers.
        dot_distance = get_fret_position(fret - 0.5)
        if fret in marked_frets:
            draw_text(ax, dot_distance, 0.5, "●")
        if fret in marked_octaves:
            draw_text(ax, dot_distance, 0.5, "●●")

        # Draw rectangular markers.
        if fret in marked_frets or fret in marked_octaves:
            rect_left = get_fret_position(fret - 0.7)
            rect_right = get_fret_position(fret - 0.3)
            rect_width = rect_right - rect_left
            rect_height = 0.4

            rect = patches.Rectangle(
                (rect_left, 1 - rect_height / 2),
                rect_width,
                rect_height,
                linewidth=1,
                edgecolor="gray",
                facecolor="gray",
                zorder=10,
            )

            ax.add_patch(rect)

    plt.savefig(f"output/flageolets_{root_note}.png", bbox_inches="tight", dpi=200)


def freq_ratio_to_semitones(freq_ratio):
    """Convert a frequency ratio to tonal distance in semitones."""
    num_semitones = 12 * math.log(freq_ratio, 2)

    return num_semitones


def semitones_to_octaves(num_semitones):
    """Convert semitone distance to octave distance."""
    num_octaves = math.floor(num_semitones / 12)

    return num_octaves


def get_fret_position(fret):
    """Get the position of a fret on the fretboard."""
    position = 1 - 2 ** (-(fret / 12))

    return position


def get_harmonic_intensity(harmonic):
    """Get intensity of harmonic (used for coloring)."""
    intensity = 1 / ((harmonic - 1) / 1.75)

    return intensity


def draw_text(ax, x, y, text):
    """Draw text on the given Axes."""
    ax.text(
        x,
        y,
        text,
        horizontalalignment="center",
        verticalalignment="center",
        bbox=dict(facecolor="white", edgecolor="none", boxstyle="round, pad=0.1"),
        zorder=11,
    )


if __name__ == "__main__":
    main()
