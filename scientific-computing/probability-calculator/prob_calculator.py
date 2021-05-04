import copy
import random
from typing import Any


class Hat:
    def __init__(
        self,
        **kwargs: Any,
    ) -> None:
        self.actual_balls = kwargs
        self.contents = []
        for k, v in kwargs.items():
            self.contents.extend([k] * v)

    def draw(
        self,
        num: int,
    ) -> list:
        drawn = []
        for n in range(num):
            try:
                index = random.randrange(0, len(self.contents))
                drawn.append(self.contents.pop(index))
            except ValueError:
                pass
        return drawn


def experiment(
    hat: Hat,
    expected_balls: dict,
    num_balls_drawn: int,
    num_experiments: int,
) -> float:
    print(f"{hat.actual_balls=}")
    print(f"{expected_balls=}")
    print(f"{num_balls_drawn=}")
    print(f"{num_experiments=}")
    count = 0
    for xp in range(num_experiments):
        this_hat = copy.deepcopy(hat)
        drawn = this_hat.draw(num_balls_drawn)
        for k, v in expected_balls.items():
            if drawn.count(k) < v:
                break
        else:
            count += 1
        pass
    print(str(count / num_experiments))
    return count / num_experiments
