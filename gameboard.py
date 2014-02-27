from math import copysign
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, ListProperty
            
class CoinSlots(Widget):
    pass

class Character(Widget):
    
    def on_pos(self, instance, value):
        board = instance.parent
        
        for baddie in board.baddies:
            if instance.collide_widget(baddie):
                self.fail
                return
        
        grid = board.grid

        for cell in grid:
            if instance.collide_point(*cell.center):
                instance.whatever(cell)
                return

class GameBoard(Widget):
    grid = ObjectProperty(None)
    baddies = ListProperty([])
    man = ObjectProperty(None)

    def sign(self, n):
        return copysign(1, n)
        
    def on_grid(self, instance, grid):
        if grid:
            total = grid.rows * grid.cols
            
            for x in xrange(total):
                grid.add_widget(CoinSlots())

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            touch.grab(self)
            return True
        else:
            return False

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            directions = (touch.dx, touch.dy)
            _max = max(directions, key=abs)

            if abs(_max) > 10:
                ix = directions.index(_max)
                b = [self.sign(x) if x==_max else 0 for x in directions]
                
                if b[0] == b[1]:
                    b = [b[0], 0]
