
from libqtile.config import Key
from libqtile.lazy import lazy
import utils.functions as fn

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "wezterm"      # My terminal of choice
primaryBrowser = "firefox"       # My browser of choice
secondaryBrowser = "google-chrome"       # My browser of choice



keys = [

    # NOTE:  The essentials
    Key([mod], "Return", lazy.spawn(myTerm), desc="Terminal"),
    Key([mod], "space", lazy.spawn("rofi -show drun"), desc='Run Launcher'),
    Key([mod, "shift"], "period", lazy.spawn("rofi -modi emoji -show emoji"), desc='Rofi emoji'),
    Key([mod], "b", lazy.spawn(primaryBrowser), desc='Web browser'),
    Key([mod, "shift"], "b", lazy.spawn(secondaryBrowser), desc='Web browser'),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Logout menu"),
    Key([mod, "shift"], "l",lazy.spawn("betterlockscreen -l"), desc="lockscreen"),
    Key([mod], "l",lazy.spawncmd(), desc="Spawn a command using a prompt widget"),


    # NOTE: Movement
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "s", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "t", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "n", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Up", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Down", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "period", lazy.next_screen(),desc='Move focus to next monitor'),
    Key([mod], "comma", lazy.prev_screen(), desc='Move focus to prev monitor'),

    Key([mod, "shift"], "space", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # NOTE: Tab
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab"),

    Key([mod, "shift"], "s",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab"),

    Key([mod, "shift"], "t",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab"
        ),

    Key([mod, "shift"], "n",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window downup/move up a section in treetab"
        ),


    # NOTE: Treetab prompt
    Key([mod, "shift"], "a", fn.add_treetab_section,
        desc='Prompt to add new section in treetab'),

    Key([mod, "shift"], "d", fn.del_treetab_section,
        desc='Prompt to add new section in treetab'),


    # NOTE: Rezise
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left"),

    Key([mod, "control"], "s", lazy.layout.grow_right(),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the right"),

    Key([mod, "control"], "t", lazy.layout.grow_down(), desc="Grow window down"),

    Key([mod, "control"], "n", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "m", lazy.layout.maximize(),desc='Toggle between min and max sizes'),

    Key([mod], "f", lazy.window.toggle_floating(), desc='toggle floating'),

    Key([mod, "shift"], "f", fn.maximize_by_switching_layout(),
        lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),

    Key([mod, "shift"], "m", fn.minimize_all(),
        desc="Toggle hide/show all windows on current group"),


]
