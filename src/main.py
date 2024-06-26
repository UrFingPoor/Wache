import keyboard
from Engine.overlay import Overlay_menu

current_window = "VRChat" 
class Main():

    def __init__(self) -> None:
        self.status = True
        self.imgui_menu = Overlay_menu(current_window)
        self.main()

    def main(self):
        keyboard.add_hotkey("INSERT", self.menu_status_change)
        while True:
            self.imgui_menu.update_overlay_menu(self.status)

    def menu_status_change(self):
        self.status = not self.status

if __name__ == "__main__":
    Main()