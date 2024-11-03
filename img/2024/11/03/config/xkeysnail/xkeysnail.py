# -*- coding: utf-8 -*-

from __future__ import barry_as_FLUFL
import re
from xkeysnail.transform import *

# Use the following for testing terminal keymaps
# terminals = [ "", ... ]
# xbindkeys -mk
terminals = [
    "gnome-terminal",
    "terminator",
    "konsole",
    "io.elementary.terminal",
    "tabby",
    "sakura",
    "guake",
    "tilda",
    "xterm",
    "eterm",
    "kitty",
    "alacritty",
    "mate-terminal",
    "tilix",
    "xfce4-terminal",
]

mscodes = ["code", "vscodium"]
codeStr = "|".join(str(x) for x in mscodes)


browsers = ["Firefox", "Google-chrome"]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str(x) for x in terminals)
browsers = [term.casefold() for term in browsers]
# define timeout for multipurpose_modmap
define_timeout(1)

# define_conditional_modmap(
#    lambda wm_class: wm_class.casefold() in browsers,
#    {
#        Key.LEFT_META: Key.LEFT_CTRL,
#    },
# )
# [Global modemap] Change modifier keys as in xmodmap
define_modmap(
    {
        Key.CAPSLOCK: Key.LEFT_CTRL,
        Key.RIGHT_SHIFT: Key.CAPSLOCK,
        Key.LEFT_META: Key.LEFT_ALT,
        Key.LEFT_ALT: Key.LEFT_META,
    }
)

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(
    re.compile(r"Emacs"),
    {
        Key.RIGHT_CTRL: Key.ESC,
    },
)

# [Multipurpose modmap] Give a key two meanings. A normal key when pressed and
# released, and a modifier key when held down with another key. See Xcape,
# Carabiner and caps2esc for ideas and concept.
# define_multipurpose_modmap(
# Enter is enter when pressed and released. Control when held down.
# {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}

# Capslock is escape when pressed and released. Control when held down.
# {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]
# To use this example, you can't remap capslock with define_modmap.
# )

# [Conditional multipurpose modmap] Multipurpose modmap in certain conditions,
# such as for a particular device.
# define_conditional_multipurpose_modmap(lambda wm_class, device_name: device_name.startswith("Microsoft"), {
# Left shift is open paren when pressed and released.
# Left shift when held down.
# Key.LEFT_SHIFT: [Key.KPLEFTPAREN, Key.LEFT_SHIFT],

# Right shift is close paren when pressed and released.
# Right shift when held down.
# Key.RIGHT_SHIFT: [Key.KPRIGHTPAREN, Key.RIGHT_SHIFT]
# })


# Keybindings for Firefox/Chrome
define_keymap(
    re.compile("Firefox|Google-chrome"),
    {
        # Ctrl+Alt+j/k to switch next/previous tab
        K("LWin-Shift-RIGHT_BRACE"): K("C-TAB"),
        K("LWin-Shift-LEFT_BRACE"): K("C-Shift-TAB"),
        K("LWin-RIGHT_BRACE"): K("LM-RIGHT"),
        K("LWin-LEFT_BRACE"): K("LM-LEFT"),
        K("LWin-L"): K("C-L"),
        # Type C-j to focus to the content
        K("C-j"): K("C-f6"),
        # very naive "Edit in editor" feature (just an example)
        #K("C-o"): [launch(["code"])],
    },
    "Firefox and Chrome",
)

# Keybindings for Firefox/Chrome
define_keymap(
    re.compile("X-terminal-emulator"),
    {
        K("LWin-Shift-LEFT_BRACE"): K("C-page_up"),
        K("LWin-Shift-RIGHT_BRACE"): K("C-page_down"),

    },
    "Firefox and Chrome",
)

