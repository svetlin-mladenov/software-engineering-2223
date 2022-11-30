import re
from typing import Any

# not enum is intentional
class Colours:
    def __init__(self):
        self.BLUE_FG = '\033[94m'
        self.CYAN_FG = '\033[96m'
        self.DARKCYAN_FG = '\033[96m'
        self.GREEN_FG = '\033[92m'
        self.PURPLE_FG = '\033[95m'
        self.RED_FG = '\033[91m'
        self.YELLOW_FG = '\033[93m'
        self.WHITE_FG = '\033[37m'
        self.CYAN_FG = '\033[36m'
        self.BLACK_FG = '\033[30m'
        self.GRAY_BG = '\033[100m'
        self.BLACK_BG = '\033[40m'
        self.GREEN_BG = '\033[102m'
        self.BROWN_BG= '\033[43m'

        self.BOLD = '\033[1m'
        self.FAINT = '\033[2m'
        self.END = '\033[0m'  
        self.UNDERLINE = '\033[4m'
    # TODO 8 bit support and rgb converter


class Style:
    def __init__(self, theme=None):

        self.border_dict = {
            "border_top_left":'╔',
            "border_top_right":'╗',
            "border_bottom_left":'╚',
            "border_bottom_right": '╝',
            "border_line_horizontal": '═',
            "border_line_vertical":'║',
            "border_connector_top":'╤',
            "border_connector_right":'╢',
            "border_connector_left":'╟',
            "border_connector_bottom":'╧',
            "line_connector":'┼',
            "line_vertical":'│',
            "line_horizontal":'─'
        }

        # border pieces
        self.border_top_left = '╔'
        self.border_top_right = '╗'
        self.border_bottom_left = '╚'
        self.border_bottom_right = '╝'
        self.border_line_horizontal = '═'
        self.border_line_vertical = '║'
        self.border_connector_top = '╤'
        self.border_connector_right = '╢'
        self.border_connector_left = '╟'
        self.border_connector_bottom = '╧'

        # within board
        self.line_connector = '┼'
        self.line_vertical = '│'
        self.line_horizontal = '─'

    def is_border(self, char: str) -> bool:
        for border in self.border_dict.keys():
            if char in self.border_dict[border]:
                return True

        return False

    def convert_line_to_border(self, char: str, side: str, corner=None) -> str:
        """
        Convert a char (part of cell line) into a char (cell border)
        Doesnt deal with corner cases

        side arg: "top" "bottom" "right" "left"
        corner arg: "left, right"
        """

        if char == self.line_horizontal:  # convert to vertical border
            return  self.border_line_horizontal

        elif char == self.line_vertical:  # convert to horizontal border
            return self.border_line_vertical
            
        else:  # connector and edge cases
            if side == 'top':
                if corner is None:
                    return self.border_connector_top
                elif corner == "left":
                    return self.border_top_left
                elif corner == "right":
                    return self.border_top_right      

            elif side == 'bottom':
                if corner == "left":
                    return self.border_bottom_left
                elif corner == "right":
                    return self.border_bottom_right
                else:
                    return self.border_connector_bottom

            elif side == 'right':
                return self.border_connector_right

            elif side == 'left':
                return self.border_connector_left
            else:
                return  # TODO raise error here


class Cell:
    def __init__(self, row: int, column: int, value=' '):
        self.style = Style()  # TODO: implement different styles
        self.row = row
        self.column = column
        self.value = value
        self.value_colour = None
        self.is_highlighted = False
        self.colour = None
        self.outlook = []

    def colour_value(self, colour: str) -> None:
        """Adds ansii that highlights the cells value and keeps border highlight"""
        # add cell value colour
        self.value_colour = colour

        if self.value_colour is not None:
            self.outlook = [line.replace(" " + self.value + " ", self.value_colour + " " + self.value + " " + Colour.END) for line in self.outlook]

    def _rm_invalid_borders(self) -> None:
        """invalid borders are ones that make the table have double borders when printing"""
        if self.row != 0:
            self._rm_top_border()
        if self.column != 0:
            self._rm_left_border()

    def _rm_top_border(self) -> None:
        self.outlook.pop(0)

    def _rm_left_border(self) -> None:
        for i in range(len(self.outlook)):
            self.outlook[i] = self.outlook[i][1:]

    def _add_cell_frame(self, max_row: int, max_column: int, style: Style) -> None:
        """Adds a frame(outer border for the table) to the cell."""
    
        # get edge
        if self.column == 0:  
            edge = "left"
        elif self.column == max_column:
            edge = "right"
        else:
            edge = None


        # change vertical lines into border
        for i in range(len(self.outlook)):
                
            if edge == "left":
                self.outlook[i] = replace_str_in_str(self.outlook[i], 
                    style.convert_line_to_border(self.outlook[i][0], edge),
                    0,
                    1,
                )
            elif edge == "right":
                self.outlook[i] = replace_str_in_str(self.outlook[i], 
                    style.convert_line_to_border(self.outlook[i][-1], edge),
                    -1,
                    -1,
                )
                self.outlook[i] = self.outlook[i][:-1]  # remove trash remaining char


        # for horizontal lines top/bottom
        if self.row == 0 or self.row == max_row:

            if self.row == 0:
                side = "top"
                line_index = 0  # index where the horizontal lines are
            else:
                side = "bottom"
                line_index = -1  # index where the horizontal lines are

            new_border = ""

            # for each char in line
            for char in self.outlook[line_index]:

                if len(new_border) == 0 or self.column == max_column:  # for corner pieces. check for new_border len if its left edge because else it makes 2 corner pieces when it should 1
                    new_border += style.convert_line_to_border(char, side, edge)
                else:
                    new_border += style.convert_line_to_border(char, side)

            self.outlook[line_index] = new_border


        return
            # for each char in the top 



