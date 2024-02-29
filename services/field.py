from itertools import groupby
import png

from config.config import FIELD_WIDTH, FIELD_HEIGHT, OUTPUT_FILENAME


def is_exit(field_width: int, field_height: int, x: int, y: int) -> bool:
    """Check if ant has reached the edge of field."""
    result = False
    if x in (0, FIELD_WIDTH) or y in (0, FIELD_HEIGHT):
        result = True
    return result


def draw_field(field: dict[(int, int), str]) -> None:
    """Create png-file with ant path."""
    png_list: list = []
    for key, group in groupby(field.keys(), lambda c: c[1]):
        png_row: list = []
        for coordinate in group:
            if field[coordinate] == 'white':
                png_row.append(255)
            else:
                png_row.append(0)
        png_list.insert(0, png_row)
    png.from_array(png_list, 'L').save(OUTPUT_FILENAME)
