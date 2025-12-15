test_rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
assert_positions = [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
assert_cnt = 3


def test_solution():
    init_position = 50
    cnt_of_zero = 0
    for rotation in test_rotations:
        direction, steps = rotation[0], int(rotation[1:]) % 100
        if direction == "L":
            if init_position < steps:
                init_position = 100 + init_position - steps
            else:
                init_position -= steps
        elif direction == "R":
            init_position = (init_position + steps) % 100

        assert init_position == assert_positions.pop(0)

        if init_position == 0:
            cnt_of_zero += 1

    assert cnt_of_zero == assert_cnt


def solution(rotations) -> int:
    init_position = 50
    cnt_of_zero = 0
    for rotation in rotations:
        direction, steps = rotation[0], int(rotation[1:]) % 100
        if direction == "L":
            if init_position < steps:
                init_position = 100 + init_position - steps
            else:
                init_position -= steps
        elif direction == "R":
            init_position = (init_position + steps) % 100

        if init_position == 0:
            cnt_of_zero += 1

    return cnt_of_zero


if __name__ == "__main__":
    # test_solution()
    with open("./day1/input.txt", "r") as f:
        rotations = f.read().splitlines()
    print(solution(rotations))
