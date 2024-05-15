import subprocess
from libqtile import qtile
from libqtile.lazy import lazy
from settings.globals import *

# Allows you to input a name when adding treetab section.


@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)


@lazy.layout.function
def del_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_del_section)

# A function for hide/show all the windows in a group


@lazy.function
def minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()


# A function for toggling between MAX and MONADTALL layouts


@lazy.function
def maximize_by_switching_layout(qtile):
    current_layout_name = qtile.current_group.layout.name
    if current_layout_name == 'monadtall':
        qtile.current_group.layout = 'max'
    elif current_layout_name == 'max':
        qtile.current_group.layout = 'monadtall'


def vpn_status():
    process = subprocess.Popen(
        [f'{SCRIPTS_PATH}/vpn_status'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    output = output.decode().strip()
    return output


def victim_target():
    process = subprocess.Popen(
        [f'{SCRIPTS_PATH}/target_to_hack'], stdout=subprocess.PIPE)
    output, _ = process.communicate()
    output = output.decode().strip()
    return output
