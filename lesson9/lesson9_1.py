class Automobile():
    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine

    @classmethod
    def go_ahead(cls):
        print("Еду вперед")
    @classmethod
    def drive_back(cls):
        print("Еду назад")


class Automobile_next(Automobile):
    @classmethod
    def turn_right(cls):
        print("Еду направо")
    @classmethod
    def turn_left(cls):
        print("Еду налево")


auto = Automobile(model="Nisan", color="зелёного", engine="1.6")
auto.go_ahead()
auto.drive_back()
Automobile_next.turn_left()
Automobile_next.turn_right()