class Table:
    def __init__(self, rows=0, columns=0, style=Style()):

        self.rows = rows
        self.columns = columns
        self.matrix = [ [Cell(row, column,' ') for column in range(0, columns)] for row in range(0, rows) ]
        self.style = style
        self.colours = Colours()

        self.column_width = []
        for column in range(columns):
            self.column_width.append(0)

        self.row_height = []
        for row in range(rows):
            self.row_height.append(0)
        self.add_lines()

    def add_lines(self) -> None:
        """Create a border for every cell"""
        for row in self.matrix:
            for cell in row:
                cell = self._add_cell_border(cell)
          
    def print(self) -> None:
        """Prints table"""
        table_str = ""

        # iterate rows
        for rowNum, row in enumerate(self.matrix):

            # iterate lines in the row (cell border consists of multiple lines, iterate top->bottom)
            for line in range(0, self.row_height[rowNum]+2):

                if line == self.row_height[rowNum]+1 and rowNum != 0: # works only for top elements
                    break

                # iterate over every cell in row
                for cell in row:
                    try:
                        # add a line of the cells border to the table string
                        table_str += cell.outlook[line]
                    except IndexError:
                        # this shouldnt be reachable, added only for debug visualisation
                        break
                table_str += '\n'

        print(table_str)

    def _add_cell_border(self, cell: Cell, verify=False) -> Cell:
        """
        Adds a border to a cell. The border has a different size depending on the cells value.

        'verify' arg updates cells affected by the border change.
        """

        cell.outlook = []  # Remove existing border.
        cell_value_width, separated_values = longest_str_len_before_substr(cell.value, '\n')  # get value width(char amount before '\n') and a list of each line(if '\n' present)


        verify_row = False  # used for updating other rows borders
        verify_column = False  # used for updating other columns borders

        # check if cell border exceeds column width
        if cell_value_width > self.column_width[cell.column]:
            self.column_width[cell.column] = cell_value_width  # update column width

            # update cell borders in the affected column
            if verify:  
                verify_column = True


        # create a str containing a horizontal line for the border top and bottom
        horizontal_lines = self.column_width[cell.column]*self.style.line_horizontal + 2*self.style.line_horizontal

        # Add the borders top
        cell.outlook.append(
            self.style.line_connector + 
            horizontal_lines +
            self.style.line_connector
        )

        # Add all the middle lines in the border (ones with vertical border frame)

        cell_value_height = len(separated_values)  # get cell value height

        # check if current cell value is taller(\n amount) than the other cell in its row
        if cell_value_height > self.row_height[cell.row]:
            self.row_height[cell.row] = cell_value_height  # update row height

            # update cell borders in the affected row
            if verify:
                verify_row = True

        # iterate over each line of value (lines are separated by \n)
        for i in range(0, self.row_height[cell.row]):

            half_1 = self.style.line_vertical + ' '  # add first half of the line (same in all cell borders)

            # try to add cells value if there is one (if updating a cells border, it could be missing value height)
            try:
                half_1 += separated_values[i]
            except IndexError:
                pass

            required_spaces = " "  # spaces required to add for the borders to link

            # add the required spaces
            for i in range(self.column_width[cell.column] - len(half_1) + 2):
                required_spaces += " "

            # add the line to cell border
            cell.outlook.append(
                half_1 +
                required_spaces +
                self.style.line_vertical
            )

        # add last line
        cell.outlook.append(
            self.style.line_connector + 
            horizontal_lines +
            self.style.line_connector
        )

        # remove unnecessary borders based on the cells position in the matrix
        cell._rm_invalid_borders()
        cell._add_cell_frame(self.rows-1, self.columns-1, self.style)

        # update rows and columns that need to update their border
        if verify_row:
            self.verify_row(cell.row)
        if verify_column:
            self.verify_column(cell.column)


        return cell

    def add_cell_value(self, row: int, column: int, value: Any) -> None:
        """Changes the cells value and updates its border"""

        # create new cell
        cell = self.matrix[row][column]
        cell.value = value
        cell = self._add_cell_border(cell, verify=True)

    def get_cell_value(self, row: int, column: int) -> Any:
        """ Get the values of a cell with coordinates """
        return self.matrix[row][column].value


    def verify_row(self, row: int) -> None:
        """Updates border for all cells in a column"""

        # iterate over rows
        for column in range(0, self.columns):

            # add new border
            cell = self.matrix[row][column]
            self._add_cell_border(cell)

    def verify_column(self, column: int) -> None:
        """Updates border for all cells in a row."""

        # iterate over columns
        for row in range(0, self.rows):

            # add new border
            cell = self.matrix[row][column]
            self._add_cell_border(cell)

    def highlight_cell(self, row: int, column: int, colour: str) -> None:
        """Highlights the border around the selected cell. Overwrites existing highlighted cell borders"""

        cell = self.matrix[row][column]

        if colour == '':
            cell.is_highlighted = False
        else:
            cell.is_highlighted = True

        # highlight borders of current cell
        for i in range(0, len(cell.outlook)):
            # if i == len(cell.outlook) - 1 and row != self.rows-1 and self.matrix[row-1][column].is_highlighted == True:
            #     break 
            cell.outlook[i] = colour + remove_ansi(cell.outlook[i]) + self.colours.END

        # try to highlight rightmost chars of left cell
        if cell.column > 0:
            left_cell = self.matrix[row][column-1]
            for i in range(0, len(left_cell.outlook)):
                left_cell.outlook[i] = remove_ansi(left_cell.outlook[i])
                left_cell.outlook[i] = replace_str_in_str(left_cell.outlook[i], colour, -1, -1) + self.colours.END

        # try to highlight bottomost chars of top cell
        if cell.row > 0:
            top_cell = self.matrix[row-1][column]
            top_cell.outlook[-1] = remove_ansi(top_cell.outlook[-1])
            top_cell.outlook[-1] = colour + top_cell.outlook[-1] + self.colours.END

        # try to highlight bottomost rightmost char of top left cell (corner)
        if cell.row > 0 and cell.column > 0:
            top_left_cell = self.matrix[row-1][column-1]
            top_left_cell.outlook[-1] = remove_ansi(top_left_cell.outlook[-1])
            top_left_cell.outlook[-1] = top_left_cell.outlook[-1][:-1] + colour + top_left_cell.outlook[-1][-1] + self.colours.END

    def unhighlight_cell(self, row: int, column: int) -> None:
        """Unhighlights highlighted cells. Slightly faster than calling highlight_cell() with empty colour string """

        cell = self.matrix[row][column]

        if cell.is_highlighted == False:
            return

        cell.is_highlighted = False

        # unhighlight borders of current cell
        for i in range(0, len(cell.outlook)):
            cell.outlook[i] = remove_ansi(cell.outlook[i])

        # unhighlight rightmost chars of left cell
        if cell.column > 0:
            left_cell = self.matrix[row][column-1]
            for i in range(0, len(left_cell.outlook)):
                left_cell.outlook[i] = remove_ansi(left_cell.outlook[i])

        # unhighlight bottomost chars of top cell
        if cell.row > 0:
            top_cell = self.matrix[row-1][column]
            top_cell.outlook[-1] = remove_ansi(top_cell.outlook[-1])

        # unhighlight bottomost rightmost char of top left cell (corner)
        if cell.row > 0 and cell.column > 0:
            top_left_cell = self.matrix[row-1][column-1]
            top_left_cell.outlook[-1] = remove_ansi(top_left_cell.outlook[-1])