jetbrains = ["jetbrains-idea"]
jetbrains = [term.casefold() for term in jetbrains]
define_keymap(
    #  clambda wm_class: wm_class not in ("IntelliJ IDEA"),
    lambda wm_class: wm_class.casefold() not in (jetbrains+terminals),
    {
        K("RC-KEY_1"): K("F1"),
        K("RC-KEY_2"): K("F2"),
        K("RC-KEY_3"): K("F4"),
        K("RC-KEY_4"): K("F4"),
        K("RC-KEY_5"): K("F5"),
        K("RC-KEY_6"): K("F6"),
        K("RC-KEY_7"): K("F7"),
        K("RC-KEY_8"): K("F8"),
        K("RC-KEY_9"): K("F9"),
        K("RC-KEY_0"): K("F10"),
             
        K("LWin-KEY_1"): K("LC-KEY_1"),
        K("LWin-KEY_2"): K("LC-KEY_2"),
        K("LWin-KEY_3"): K("LC-KEY_3"),
        K("LWin-KEY_4"): K("LC-KEY_4"),
        K("LWin-KEY_5"): K("LC-KEY_5"),
        K("LWin-KEY_6"): K("LC-KEY_6"),
        K("LWin-KEY_7"): K("LC-KEY_7"),
        K("LWin-KEY_8"): K("LC-KEY_8"),
        K("LWin-KEY_9"): K("LC-KEY_9"),
        K("LWin-KEY_0"): K("LC-KEY_0"),

        K("RC-MINUS"): K("F11"),
        K("RC-EQUAL"): K("F12"),
        # Ctrl+Alt+j/k to switch next/previous tab
        K("LWin-A"): K("C-a"),
        K("LWin-N"): K("C-N"),
        K("LWin-Shift-N"): K("C-Shift-N"),
        K("LWin-C"): K("C-c"),
        K("LWin-S"): K("C-s"),
        K("LWin-f"): K("C-f"),
        K("LWin-w"): K("C-w"),
        K("LWin-Shift-w"): K("C-Shift-w"),
        K("LWin-Q"): K("C-q"),
        K("LWin-t"): K("C-t"),
        K("LWin-Shift-t"): K("C-Shift-t"),
        K("LWin-X"): K("C-x"),
        K("LWin-Z"): K("C-z"),
        K("LWin-Shift-T"): K("C-Shift-t"),
        K("LWin-Shift-C"): K("C-Shift-c"),
        K("LWin-Shift-V"): K("C-Shift-V"),
        K("LWin-LC-C"): K("C-M-c"),
        K("LWin-LC-V"): K("C-M-v"),
        K("LWin-Shift-LEFT_BRACE"): K("LC-tab"),
        K("LWin-Shift-RIGHT_BRACE"): K("LC-Shift-tab"),

        K("LWin-V"): K("C-V"),
        K("LWin-Shift-V"): K("C-Shift-v"),
    },
    "IntelliJ-like keys",
)
# Keybindings for Zeal https://github.com/zealdocs/zeal/
define_keymap(
    re.compile("Zeal"),
    {
        # Ctrl+s to focus search area
        K("C-s"): K("C-k"),
    },
    "Zeal",
)

