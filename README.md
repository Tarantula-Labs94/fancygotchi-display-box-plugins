# FancyGotchi Display Box Plugins

Small, beginner-friendly display add-ons for a Pwnagotchi using **FancyGotchi** on a **Display HAT Mini**.

These were made to fill the little empty boxes in a Pip-Boy/FancyGotchi style theme with useful numbers.

## What this adds

| Add-on | What it shows | File |
|---|---|---|
| Handshake Count Box | Small number showing saved handshake files | `plugins/handshake_count_box.py` |
| Lifetime Deauth Count Box | Small number showing total deauth events, saved after reboot | `plugins/deauth_count_box.py` |
| PiSugar2 Placement Notes | Moves the PiSugar2 battery text into a better spot | `docs/pisugar2-placement.md` |

> Use only on networks and devices you own or are authorized to test.

---

## Tested style setup

This repo was built around this kind of setup:

- Raspberry Pi Zero 2 W
- Display HAT Mini
- PiSugar2
- Pwnagotchi / Aluminum Ice style image
- FancyGotchi theme layout

Other layouts may work too, but you may need to change the screen coordinates.

---

## Repo layout

```text
fancygotchi-display-box-plugins/
├── plugins/
│   ├── handshake_count_box.py
│   └── deauth_count_box.py
├── docs/
│   ├── pisugar2-placement.md
│   └── troubleshooting.md
├── README.md
├── LICENSE
└── .gitignore
```

---

# Quick install

## 1. Copy the plugins to your Pwnagotchi

Custom plugins go here on the Pwnagotchi:

```bash
/usr/local/share/pwnagotchi/custom-plugins/
```

From inside this repo folder, copy both plugins:

```bash
sudo cp plugins/handshake_count_box.py /usr/local/share/pwnagotchi/custom-plugins/
sudo cp plugins/deauth_count_box.py /usr/local/share/pwnagotchi/custom-plugins/
```

If you are not cloning this repo directly on the Pwnagotchi, you can also open each file on GitHub, copy the code, and paste it into a new file with `nano`.

---

## 2. Enable the plugins

Open your Pwnagotchi config:

```bash
sudo nano /etc/pwnagotchi/config.toml
```

Add these lines near your other plugin settings:

```toml
main.plugins.handshake_count_box.enabled = true
main.plugins.deauth_count_box.enabled = true
```

Save in nano:

```text
CTRL + O
Enter
CTRL + X
```

---

## 3. Test before restarting

Check the plugin files:

```bash
sudo python3 -m py_compile /usr/local/share/pwnagotchi/custom-plugins/handshake_count_box.py
sudo python3 -m py_compile /usr/local/share/pwnagotchi/custom-plugins/deauth_count_box.py
```

If those commands print nothing, that is good.

Now check your TOML config:

```bash
python3 -c "import toml; toml.load('/etc/pwnagotchi/config.toml'); print('TOML OK')"
```

If it prints this, you are good:

```text
TOML OK
```

Restart Pwnagotchi:

```bash
sudo systemctl restart pwnagotchi
```

---

# Plugin 1: Handshake Count Box

This plugin shows a small number for files inside:

```bash
/root/handshakes
```

It does **not** remove the normal FancyGotchi handshake text. It only adds a tiny number into a theme box.

Default position:

```python
position=(275, 135),
```

---

# Plugin 2: Lifetime Deauth Count Box

This plugin shows a small number for deauth events.

It saves the number here:

```bash
/root/deauth_count.txt
```

That means the number stays after reboot. It keeps counting until you reset it.

Default position:

```python
position=(225, 133),
```

Reset the lifetime count:

```bash
sudo rm /root/deauth_count.txt
sudo systemctl restart pwnagotchi
```

---

# PiSugar2 battery placement

This repo does not replace the PiSugar2 plugin. It only includes notes for moving the PiSugar2 display text.

See:

```text
docs/pisugar2-placement.md
```

Working positions from this setup:

```python
BAT position=(265, 65)
CHG position=(265, 82)
```

---

# How to move the numbers

Each plugin has a line that looks like this:

```python
position=(275, 135),
```

Think of it like this:

```text
position=(left/right, up/down)
```

Usually:

```text
Bigger first number = move right
Smaller first number = move left

Bigger second number = move down
Smaller second number = move up
```

Change the numbers a little at a time, then restart:

```bash
sudo systemctl restart pwnagotchi
```

A small move is usually `2` to `5` numbers.

---

# Working positions from this setup

These are the final positions used for the setup this repo was made from:

```python
PiSugar BAT:      position=(265, 65)
PiSugar CHG:      position=(265, 82)
Handshake Count:  position=(275, 135)
Deauth Count:     position=(225, 133)
```

---

# Troubleshooting

## Check if the plugins copied correctly

```bash
ls -l /usr/local/share/pwnagotchi/custom-plugins/ | grep count_box
```

You should see:

```text
handshake_count_box.py
deauth_count_box.py
```

## Check if the plugins are enabled

```bash
grep -n "handshake_count_box\|deauth_count_box" /etc/pwnagotchi/config.toml
```

You should see:

```toml
main.plugins.handshake_count_box.enabled = true
main.plugins.deauth_count_box.enabled = true
```

## Check recent plugin errors

```bash
sudo journalctl -u pwnagotchi -n 100 --no-pager | grep -i "handshake_count\|deauth_count\|error"
```

## Check Pwnagotchi status

```bash
systemctl status pwnagotchi
```

More help is in:

```text
docs/troubleshooting.md
```

---

# Notes

- The handshake count plugin counts files in `/root/handshakes`.
- The deauth count plugin counts deauth events seen by the plugin after it is installed.
- The deauth count is saved in `/root/deauth_count.txt`.
- If your theme is different, your coordinates may need to change.
- If Pwnagotchi crashes after editing config, test the TOML before rebooting.

---

# Credits

Custom plugin author name used in the plugin files:

```text
TarantulaLabs
```
