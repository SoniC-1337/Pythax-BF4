import threading
import pymem
from tkinter import *
import numpy as np
import asyncio
import sys




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

    class game:

        def __init__(self):
            self.battlefield = pymem.Pymem("bf4.exe")

        def screen_size(self):
            m_pScreen = self.battlefield.read_int(
                offsets.OFFSET_DXRENDERER + 0x38)

            if not m_pScreen:
                return 0

            sizes = np.empty(2)
            sizes[0] = self.battlefield.read_int(m_pScreen + 0x58)
            sizes[1] = self.battlefield.read_int(m_pScreen + 0x5C)

            return sizes

        def game_ctx(self):
            return self.battlefield.read_int(offsets.OFFSET_CLIENTGAMECONTEXT)

        def player_manager(self):
            return self.battlefield.read_int(self.game_ctx() + offsets.OFFSET_PLAYERMANAGER)

        def localplayer(self):
            return self.battlefield.read_int(self.player_manager() + offsets.OFFSET_LOCALPLAYER)

        def players(self):
            return self.battlefield.read_int(self.player_manager() + offsets.OFFSET_PLAYERS_ARRAY)

        def get_entity(self, index):
            return self.battlefield.read_int(self.players() + (index * 0x8))

        def get_soldier(self, entity):
            self.battlefield.read_int(entity + offsets.OFFSET_SOLDIER)

        def get_health(self, entity):
            return self.battlefield.read_float(self.battlefield.read_int(entity + 0x140) + 0x20)

        def is_visible(self, soldier):
            Occluded = self.battlefield.read_bool(
                soldier + offsets.OFFSET_OCCLUDED)
            if not Occluded:
                return True
            else:
                return False

        def get_team(self, entity):
            return self.battlefield.read_int(entity + offsets.OFFSET_TEAMID)

        def get_position(self, soldier):
            self.battlefield.read_int(
                self.battlefield.read_int(soldier + 0x490) + 0x30)


# from this point everything still has to be done


    class anti_cheat:
        class bypass(threading.Thread):

            def __init__(self):
                threading.Thread.__init__(self)

            def run(self):
                print("anticheat bypass running")


class features:

    class aimbot(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.run()

        def run(self):
            print("called aimbot")

    class esp(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.run()

        def run(self):
            print("called esp")

    class recoil(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.run()

        def run(self):
            print("called recoil")

    class minimap(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.run()

        def run(self):
            print("called minimap")

    class spread(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.run()

        def run(self):
            print("called spread")

    class engine_chams(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.run()

        def run(self):
            print("called engine_chams")


class Pythax():

    @staticmethod
    async def winmain():
        try:
            BF4 = process()
            G = BF4.game()
    
            print("game base address : {}".format(hex(G.battlefield.base_address)))
            print("game context : {}".format(hex(G.game_ctx())))
            print("player manager : {}".format(hex(G.player_manager())))

            # throws error when trying to get player array, prob reading wrong type
            print("player array : {}".format(hex(G.players())))

            class THREADS:
                @classmethod
                def call_hacks(self):
                    features.aimbot().start()
                    features.esp().start()
                    features.recoil().start()
                    features.minimap().start()
                    features.spread().start()
                    features.engine_chams().start()

                def __init__(self):
                    self.call_hacks()


            THREADS()

            while True:
                for i in range(70):
                    entity = G.get_entity(i)
                    print(str(G.get_health(entity))+str(i))
    
    
        except Exception as e:
            print(e)

    
    def __init__(self):
        asyncio.run(self.winmain())


if __name__ == '__main__':
    Pythax()
