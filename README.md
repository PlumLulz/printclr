## printclr
Simple print color function utilizing ANSI escape codes.

## Install

`pip install printclr`

## Usage

```python
from printclr import printclr, printclr_testall

# High intensity grey text color with high intensity red backgroun color
printclr("Color print test", text_color="hi_grey", bg_color="hi_red")

# Print with bold green text color:
printclr("Color print test", text_color="green", style="bold")

# Print table of all text and bg colors with normal text style
printclr_testall(style="normal")
```

## printclr() and printclr_testall() structure
```
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
```

## Available text/background colors
```
Text/background colors: red, green, blue, purple, cyan, yellow, black, grey (prepend hi_ for high intensity)
Text style types: normal, faint, bold
```

## printclr_testall() output
![image](https://i.imgur.com/2vd9MJS.png)