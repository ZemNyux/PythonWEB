from dataclasses import dataclass

@dataclass
class NeighborAbove:
    name: str
    has_drill: bool
    pacing_speed: int
    music_volume: int

    def start_drilling(self):
        if self.has_drill:
            print(f"Сусід {self.name} увімкнув перфоратор о 7 ранку!")
        else:
            print(f"У {self.name} немає дрелі, тому він просто стукає молотком по батареї.")

    def walk_like_elephant(self):
        print(f"Сусід {self.name} тупцює зі швидкістю {self.pacing_speed} км/год, ніби вдягнув чавунні тапочки.")

    def play_music(self):
        print(f"У квартирі вище врубали музику на {self.music_volume}% гучності. Стіни дрижать!")

    def drop_metal_ball(self):
        print(f"О! {self.name} щойно вронив металеву кулю на підлогу, і вона покотилася... Класика!")

if __name__ == "__main__":
    neighbor1 = NeighborAbove(name="Дядя Толя", has_drill=True, pacing_speed=15, music_volume=90)
    neighbor2 = NeighborAbove(name="Олег", has_drill=False, pacing_speed=20, music_volume=100)

    print("День 1")
    neighbor1.start_drilling()
    neighbor1.walk_like_elephant()
    neighbor1.drop_metal_ball()

    print("\nДень 2")
    neighbor2.play_music()
    neighbor2.start_drilling()
    neighbor2.drop_metal_ball()