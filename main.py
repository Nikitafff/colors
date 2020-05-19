import functools


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    my_colors = {}
    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if args not in my_colors:
            my_colors[args] = cls(*args)
        return my_colors[args]
    return wrapper_singleton


@singleton
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
        if isinstance(other, self.__class__):
            return self.colors == other.colors
        return False

    def __add__(self, other):
        if isinstance(other, self.__class__):
            new_colors = (min(sum(x), 255) for x in zip(self.colors, other.colors))
            return Color(*new_colors)
        return False

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            cl = -256 * (1 - other)
            f = (259 * (cl + 255)) / (255 * (259 - cl))
            new_colors = (int(f * (color - 128) + 128) for color in self.colors)
            return Color(*new_colors)

    def __rmul__(self, other):
        return self.__mul__(other)



class B:
    pass


red_color = Color(255, 0, 0)
red_colors = Color(255, 0, 0)
green_color = Color(0, 255, 0)
blue_color = Color(0, 0, 255)
b = B()

print(red_color == green_color)
print(red_color == red_colors)
print(red_colors, green_color)
print(b == red_colors)
print(red_colors == b)
print(red_colors + green_color)
print(red_colors + blue_color)
print(green_color + blue_color)
print(blue_color * 0.1)
print(red_colors * 0.5)
print(0.5 * red_colors)
print(red_colors is red_color)
