# Troubleshooting Guide

This page is for common problems when adding the display box plugins.

---

## 1. Test `config.toml`

Run this after editing `/etc/pwnagotchi/config.toml`:

```bash
python3 -c "import toml; toml.load('/etc/pwnagotchi/config.toml'); print('TOML OK')"
```

Good output:

```text
TOML OK
```

If it shows an error, fix the config before restarting Pwnagotchi.

---

## 2. Check if Pwnagotchi is running

```bash
systemctl status pwnagotchi
```

Restart Pwnagotchi:

```bash
sudo systemctl restart pwnagotchi
```

Stop it while troubleshooting:

```bash
sudo systemctl stop pwnagotchi
```

Run debug mode:

```bash
sudo pwnagotchi --debug
```

---

## 3. Check recent logs

```bash
sudo journalctl -u pwnagotchi -n 100 --no-pager
```

Show only plugin-related messages:

```bash
sudo journalctl -u pwnagotchi -n 100 --no-pager | grep -i "pisugar\|handshake_count\|deauth_count\|error"
```

---

## 4. Check if the plugins exist

```bash
ls -l /usr/local/share/pwnagotchi/custom-plugins/
```

Only show these plugins:

```bash
ls -l /usr/local/share/pwnagotchi/custom-plugins/ | grep count_box
```

Expected files:

```text
handshake_count_box.py
deauth_count_box.py
```

---

## 5. Check if the plugins are enabled

```bash
grep -n "pisugar2\|handshake_count_box\|deauth_count_box" /etc/pwnagotchi/config.toml
```

Expected lines:

```toml
main.plugins.pisugar2.enabled = true
main.plugins.handshake_count_box.enabled = true
main.plugins.deauth_count_box.enabled = true
```

You only need the `pisugar2` line if you are using the PiSugar2 battery plugin.

---

## 6. Test plugin syntax

Handshake plugin:

```bash
sudo python3 -m py_compile /usr/local/share/pwnagotchi/custom-plugins/handshake_count_box.py
```

Deauth plugin:

```bash
sudo python3 -m py_compile /usr/local/share/pwnagotchi/custom-plugins/deauth_count_box.py
```

If the command prints nothing, the file is usually okay.

---

## 7. Reset lifetime deauth count

```bash
sudo rm /root/deauth_count.txt
sudo systemctl restart pwnagotchi
```

The count will start back at zero.

---

## 8. Duplicate `main.custom_plugins` error

If TOML says `Duplicate keys`, check for duplicate plugin path lines:

```bash
sudo nl -ba /etc/pwnagotchi/config.toml | grep "main.custom_plugins"
```

Good:

```toml
main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"
```

Bad if both are active:

```toml
main.custom_plugins = "/usr/local/share/pwnagotchi/custom-plugins/"
main.custom_plugins = "/usr/local/share/pwnagotchi/installed-plugins/"
```

Comment one out with `#`.

---

## 9. Text is in the wrong spot

Open the plugin you want to move:

```bash
sudo nano /usr/local/share/pwnagotchi/custom-plugins/handshake_count_box.py
```

or:

```bash
sudo nano /usr/local/share/pwnagotchi/custom-plugins/deauth_count_box.py
```

Find:

```python
position=(275, 135),
```

Rule of thumb:

```text
Bigger first number = right
Smaller first number = left

Bigger second number = down
Smaller second number = up
```

Change by small amounts, save, and restart:

```bash
sudo systemctl restart pwnagotchi
```
