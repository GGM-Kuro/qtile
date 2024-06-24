from libqtile import layout
from libqtile.config import Match
import utils.colors

# Layouts and layout rules
themeColor  = utils.colors.NordFox


layout_conf = {
    'border_focus': themeColor[8],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.MonadTall(**layout_conf),
    layout.Max(),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    border_focus=themeColor[8],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="dialog"),         # dialog boxes
        Match(wm_class="download"),       # downloads
        Match(wm_class="Emulator"),       # Emulator android
        Match(wm_class="error"),          # error msgs
        Match(wm_class="file_progress"),  # file progress boxes
        Match(wm_class='kdenlive'),       # kdenlive
        Match(wm_class="notification"),   # notifications
        Match(wm_class="ssh-askpass"),    # ssh-askpass
        Match(wm_class="toolbar"),        # toolbars
        Match(wm_class="Yad"),            # yad boxes
        Match(title='Qalculate!'),        # qalculate-gtk


        # NOTE: tkinter windows
        Match(wm_class="tk"),
        Match(wm_class="Tk"),
        Match(wm_class="Toplevel"),

    ]
)

