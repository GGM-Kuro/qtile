import os
import subprocess
import utils.functions as fn
from libqtile import bar, hook, qtile, widget

from libqtile.config import Click, Drag, Screen, Match
from libqtile.lazy import lazy
# Make sure 'qtile-extras' is installed or this config will not work.
from qtile_extras import widget
from qtile_extras.widget.groupbox2 import GroupBoxRule, ScreenRule
# import qtile_extras
from qtile_extras.widget.decorations import BorderDecoration,RectDecoration
import utils.colors
from settings.keybindings import *
from settings.globals import *
from settings.groups import *
from settings.layouts import layouts,floating_layout

from libqtile.log_utils import logger


@hook.subscribe.startup_once
def autostart():
    logger.warning("In autostart")
    home = os.path.join(os.path.expanduser('~'), ".config", "qtile")
    subprocess.call([os.path.join(home, 'autostart.sh')])


theme_colors = utils.colors.NordFox


widget_defaults = dict(
    font="Fira Code Bold",
    fontshadow='#000000ee',
    fontsize=16,
)


default_decorations = {
    "radius":10,
    "filled":True,
    "padding_y":5,
}


def default_decor(colour=theme_colors[8]):

    default={
        "decorations": [
    BorderDecoration(
        colour=theme_colors[2],
        border_width=[0, 0,12, 0],
    ),
    BorderDecoration(
        colour=colour,
        border_width=[0, 0, 4, 0],
    ),
    RectDecoration(
        radius=10,
        filled=True,
        padding_y=5,
        colour=theme_colors[2],
    ),
    ]
    }

    return default

def init_widgets_list():
    widgets_list = [
        widget.Spacer(length=8),
        widget.Image(
            filename="/home/kuro/Desktop/kuro/Icons/Monkey",
            scale="False",
            length=38,
            margin_x=5,
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(myTerm)},
        ),
        widget.Prompt(
            foreground=theme_colors[1]
        ),
        widget.Spacer(length=8),
        widget.CurrentLayoutIcon(

            foreground=theme_colors[1],

            padding=10,
            width=100,
            scale=0.6,
            **default_decor(theme_colors[1]),
        ),
        widget.Spacer(length=8),
        widget.GenPollCommand(
            fontsize=16,
            update_interval=300,
            cmd=f'{SCRIPTS_PATH}/ethernet_status',
            foreground=theme_colors[8],
            # backgrgound=theme_colors[2],
            padding=12,
            fmt='󰈀 Local: {}',
            **default_decor(),
        ),
        widget.Spacer(length=8),
        widget.GenPollText(
            update_interval=15,
            func=fn.vpn_status,
            foreground=theme_colors[3] if "vpn off" in fn.vpn_status(
            ) else theme_colors[1],
            fmt='{}',
            padding=12,
            **default_decor(theme_colors[3] if "vpn off" in fn.vpn_status(
            ) else theme_colors[1]),
        ),
        widget.Spacer(length=8),
        widget.GenPollText(
            padding=12,
            width = bar.CALCULATED if "󰯐" in fn.victim_target(
                    ) else 0,
            update_interval=100,
            func=fn.victim_target,
            foreground=theme_colors[4]if "󰯐" in fn.victim_target(
                    ) else theme_colors[0],
            fmt='{}',
            decorations=[
                RectDecoration(
                    **default_decorations,
                    colour=theme_colors[2] if "󰯐" in fn.victim_target(
                    ) else theme_colors[0],
                    line_width=2,
                    line_colour=theme_colors[4],
                ),

            ],
        ),
        widget.Spacer(
            length=bar.STRETCH,
        ),
        widget.Spacer(
            length=bar.STRETCH,
        ),       widget.GroupBox2(
            padding=10,
            margin=50,
            decorations=[
                RectDecoration(
                    line_colour="#eeeeee",
                    line_width=2,
                    colour="#222222",
                    radius=10,
                    filled=True,
                    padding_y=5,
                    padding_x=3
                ),
            ],
            rounded= True,
            fontsize=25,
            rules=[
                GroupBoxRule(box_size=50).when(),
                GroupBoxRule(text='󰮊', text_colour="#71627a").when( group_name="6", focused=True),
                GroupBoxRule(text_colour=str(theme_colors[3][0])).when( screen=ScreenRule.OTHER, occupied=True),
                GroupBoxRule(text_colour=str( theme_colors[5][0])).when(occupied=True),
                GroupBoxRule(text='󰮯').when(focused=True),
                GroupBoxRule(text='󰊠').when( screen=ScreenRule.OTHER, focused=False),
                GroupBoxRule(text='󰊠').when( screen=ScreenRule.THIS, focused=False),
                GroupBoxRule(text='').when(occupied=True, urgent=True),
                GroupBoxRule(text='').when(),
            ],
        ),
        widget.Spacer(
            length=bar.STRETCH,
            padding=40,
        ),       widget.Spacer(
            length=bar.STRETCH,
        ),
        widget.WindowName(
            foreground=theme_colors[6],
            scroll=True,
            scroll_repeat=0.5,
            scroll_delay=2,
            width=100,
            **default_decor(),
        ),
        widget.Spacer(length=8),
        widget.GenPollText(
            update_interval=300,
            scroll=True,
            scroll_repeat=0.5,
            scroll_delay=2,
            width=100,
            func=lambda: subprocess.check_output(
                "printf $(uname -r)", shell=True, text=True),
            foreground=theme_colors[3],
            fmt='❤ {}',
            **default_decor(theme_colors[3])
        ),
        widget.Spacer(length=8),
        widget.KeyboardLayout(
            foreground=theme_colors[4],
            configured_keyboards=['us','latam'],
            fmt='⌨ Kbd: {}',
            padding=10,
            **default_decor(theme_colors[4]),
        ),
        widget.Spacer(length=8),
        widget.Clock(
            foreground=theme_colors[5],
            format=" %a,%b %d  %H:%M",
            **default_decor(theme_colors[5]),
        ),
        widget.Spacer(length=8),
        widget.GenPollCommand(
            fontsize=14,
            update_interval=10,
            cmd=f"{SCRIPTS_PATH}/battery_status",
            foreground=theme_colors[6],
            opacity=0,
            padding=12,
            **default_decor(theme_colors[6]),
        ),
        widget.Systray(
            icon_size=20,
            margin=100,
            # foreground=theme_colors[6],
            decorations=[
                BorderDecoration(
                    colour=theme_colors[16],
                    border_width=[0, 0, 4, 0],
                ),
            ],
            # background=theme_colors[6],


        ),
        widget.Spacer(length=20),

    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


def init_widgets_screen2():
    widgets_screen2 = [
        widget.Spacer(length=bar.STRETCH),
        init_widgets_screen1()[13],
        widget.Spacer(lengRh=bar.STRETCH),
        init_widgets_screen1()[3]
    ]

    return widgets_screen2


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=49, opacity=1, margin=2, padding=20, background=theme_colors[0])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=49, background= theme_colors[0])),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=26))]

def init_fake_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=49, opacity=1, margin=2, padding=20, background=theme_colors[0]),width=1920,height=1080,x=0,y=0),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=49, background= theme_colors[0]),width=1280,height=720,x=1920,y=0),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=49, background= theme_colors[0]),width=1280,height=720,x=3200,y=0),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=49, background= theme_colors[0]),width=1280,height=720,x=1920,y=720),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=49, background= theme_colors[0]),width=1280,height=720,x=3200,y=720),
            ]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    # fake_screens = init_fake_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

auto_fullscreen = True
focus_on_window_activation = "urgent"
reconfigure_screens = True
bring_front_click = False
cursor_warp = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
