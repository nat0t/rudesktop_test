from config.config import FIELD_WIDTH, FIELD_HEIGHT, FIELD_COLOR, ANT_START_DIRECTION, ANT_START_X, ANT_START_Y
from services.field import is_exit, draw_field
from services.move import move

if __name__ == '__main__':
    coordinates = ANT_START_X, ANT_START_Y
    color = FIELD_COLOR
    direction = ANT_START_DIRECTION
    field = {(x, y): FIELD_COLOR for y in range(FIELD_HEIGHT) for x in range(FIELD_WIDTH)}
    field.update({coordinates: color})

    while 1:
        *coordinates, direction, field = move(*coordinates, direction, field)
        if is_exit(FIELD_WIDTH, FIELD_HEIGHT, *coordinates):
            break
    draw_field(field)
