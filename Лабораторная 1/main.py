# TODO Написать 3 класса с документацией и аннотацией типов

from abc import ABC


class Tree(ABC):
    """
    Класс, описывающий абстракцию дерева как биологического объекта.
    """

    def __init__(self, height: float, age: int, species: str):
        """
        Инициализация объекта дерева.

        :param height: Высота дерева в метрах (должна быть положительной).
        :type height: float
        :param age: Возраст дерева в годах (не может быть отрицательным).
        :type age: int
        :param species: Название вида дерева.
        :type species: str
        :raises ValueError: Если высота <= 0 или возраст < 0.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.height = height
        self.age = age
        self.species = species

    def grow(self, meters: float) -> None:
        """
        Увеличивает высоту дерева на указанное значение.

        :param meters: На сколько метров выросло дерево (должно быть > 0).
        :type meters: float
        :return: None
        :rtype: None

        >>> t = Tree(5.0, 10, "Oak")
        >>> t.grow(1.5)
        """
        if meters <= 0:
            raise ValueError("Дерево не может вырасти на неположительное значение.")
        ...

    def shed_leaves(self, season: str) -> bool:
        """
        Имитирует сбрасывание листьев в определенный сезон.

        :param season: Название сезона (например, 'Autumn').
        :type season: str
        :return: True, если листья сброшены, иначе False.
        :rtype: bool

        >>> t = Tree(5.0, 10, "Oak")
        >>> t.shed_leaves("Autumn")
        """
        if not isinstance(season, str):
            raise TypeError("Сезон должен быть строкой.")
        ...



class SocialAccount(ABC):
    """
    Класс, описывающий абстракцию учетной записи пользователя в соцсети.
    """

    def __init__(self, username: str, age: int):
        """
        Создание учетной записи.

        :param username: Имя пользователя (длина от 3 до 20 символов).
        :type username: str
        :param age: Возраст пользователя (минимум 13 лет).
        :type age: int
        :raises ValueError: Если имя недопустимо или возраст меньше 13.
        """
        if not (3 <= len(username) <= 20):
            raise ValueError("Имя пользователя должно быть от 3 до 20 символов.")
        if age < 13:
            raise ValueError("Минимальный возраст для регистрации — 13 лет.")

        self.username = username
        self.age = age
        self.is_banned = False

    def change_username(self, new_username: str) -> bool:
        """
        Изменяет имя пользователя.

        :param new_username: Новое имя пользователя.
        :type new_username: str
        :return: True, если изменение успешно.
        :rtype: bool

        >>> acc = SocialAccount("user123", 18)
        >>> acc.change_username("new_user")
        """
        if not (3 <= len(new_username) <= 20):
            raise ValueError("Новое имя должно быть от 3 до 20 символов.")
        ...

    def ban(self, reason: str) -> None:
        """
        Блокирует учетную запись.

        :param reason: Причина блокировки.
        :type reason: str
        :return: None
        :rtype: None

        >>> acc = SocialAccount("user123", 18)
        >>> acc.ban("Violation of rules")
        """
        if not isinstance(reason, str):
            raise TypeError("Причина должна быть строкой.")
        ...



class Vehicle(ABC):
    """
    Класс, описывающий абстракцию транспортного средства.
    """

    def __init__(self, max_speed: float, weight: float, fuel_level: float):
        """
        Инициализация транспортного средства.

        :param max_speed: Максимальная скорость транспорта в км/ч (должна быть > 0).
        :type max_speed: float
        :param weight: Вес транспорта в кг (должен быть > 0).
        :type weight: float
        :param fuel_level: Уровень топлива в литрах (не может быть отрицательным).
        :type fuel_level: float
        :raises ValueError: Если скорость или вес <= 0, или топливо < 0.
        """
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть положительным числом.")
        if weight <= 0:
            raise ValueError("Вес транспорта должен быть положительным числом.")
        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным.")

        self.max_speed = max_speed
        self.weight = weight
        self.fuel_level = fuel_level

    def accelerate(self, speed: float) -> None:
        """
        Увеличивает скорость движения до указанного значения.

        :param speed: Целевая скорость в км/ч (должна быть > 0 и <= max_speed).
        :type speed: float
        :return: None
        :rtype: None
        :raises ValueError: Если скорость недопустима.

        >>> v = Vehicle(200.0, 1500.0, 50.0)
        >>> v.accelerate(100.0)
        """
        if speed <= 0 or speed > self.max_speed:
            raise ValueError("Скорость должна быть в пределах допустимого диапазона.")
        ...

    def refuel(self, volume: float) -> None:
        """
        Добавляет топливо в бак.

        :param volume: Объем топлива для заправки в литрах (должен быть > 0).
        :type volume: float
        :return: None
        :rtype: None

        >>> v = Vehicle(200.0, 1500.0, 50.0)
        >>> v.refuel(20.0)
        """
        if volume <= 0:
            raise ValueError("Объем заправки должен быть положительным числом.")
        ...

    def stop(self) -> bool:
        """
        Останавливает транспортное средство.

        :return: True, если остановка успешна.
        :rtype: bool

        >>> v = Vehicle(200.0, 1500.0, 50.0)
        >>> v.stop()
        """
        ...