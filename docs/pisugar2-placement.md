# PiSugar2 Battery Placement Fix

This note is for FancyGotchi users who already have the PiSugar2 plugin working, but the battery text is printing in the wrong spot.

This was made around a Display HAT Mini layout.

---

## What this fixes

The PiSugar2 plugin may print battery text across the top of the screen.

This guide moves it into a cleaner FancyGotchi theme box.

---

## 1. Enable PiSugar2

Open your config:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Enable the plugin:

```toml
main.plugins.pisugar2.enabled = true
```

Recommended while testing:

```toml
# main.plugins.pisugar2.shutdown = 5
# main.plugins.pisugar2.sync_rtc_on_boot = true
```

Save:

```text
CTRL + O
Enter
CTRL + X
```

---

## 2. Important config note

Only use one active `main.custom_plugins` line.

Good:

```toml
main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"
```

If you also have this active:

```toml
main.custom_plugins = "/usr/local/share/pwnagotchi/installed-plugins/"
```

comment one of them out. Duplicate keys can crash Pwnagotchi.

---

## 3. Copy the PiSugar2 plugin if needed

If `pisugar2.py` exists in installed plugins but not custom plugins:

```bash
sudo cp /usr/local/share/pwnagotchi/installed-plugins/pisugar2.py /usr/local/share/pwnagotchi/custom-plugins/
```

Check:

```bash
ls -l /usr/local/share/pwnagotchi/custom-plugins/ | grep pisugar
```

---

## 4. Edit battery placement

Open the plugin:

```bash
sudo nano /usr/local/share/pwnagotchi/custom-plugins/pisugar2.py
```

Find the battery display section.

The original positions may look like this:

```python
position=(ui.width() / 2 + 15, 0),
```

and:

```python
position=(ui.width() / 2 - 12, 0),
```

Change them to:

```python
position=(265, 65),
```

and:

```python
position=(265, 82),
```

Example:

```python
        ui.add_element(
            "bat",
            LabeledValue(
                color=BLACK,
                label="BAT",
                value="0%",
                position=(265, 65),
                label_font=fonts.Bold,
                text_font=fonts.Medium,
            ),
        )
        # display charging status
        if self.is_new_model:
            ui.add_element(
                "chg",
                LabeledValue(
                    color=BLACK,
                    label="",
                    value="",
                    position=(265, 82),
                    label_font=fonts.Bold,
                    text_font=fonts.Bold,
                ),
            )
```

Save:

```text
CTRL + O
Enter
CTRL + X
```

Restart:

```bash
sudo systemctl restart pwnagotchi
```

---

## Moving the battery text

The format is:

```python
position=(x, y),
```

Usually:

```text
Bigger x = right
Smaller x = left

Bigger y = down
Smaller y = up
```

Make small changes and restart after each change.
