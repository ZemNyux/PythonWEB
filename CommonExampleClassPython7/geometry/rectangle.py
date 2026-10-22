from dataclasses import dataclass, field


@dataclass
class Rectangle:
    __width: float = 1.0
    __height: float = 1.0

    @property
    def width(self) -> float:
        return self.__width

    @width.setter
    def width(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Ширина має бути числом (float/int)")
        if value < 0:
            raise ValueError("Ширина не може бути менше 0")
        self.__width = float(value)

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Висота має бути числом (float/int)")
        if value < 0:
            raise ValueError("Висота не може бути менше 0")
        self.__height = float(value)

    def get_area(self) -> float:
        return self.__width * self.__height

    def get_perimeter(self) -> float:
        return 2 * (self.__width + self.__height)