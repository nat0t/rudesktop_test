from config.config import FIELD_COLOR


def invert_color(x: int, y: int, field: dict[(int, int), str]) -> dict[(int, int), str]:
    """Invert color of cell with provided coordinates."""
    color = field.get((x, y), FIELD_COLOR)
    field[(x, y)] = 'white' if color == 'black' else 'black'
    return field


def change_direction_white(direction: str) -> str:
    """Change direction of ant if his cell is white."""
    selector = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    return selector[direction]


def change_direction_black(direction: str) -> str:
    """Change direction of ant if his cell is black."""
    selector = {'up': 'left', 'right': 'up', 'down': 'right', 'left': 'down'}
    return selector[direction]


def change_direction(direction: str, color: str) -> str:
    """Change direction of ant depends on cell color."""
    return change_direction_white(direction) if color == 'white' else change_direction_black(direction)


def move_white(x: int, y: int, direction: str) -> tuple[int, int, str]:
    """Make ant move if his cell is white."""
    selector = {
        'up': (x + 1, y),
        'right': (x, y - 1),
        'down': (x - 1, y),
        'left': (x, y + 1),
    }
    return *selector[direction], change_direction(direction, 'white')


def move_black(x: int, y: int, direction: str) -> tuple[int, int, str]:
    """Make ant move if his cell is black."""
    selector = {
        'up': (x - 1, y),
        'right': (x, y + 1),
        'down': (x + 1, y),
        'left': (x, y - 1),
    }
    return *selector[direction], change_direction(direction, 'black')


def move(x: int, y: int, direction: str, field: dict[tuple[int, int], str]) -> tuple[int, int, str, dict]:
    """Make ant move."""
    color = field.get((x, y), FIELD_COLOR)
    field = invert_color(x, y, field)
    if color == 'white':
        return *move_white(x, y, direction), field
    elif color == 'black':
        return *move_black(x, y, direction), field
