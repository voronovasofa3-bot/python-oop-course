from datetime import datetime


class Vehicle:
    """
    Базовый класс для представления транспортных средств.

    Attributes:
        brand (str): Марка транспортного средства
        model (str): Модель транспортного средства
        _year (int): Год выпуска (защищенный атрибут)
        _max_speed (float): Максимальная скорость в км/ч (защищенный атрибут)
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: float) -> None:
        """
        Инициализация объекта транспортного средства.

        Args:
            brand: Марка транспортного средства
            model: Модель транспортного средства
            year: Год выпуска
            max_speed: Максимальная скорость в км/ч
        """
        self.brand = brand
        self.model = model
        self._year = year
        self._max_speed = max_speed
        self._is_moving = False

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта в удобочитаемом формате.

        Returns:
            str: Строка с описанием транспортного средства
        """
        return f"{self.brand} {self.model} ({self._year} год)"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление объекта.

        Returns:
            str: Строка для воспроизведения объекта
        """
        return f"Vehicle(brand='{self.brand}', model='{self.model}', year={self._year}, max_speed={self._max_speed})"

    def start_engine(self) -> str:
        """
        Запускает двигатель транспортного средства.

        Returns:
            str: Сообщение о запуске двигателя
        """
        self._is_moving = True
        return f"Двигатель {self.brand} {self.model} запущен"

    def stop_engine(self) -> str:
        """
        Останавливает двигатель транспортного средства.

        Returns:
            str: Сообщение об остановке двигателя
        """
        self._is_moving = False
        return f"Двигатель {self.brand} {self.model} остановлен"

    def get_max_speed(self) -> float:
        """
        Возвращает максимальную скорость транспортного средства.

        Returns:
            float: Максимальная скорость в км/ч
        """
        return self._max_speed

    def get_age(self) -> int:
        """
        Вычисляет возраст транспортного средства.

        Returns:
            int: Возраст в годах
        """
        current_year = datetime.now().year
        return current_year - self._year


class Car(Vehicle):
    """
    Класс для представления автомобилей.

    Наследуется от класса Vehicle и добавляет специфичные для автомобилей
    характеристики и методы.

    Attributes:
        brand (str): Марка автомобиля
        model (str): Модель автомобиля
        _year (int): Год выпуска
        _max_speed (float): Максимальная скорость в км/ч
        _num_doors (int): Количество дверей (защищенный атрибут)
        _fuel_type (str): Тип топлива (защищенный атрибут)
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: float,
                 num_doors: int = 4, fuel_type: str = "gasoline") -> None:
        """
        Инициализация объекта автомобиля.

        Args:
            brand: Марка автомобиля
            model: Модель автомобиля
            year: Год выпуска
            max_speed: Максимальная скорость в км/ч
            num_doors: Количество дверей (по умолчанию 4)
            fuel_type: Тип топлива (по умолчанию 'gasoline')
        """
        super().__init__(brand, model, year, max_speed)
        self._num_doors = num_doors
        self._fuel_type = fuel_type

    def __str__(self) -> str:
        """
        Возвращает строковое представление автомобиля.

        Returns:
            str: Строка с описанием автомобиля
        """
        base_str = super().__str__()
        return f"{base_str}, {self._num_doors} дверей"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление автомобиля.

        Returns:
            str: Строка для воспроизведения объекта
        """
        # Используем self._year и self._max_speed - они унаследованы от Vehicle
        return (f"Car(brand='{self.brand}', model='{self.model}', year={self._year}, "
                f"max_speed={self._max_speed}, num_doors={self._num_doors}, "
                f"fuel_type='{self._fuel_type}')")

    def start_engine(self) -> str:
        """
        Запускает двигатель автомобиля.

        Returns:
            str: Сообщение о запуске двигателя автомобиля
        """
        self._is_moving = True
        return f"Автомобиль {self.brand} {self.model} ({self._fuel_type}) заведен"

    def get_num_doors(self) -> int:
        """
        Возвращает количество дверей автомобиля.

        Returns:
            int: Количество дверей
        """
        return self._num_doors

    def refuel(self, liters: float) -> str:
        """
        Заправляет автомобиль топливом.

        Args:
            liters: Количество литров топлива

        Returns:
            str: Сообщение о заправке
        """
        return f"Автомобиль {self.brand} {self.model} заправлен {liters} л {self._fuel_type}"


class Motorcycle(Vehicle):
    """
    Класс для представления мотоциклов.

    Наследуется от класса Vehicle и добавляет специфичные для мотоциклов
    характеристики и методы.

    Attributes:
        brand (str): Марка мотоцикла
        model (str): Модель мотоцикла
        _year (int): Год выпуска
        _max_speed (float): Максимальная скорость в км/ч
        _engine_capacity (float): Объем двигателя в куб.см (защищенный атрибут)
        _has_sidecar (bool): Наличие коляски (защищенный атрибут)
    """

    def __init__(self, brand: str, model: str, year: int, max_speed: float,
                 engine_capacity: float, has_sidecar: bool = False) -> None:
        """
        Инициализация объекта мотоцикла.

        Args:
            brand: Марка мотоцикла
            model: Модель мотоцикла
            year: Год выпуска
            max_speed: Максимальная скорость в км/ч
            engine_capacity: Объем двигателя в куб.см
            has_sidecar: Наличие коляски (по умолчанию False)
        """
        super().__init__(brand, model, year, max_speed)
        self._engine_capacity = engine_capacity
        self._has_sidecar = has_sidecar

    def __str__(self) -> str:
        """
        Возвращает строковое представление мотоцикла.

        Returns:
            str: Строка с описанием мотоцикла
        """
        base_str = super().__str__()
        sidecar_info = " с коляской" if self._has_sidecar else ""
        return f"{base_str}, {self._engine_capacity} куб.см{sidecar_info}"

    def __repr__(self) -> str:
        """
        Возвращает официальное строковое представление мотоцикла.

        Returns:
            str: Строка для воспроизведения объекта
        """
        # Используем self._year и self._max_speed - они унаследованы от Vehicle
        return (f"Motorcycle(brand='{self.brand}', model='{self.model}', year={self._year}, "
                f"max_speed={self._max_speed}, engine_capacity={self._engine_capacity}, "
                f"has_sidecar={self._has_sidecar})")

    def start_engine(self) -> str:
        """
        Запускает двигатель мотоцикла.

        Returns:
            str: Сообщение о запуске двигателя мотоцикла
        """
        self._is_moving = True
        return f"Мотоцикл {self.brand} {self.model} ({self._engine_capacity} куб.см) заведен"

    def get_engine_capacity(self) -> float:
        """
        Возвращает объем двигателя мотоцикла.

        Returns:
            float: Объем двигателя в куб.см
        """
        return self._engine_capacity

    def perform_wheelie(self) -> str:
        """
        Выполняет подъем переднего колеса (wheelie).

        Returns:
            str: Сообщение о выполнении трюка
        """
        if self._max_speed > 150:
            return f"Мотоцикл {self.brand} {self.model} выполняет wheelie!"
        else:
            return f"Мотоцикл {self.brand} {self.model} недостаточно мощный для wheelie"


# Пример использования классов
if __name__ == "__main__":
    # Создание объектов
    car1 = Car("Toyota", "Camry", 2020, 210.0, 4, "gasoline")
    car2 = Car("BMW", "X5", 2022, 250.0, 5, "diesel")
    moto1 = Motorcycle("Harley-Davidson", "Sportster", 2019, 180.0, 883.0, False)
    moto2 = Motorcycle("Ducati", "Panigale", 2021, 299.0, 1103.0, False)

    # Демонстрация работы методов
    print("=== Базовые методы ===")
    print(str(car1))
    print(repr(car1))
    print()
    print(str(moto1))
    print(repr(moto1))
    print()

    print("=== Наследованные методы ===")
    print(car1.start_engine())
    print(car1.get_max_speed())
    print(f"Возраст автомобиля: {car1.get_age()} лет")
    print()

    print("=== Переопределенные методы ===")
    print(car2.start_engine())
    print(moto2.start_engine())
    print()

    print("=== Специфичные методы дочерних классов ===")
    print(car1.refuel(50))
    print(f"Количество дверей: {car1.get_num_doors()}")
    print(moto2.perform_wheelie())
    print(f"Объем двигателя: {moto1.get_engine_capacity()} куб.см")