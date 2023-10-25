class RGBColor:
    """
    A class for colors in rgb format
    """
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def format(self):
        """
        Returns string formatted into rgb
        """
        return f"RGB ({self.red}, {self.green}, {self.blue})"

    def apply_color(self, text):
        """
        ANSI escape codes for color formatting
        """
        return f"\x1b[38;2;{self.red};{self.green};{self.blue}m{text}\x1b[0m"


# Dictionary of colors
color = {
    "orange": RGBColor(232, 70, 16),
    "yellow": RGBColor(232, 178, 16),
    "green": RGBColor(110, 146, 11)
}
