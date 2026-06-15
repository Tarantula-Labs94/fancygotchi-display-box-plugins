import os
import glob
import logging

import pwnagotchi.plugins as plugins
from pwnagotchi.ui.components import LabeledValue
import pwnagotchi.ui.fonts as fonts
from pwnagotchi.ui.view import BLACK


# Change position=(x, y) below to move the number on screen.
# x = left/right, y = up/down.

class HandshakeCountBox(plugins.Plugin):
    __author__ = "TarantulaLabs"
    __version__ = "1.0.0"
    __license__ = "GPL3"
    __description__ = "Shows handshake count as a small number in a theme box."

    def on_loaded(self):
        logging.info("[handshake_count_box] plugin loaded")

    def on_ui_setup(self, ui):
        ui.add_element(
            "handshake_count_box",
            LabeledValue(
                color=BLACK,
                label="",
                value="0",
                position=(275, 135),
                label_font=fonts.Bold,
                text_font=fonts.Bold,
            ),
        )

    def on_ui_update(self, ui):
        try:
            handshakes_dir = "/root/handshakes"
            files = glob.glob(os.path.join(handshakes_dir, "*"))
            count = len(files)
            ui.set("handshake_count_box", str(count))
        except Exception as e:
            logging.error("[handshake_count_box] error: %s" % e)
            ui.set("handshake_count_box", "?")

    def on_unload(self, ui):
        with ui._lock:
            ui.remove_element("handshake_count_box")
