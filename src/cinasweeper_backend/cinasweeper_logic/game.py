from dataclasses import dataclass
from typing import TYPE_CHECKING
import datetime

if TYPE_CHECKING:
    from .database import Database
    from .user import User
    from .gamestate import GameState
    from .gamemode import GameMode
    from .move import Move

@dataclass
class Game:
    id: str
    owner: User | None
    started: bool
    started_time: datetime.datetime
    game_mode: GameMode
    database: Database
    score: int

    @property
    def state(self) -> GameState:
        return self.database.get_game_state(self.id)

    def play_move(self, move: Move) -> GameState:
        # Adds more exception raises depending on the gamemode
        #save to database
        pass

    def claim(self, user: User) -> None:
        """при відсутності гравця присвоїти собі гру"""
        if self.owner is None:
            self.owner = user
        self.database.save_game(self)