#!/usr/bin/env python3
"""Собирает banner.svg из шаблона и chan.png. Зависимостей нет."""
import base64
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent.parent
tpl = (root / "assets" / "banner.template.svg").read_text(encoding="utf-8")
png = (root / "assets" / "chan.png").read_bytes()

if len(png) > 500 * 1024:
    sys.exit("chan.png > 500KB: сожми pngquant'ом или возьми пиксель-арт")

out = tpl.replace("{{CHAN_B64}}", base64.b64encode(png).decode("ascii"))
(root / "assets" / "banner.svg").write_text(out, encoding="utf-8")
print(f"banner.svg: {len(out) // 1024} KiB")