def longest_str_len_before_substr(string: str, substring: str) -> tuple[int, list[str]]:
    """Splits a string by substring and determines the length of the longest split string."""

    separated_strings = string.split(substring)  # serparate string by substring
    max_len = 0

    # determine longest separated string
    for string in separated_strings:
        if max_len < len(string):
            max_len = len(string)

    return max_len, separated_strings


def replace_str_in_str(string: str, substring: str, indexA: int, indexB: int) -> str:
    """Replaces a string in a string with a different string. indexA - indexB is the range in which the str should be replaced."""

    return string[:indexA] + substring + string[indexB:]


def remove_ansi(string: str) -> str:
    """Removes all ansi characters from string"""

    ansi_escape = re.compile(r'''
        \x1B  # ESC
        (?:   # 7-bit C1 Fe (except CSI)
            [@-Z\\-_]
        |     # or [ for CSI, followed by a control sequence
            \[
            [0-?]*  # Parameter bytes
            [ -/]*  # Intermediate bytes
            [@-~]   # Final byte
        )
    ''', re.VERBOSE)

    return ansi_escape.sub('', string)


Colour = Colours()
if __name__ == "__main__":
    table = Table(4, 6)
    table.highlight_cell(3,3, Colour.GREEN_FG)
    table.highlight_cell(2,3, Colour.RED_FG + Colour.BOLD)
    table.print()


# TODO add cell value highlight and make it unaffected by highlight, unhighlight. Essentially when unhighlighting, do as usual and add cell colour at the end
#TODO change border highlight to not affect the cell value: ex: colour | value | endColour to colour | endColour value colour | endColour
# main challange would be deteting where the value starts or ends
# TODO un/highlight row/column
# TODO cell value padding (already have function in main.py)
# TODO add_column/row method (isnt necessary for project)
