#!/usr/bin/env python3
"""
Filename: printclr.py
Author: Plum
Date: 10/11/2026

Simple print color function
Uses ANSI codes to print colored text to terminal

printclr():
	Args:
		text: Text to print to terminal
		text_color: Color of text to print
		bg_color: Color of text background to print
		style: Style of text to print
	Returns:
		Prints text variable in chosen text color and background color. (prints text normally when no args provided)

printclr_testall():
Args:
	style: Style of text to print
Returns:
	Prints table with all bg and text colors for testing

Available text/bg colors: red, green, blue, purple, cyan, yellow, black, grey (prepend hi_ for high intensity)
Available text style types: normal, faint, bold

Examples: 

Print with red text color and blue background color:
printclr("Color print test", text_color="red", bg_color="blue", style="normal")

Print with bold green text color:
printclr("Color print test", text_color="green", style="bold")

Print table to test all bg and text colors: 
printclr_testall(style="normal")
"""

import sys

# Windows systems do not have ANSI escape codes enabled by default
# Add flag ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004 to enable ANSI escape codes
if sys.platform == "win32":
    import ctypes
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ANSI color codes for text and background
text_colors = {
	"red": "31",
	"hi_red": "91",
	"green": "32",
	"hi_green": "92",
	"blue": "34",
	"hi_blue": "94",
	"purple": "35",
	"hi_purple": "95",
	"cyan": "36",
	"hi_cyan": "96",
	"yellow": "33",
	"hi_yellow": "93",
	"black": "30",
	"hi_black": "90",
	"grey": "37",
	"hi_grey": "97"
}

bg_colors = {
	"red": "41",
	"hi_red": "101",
	"green": "42",
	"hi_green": "102",
	"blue": "44",
	"hi_blue": "104",
	"purple": "45",
	"hi_purple": "105",
	"cyan": "46",
	"hi_cyan": "106",
	"yellow": "43",
	"hi_yellow": "103",
	"black": "40",
	"hi_black": "100",
	"grey": "47",
	"hi_grey": "107"
}

# printclr function
def printclr(text, text_color="", bg_color="", style="normal"):

	# ANSI style codes
	if style == "normal":
		style = "0"
	elif style ==  "bold":
		style = "1"
	elif style == "faint":
		style = "2"

	# Check if text/bg color is a valid color and get ANSI color code
	text_ansi_code = None
	bg_ansi_code = None
	if text_color in text_colors:
		text_ansi_code = text_colors[text_color]
	if bg_color in bg_colors:
		bg_ansi_code = bg_colors[bg_color]

	# Format final ANSI code and print to terminal
	if text_ansi_code != None or bg_ansi_code != None:
		ansi_code = "\033[%s;" % (style)
		if text_ansi_code != None:
			ansi_code += text_ansi_code
		if bg_ansi_code != None:
			ansi_code += ";%s" % (bg_ansi_code)
		ansi_code += "m"
		print("%s%s\033[0m" % (ansi_code, text))
	else:
		# Print normal if no colors selected or not a valid color
		print(text)

# printclr_testall function
def printclr_testall(style="normal"):

	# ANSI style codes
	if style == "normal":
		style = "0"
	elif style ==  "bold":
		style = "1"
	elif style == "faint":
		style = "2"

	final_string = ""
	for bg_color, bg_acode in bg_colors.items():
		for text_color, text_acode in text_colors.items():
			text_color2 = text_color.center(9)
			final_string += "\033[%s;%s;%sm%s\033[0m" % (style, text_acode, bg_acode, text_color2)
		# Final color in list, add line break for next bg color
		final_string += " (%s)\n" % (bg_color)
	print(final_string)