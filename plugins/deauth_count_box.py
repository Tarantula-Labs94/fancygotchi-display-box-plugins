import logging
import os

import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.view import BLACK


# Change position=(x, y) below to move the number on screen.
# x = left/right, y = up/down.
# The lifetime count is saved at /root/deauth_count.txt.

class DeauthCountBox(plugins.Plugin):
    __author__ = "TarantulaLabs"
    __version__ = "1.1.0"
    __license__ = "GPL3"
    __description__ = "Shows lifetime deauth count as a small number in a theme box."

    def on_loaded(self):
        self.count_file = "/root/deauth_count.txt"
        self.count = 0

        try:
            if os.path.exists(self.count_file):
                with open(self.count_file, "r") as f:
                    self.count = int(f.read().strip() or 0)
        except Exception as e:
            logging.error("[deauth_count_box] could not read count file: %s" % e)
            self.count = 0

        logging.info("[deauth_count_box] plugin loaded with count %s" % self.count)

    def save_count(self):
        try:
            with open(self.count_file, "w") as f:
                f.write(str(self.count))
        except Exception as e:
            logging.error("[deauth_count_box] could not save count: %s" % e)

    def on_ui_setup(self, ui):
        ui.add_element(
            "deauth_count_box",
            LabeledValue(
                color=BLACK,
                label="",
                value=str(self.count),
                position=(225, 133),
                label_font=fonts.Bold,
                text_font=fonts.Bold,
            ),
        )

    def on_deauthentication(self, agent, access_point, client_station):
        self.count += 1
        self.save_count()

    def on_ui_update(self, ui):
        try:
            ui.set("deauth_count_box", str(self.count))
        except Exception as e:
            logging.error("[deauth_count_box] error: %s" % e)
            ui.set("deauth_count_box", "?")

    def on_unload(self, ui):
        self.save_count()
        with ui._lock:
            ui.remove_element("deauth_count_box")
