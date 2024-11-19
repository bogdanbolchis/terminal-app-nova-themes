#!/usr/bin/env python3

# Execute this python code from inside a Nova local terminal session.
# Then in Terminal, use the color picker to configure each color of the profile.

rectangle = '\u2588\u2588\u2588'

def print_colors_starting_with(color_code):
    for color in range(color_code, color_code + 8):
        print(f"\033[{color}m{rectangle}\t", end=" ")
    print("")

print(f"Text:\t\t {rectangle}")
print(f"Bold text:\t\033[0;m {rectangle}\033[0m")
print("\nANSI Colors:")
print_colors_starting_with(30)
print_colors_starting_with(90)