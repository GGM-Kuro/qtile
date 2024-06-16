from libqtile.config import Key, Group
from libqtile.lazy import lazy
from .keybindings import mod,keys


groups = [Group(i) for i in [
    "5", "1", "2", "3", "4",
]]

groups.append(
    Group(
        name="6",
        layout="monadtall",
        label="",
        spawn="obsidian",

    )
)

for group in groups:
    keys.extend([
        # Switch to workspace N
        Key([mod], group.name, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name))
    ])

