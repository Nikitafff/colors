class Color:
    END = '\033[0'
    START = '\033[1;38;2'
    MOD = 'm'

    def __init__(self, red, green, blue):
        self.colors = (red, green, blue)

    def __str__(self):
        rgb_color = ';'.join(map(str, self.colors))
        return f'{self.START};{rgb_color}{self.MOD}●{self.END}{self.MOD}'

    def __eq__(self, other):
        if isinstance(other, Color):
            return self.colors == other.colors
        return False

    def __add__(self, other):
        if isinstance(other, Color):
            new_colors = (min(sum(x), 255) for x in zip(self.colors, other.colors))
            return Color(*new_colors)
        return False


class B:
    pass


red_color = Color(255, 0, 0)
red_colors = Color(255, 0, 0)
green_color = Color(0, 255, 0)
b = B()
print(red_color == green_color)
print(red_color == red_colors)
print(red_colors, green_color)
print(b == red_colors)
print(red_colors == b)
print(red_colors + green_color)
