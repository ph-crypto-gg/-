class Athlete:
    def __init__(self, name, best_time):
        self.name = name
        self.best_time = best_time

    @property
    def best_time(self):
        return self._best_time

    @best_time.setter
    def best_time(self, value):
        if value <= 0:
            raise ValueError("Время должно быть положительным")
        self._best_time = value

    def train(self, time):
        if time <= 0:
            raise ValueError("Время должно быть положительным")
        self.best_time = min(self.best_time, time)

    def result(self):
        return f"{self.name}: {self.best_time} с"


class Runner(Athlete):
    def __init__(self, name, best_time, distance):
        super().__init__(name, best_time)
        self.distance = distance

    def result(self):
        return f"Бегун {self.name}: {self.distance} м за {self.best_time} с"


class Swimmer(Athlete):
    def __init__(self, name, best_time, pool_length):
        super().__init__(name, best_time)
        self.pool_length = pool_length

    def result(self):
        return f"Пловец {self.name}: бассейн {self.pool_length} м за {self.best_time} с"


class SportClub:
    def __init__(self, name):
        self.name = name
        self.athletes = []

    def add(self, athlete):
        self.athletes.append(athlete)

    def show(self):
        print("Клуб:", self.name)
        for athlete in self.athletes:
            print(athlete.result())


def main():
    club = SportClub("Старт")
    runner = Runner("Максим", 14.0, 100)
    club.add(runner)
    club.add(Runner("Иван", 28.0, 200))
    club.add(Swimmer("Анна", 35.0, 50))
    club.show()
    runner.train(13.5)
    print("После тренировки:", runner.result())


if __name__ == "__main__":
    main()
