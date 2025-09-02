from game.sound import load, play, pause
from game.image import open, change, close
from game.level import start, load as load_level, over


load.load_sound()
play.play_sound()
pause.pause_sound()

open.open_image()
change.change_image()
close.close_image()

start.start_level()
load_level.load_level()
over.game_over()


