from printclr import printclr, printclr_testall

# High intensity grey text color with high intensity red backgroun color
printclr("Color print test", text_color="hi_grey", bg_color="hi_red")

# Print with bold green text color:
printclr("Color print test", text_color="green", style="bold")

# Print table of all text and bg colors with normal text style
printclr_testall(style="normal")