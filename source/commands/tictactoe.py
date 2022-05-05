import discord


class TicTacToeButton(discord.ui.Button["TicTacToe"]):
    def __init__(self, CROSS: int, y: int):
        """A label is required, but we don't need one so a zero-width space is used
        The row parameter tells the View which row to place the button under.
        A View can only contain up to 5 rows each row can only have 5 buttons.
        Since a Tic Tac Toe grid is 3X3 that means we have 3 rows and 3 columns
        """
        super().__init__(
            style=discord.ButtonStyle.secondary, label="\u200b", row=y
        )
        self.CROSS = CROSS
        self.y = y

    # This function is called whenever this particular button is pressed
    # This is part of the "meat" of the game logic
    async def callback(self, interaction: discord.Interaction):
        assert self.view is not None
        view: TicTacToe = self.view
        state = view.board[self.y][self.CROSS]
        if state in (view.CROSS, view.CIRCLE):
            return

        if view.current_player == view.CROSS:
            self.style = discord.ButtonStyle.danger
            self.label = "CROSS"
            self.disabled = True
            view.board[self.y][self.CROSS] = view.CROSS
            view.current_player = view.CIRCLE
            content = "It is now CIRCLE's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "CIRCLE"
            self.disabled = True
            view.board[self.y][self.CROSS] = view.CIRCLE
            view.current_player = view.CROSS
            content = "It is now CROSS's turn"

        winner = view.check_board_winner()
        if winner is not None:
            if winner == view.CROSS:
                content = "CROSS won!"
            elif winner == view.CIRCLE:
                content = "CIRCLE won!"
            else:
                content = "It's a TIE!"

            for child in view.children:
                child.disabled = True

            view.stop()

        await interaction.response.edit_message(content=content, view=view)


# This is our actual board View
class TicTacToe(discord.ui.View):
    CROSS = -1
    CIRCLE = 1
    TIE = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.CROSS
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        # Our board is made up of 3 by 3 TicTacToeButtons
        # The TicTacToeButton maintains the callbacks and helps steer
        # the actual game.
        for CROSS in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(CROSS, y))

    # This method checks for the board winner
    # it is used by the TicTacToeButton
    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.CIRCLE
            elif value == -3:
                return self.CROSS

        # Check vertical
        for line in range(3):
            value = (
                self.board[0][line] + self.board[1][line] + self.board[2][line]
            )
            if value == 3:
                return self.CIRCLE
            elif value == -3:
                return self.CROSS

        # Check diagonals
        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.CIRCLE
        elif diag == -3:
            return self.CROSS

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == 3:
            return self.CIRCLE
        elif diag == -3:
            return self.CROSS

        # If we're here, we need to check if a TIE was made
        if all(i != 0 for row in self.board for i in row):
            return self.TIE

        return None