# Emacs-like keybindings in non-Emacs applications
define_keymap(
    lambda wm_class: wm_class not in ("Emacs", "URxvt", "X-terminal-emulator","tabby"),
    {
        # Cursor
        K("C-b"): with_mark(K("left")),
        K("C-f"): with_mark(K("right")),
        K("C-p"): with_mark(K("up")),
        K("C-n"): with_mark(K("down")),
        K("C-h"): with_mark(K("backspace")),
        # Forward/Backward word
        # K("M-b"): with_mark(K("C-left")),
        # K("M-f"): with_mark(K("C-right")),
        # Beginning/End of line
        K("C-a"): with_mark(K("home")),
        K("C-e"): with_mark(K("end")),
        # Page up/down
        # K("M-v"): with_mark(K("page_up")),
        # K("C-v"): with_mark(K("page_down")),
        # Beginning/End of file
        # K("M-Shift-comma"): with_mark(K("C-home")),
        # K("M-Shift-dot"): with_mark(K("C-end")),
        # Newline
        # K("C-m"): K("enter"),
        # K("C-j"): K("enter"),
        # K("C-o"): [K("enter"), K("left")],
        # Copy
        # K("C-w"): [K("C-x"), set_mark(False)],
        # K("M-w"): [K("C-c"), set_mark(False)],
        # K("C-y"): [K("C-v"), set_mark(False)],
        # Delete
        K("C-d"): [K("delete"), set_mark(False)],
        # K("M-d"): [K("C-delete"), set_mark(False)],
        # Kill line
        K("C-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
        # Undo
        K("C-slash"): [K("C-z"), set_mark(False)],
        K("C-Shift-ro"): K("C-z"),
        # Mark
        # K("C-space"): set_mark(True),
        # K("C-M-space"): with_or_set_mark(K("C-right")),
        # Search
        # K("C-s"): K("F3"),
        # K("C-r"): K("Shift-F3"),
        # K("M-Shift-key_5"): K("C-h"),
        # Cancel
        # K("C-g"): [K("esc"), set_mark(False)],
        # Escape
        K("C-q"): escape_next_key,
        # C-x YYY
        K("C-x"): {
            # C-x h (select all)
            K("h"): [K("C-home"), K("C-a"), set_mark(True)],
            # C-x C-f (open)
            K("C-f"): K("C-o"),
            # C-x C-s (save)
            K("C-s"): K("C-s"),
            # C-x k (kill tab)
            K("k"): K("C-f4"),
            # C-x C-c (exit)
            K("C-c"): K("C-q"),
            # cancel
            K("C-g"): pass_through_key,
            # C-x u (undo)
            K("u"): [K("C-z"), set_mark(False)],
        },
    },
    "Emacs-like keys",
)


define_keymap(
    re.compile(codeStr, re.IGNORECASE),
    {
        # Wordwise remaining - for VS Code
        # Alt-F19 hack fixes Alt menu activation
        K("M-Left"): [K("M-F19"), K("C-Left")],  # Left of Word
        K("M-Right"): [K("M-F19"), K("C-Right")],  # Right of Word
        K("M-Shift-Left"): [K("M-F19"), K("C-Shift-Left")],  # Select Left of Word
        K("M-Shift-Right"): [K("M-F19"), K("C-Shift-Right")],  # Select Right of Word
        # K("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
        # K("C-PAGE_UP"): pass_through_key,           # cancel prev_view
        K("C-M-Left"): K("C-PAGE_UP"),  # next_view
        K("C-M-Right"): K("C-PAGE_DOWN"),  # prev_view
        # VS Code Shortcuts
        K("C-g"): pass_through_key,  # cancel Go to Line...
        K("Super-g"): K("C-g"),  # Go to Line...
        K("F3"): pass_through_key,  # cancel Find next
        K("C-h"): pass_through_key,  # cancel replace
        K("C-M-f"): K("C-h"),  # replace
        K("C-Shift-h"): pass_through_key,  # cancel replace_next
        K("C-M-e"): K("C-Shift-h"),  # replace_next
        K("f3"): pass_through_key,  # cancel find_next
        K("C-g"): K("f3"),  # find_next
        K("Shift-f3"): pass_through_key,  # cancel find_prev
        K("C-Shift-g"): K("Shift-f3"),  # find_prev
        # K("Super-C-g"): K("C-f2"),                  # Default - Sublime - find_all_under
        # K("C-M-g"): K("C-f2"),                      # Chromebook - Sublime - find_all_under
        # K("Super-Shift-up"): K("M-Shift-up"),       # multi-cursor up - Sublime
        # K("Super-Shift-down"): K("M-Shift-down"),   # multi-cursor down - Sublime
        # K(""): pass_through_key,                    # cancel
        # K(""): K(""),                               #
    },
    "Code",
)

define_keymap(
    re.compile("org.gnome.nautilus", re.IGNORECASE),
    {
        K("LWin-Up"): K("M-Up"),  # Go Up dir
        K("LWin-Down"): K("M-Down"),  # Go Down dir
        K("LWin-Left"): K("M-Left"),  # Go Back
        K("LWin-Right"): K("M-Right"),  # Go Forward
        K("ENTER"): K("f2"),  # Go Forward
        K("LC-ENTER"): K("ENTER"),  # Go Forward
    },
)

import os

os.system("/usr/bin/setxkbmap -option altwin:meta_win")
