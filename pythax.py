import threading
import pymem
from tkinter import *
import numpy as np


class offsets:
    OFFSET_DXRENDERER = (0x142738080)
    OFFSET_GAMERENDERER = (0x142672378)
    OFFSET_ANGLES = (0x1423b2ec0)
    OFFSET_MAIN = (0x142364b78)
    OFFSET_WORLDRENDERSETTINGS = (0x1426724a0)
    OFFSET_BORDERINPUTNODE = (0x142671fb0)
    OFFSET_WEAPON = (0x0)
    OFFSET_SOLDIER_JD62 = (0x142679340)
    OFFSET_DXDISPLAYSETTINGS = (0x142364c70)
    OFFSET_FLAG = (0x142385a98)
    OFFSET_SSMODULE = (0x14273d6e8)
    OFFSET_CONSOLECOMMANDS = (0x140663a20)
    OFFSET_CLIENTGAMECONTEXT = (0x142670d80)
    OFFSET_PLAYERMANAGER = (0x60)
    OFFSET_LOCALPLAYER = (0x540)
    OFFSET_PLAYERS_ARRAY = (0x548)
    OFFSET_TEAMID = (0x13cc)
    OFFSET_SOLDIER = (0x14d0)
    OFFSET_OCCLUDED = (0x5B1)


class process:
    global battlefield
    battlefield = pymem.Pymem("bf4.exe")

    class game:

        def screen_size(self):
            m_pScreen = battlefield.read_bytes(
                offsets.OFFSET_DXRENDERER + 0x38)

            if not m_pScreen:
                return 0

            sizes = np.empty(2)
            sizes[0] = battlefield.read_int(m_pScreen + 0x58)
            sizes[1] = battlefield.read_int(m_pScreen + 0x5C)

            return sizes

        def game_ctx(self):
            return battlefield.read_bytes(offsets.OFFSET_CLIENTGAMECONTEXT)

        def player_manager(self):
            return battlefield.read_bytes(self.game_ctx() + offsets.OFFSET_PLAYERMANAGER)

        def localplayer(self):
            return battlefield.read_bytes(self.player_manager() + offsets.OFFSET_LOCALPLAYER)

        def players(self):
            return battlefield.read_bytes(self.player_manager() + offsets.OFFSET_PLAYERS_ARRAY)

        def get_entity(self, index):
            return battlefield.read_bytes(self.players() + (index * 0x8))

        def get_soldier(self, entity):
            battlefield.read_bytes(entity + offsets.OFFSET_SOLDIER)

        def get_health(self, entity):
            return battlefield.read_float(battlefield.read_bytes(entity + 0x140) + 0x20)

        def is_visible(self, soldier):
            Occluded = battlefield.read_bool(soldier + offsets.OFFSET_OCCLUDED)
            if not Occluded:
                return True
            else:
                return False

        def get_team(self, entity):
            return battlefield.read_int(entity + offsets.OFFSET_TEAMID)

        def get_position(self, soldier):
            battlefield.read_bytes(battlefield.read_int(soldier + 0x490) + 0x30)



# from this point everything still has to be done

    class anti_cheat:
        class bypass(threading.Thread):

            def __init__(self):
                threading.Thread.__init__ = True

            def run(self):
                print("anticheat bypass running")


class features:

    class aimbot(threading.Thread):

        def __init__(self):
            threading.Thread.__init__ = True

        def run(self):
            print("called aimbot")

    class esp(threading.Thread):

        def __init__(self):
            threading.Thread.__init__ = True

        def run(self):
            print("called esp")

    class recoil(threading.Thread):

        def __init__(self):
            threading.Thread.__init__ = True

        def run(self):
            print("called recoil")

    class minimap(threading.Thread):

        def __init__(self):
            threading.Thread.__init__ = True

        def run(self):
            print("called minimap")

    class spread(threading.Thread):

        def __init__(self):
            threading.Thread.__init__ = True

        def run(self):
            print("called spread")

    class engine_chams(threading.Thread):

        def __init__(self):
            threading.Thread.__init__ = True

        def run(self):
            print("called engine_chams")
