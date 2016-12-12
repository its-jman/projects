import subprocess
import os
from pymouse import PyMouse
from Xlib import display
from Xlib import X
from Xlib.ext import record
from Xlib.protocol import rq


"""
------------------------------------------------------ACTION METHODS----------------------------------------------------
"""


def press_key(key):
    """
    uses xdotool to simulate pressing a key
    :param key: key name/number
    """
    os.system('xdotool key ' + key)


def move_to_position(coords, relative=True):
    """
    Moves mouse to

    :param coords: [x, y]; positive is down/right
    :param relative: in relation to current mouse position, or location on screen
    :return:
    """
    if relative:
        old_coords = get_position()
        coords = [coords[0] + old_coords[0], coords[1] + old_coords[1]]
    my_mouse.move(*coords)


def click_mouse(button=1):
    """

    :param button: button to click, 1: left, 3: right
    :return:
    """
    os.system("xdotool click " + str(button))


"""
---------------------------------------------------END ACTION METHODS---------------------------------------------------
"""


"""
---------------------------------------------------------GLOBAL VARS----------------------------------------------------
"""


my_mouse = PyMouse()


# PKing buttons
buttons = {
    # '`'
    49: [press_key, 'F1'],
    # '1'
    10: [press_key, 'F2'],
    # '2'
    11: [press_key, 'F3'],
    # '3'
    12: [press_key, 'F4'],
    # '4'
    13: [press_key, 'F5']
}

"""
------------------------------------------------------END GLOBAL VARS---------------------------------------------------
"""


"""
------------------------------------------------------HELPER METHODS----------------------------------------------------
"""


def get_active_window(cancel_if_not_contained=None):
    """

    :param cancel_if_not_contained: string to look for within title; will cancel if current title does not contain
    :return: False if the "not cancel" string is NOT within title
    """

    proc = subprocess.Popen(["xdotool getwindowfocus getwindowname"], stdout=subprocess.PIPE, shell=True)
    current_window, error = proc.communicate()

    if error:
        print("ERROR: " + error)

    # If there is a "not cancel" string
    if cancel_if_not_contained:
        # Find does not return -1, meaning that the "not cancel" string IS within the window title
        if current_window.find(cancel_if_not_contained) != -1:
            return True
        # "not cancel" is NOT within the title
        else:
            return False
    # If there is not a "not cancel" string
    else:
        return current_window


def get_position():
    """
    gets my_mouse's position
    :return: my_mouse.position()
    """
    return my_mouse.position()


def run_action(key_number):
    """
    Run the command tied to in the dict with the provided argument

    :param key_number: key number, already in buttons
    :return: if it is not in buttons, will return False
    """

    # TODO: Error handling if the data in buttons is not in [function, param] form
    # Provided parameter
    buttons_param = buttons[key_number][1]
    # Runs the function within buttons, with the provided paramater
    buttons[key_number][0](buttons_param)


"""
---------------------------------------------------END HELPER METHODS---------------------------------------------------
"""


"""
--------------------------------------------REQUIREMENTS FOR KEY HANDLING-----------------------------------------------
Adapted from original post: http://pastebin.com/DwSyYTYn
"""


disp = display.Display()
root = disp.screen().root


def handler(reply):
    """ This function is called when a xlib event is fired """
    data = reply.data
    while len(data):
        event, data = rq.EventField(None).parse_binary_value(data, disp.display, None, None)

        if event.type == X.KeyPress:
            key_number = event.detail

            if key_number in buttons:
                if get_active_window(cancel_if_not_contained="OSBuddy"):
                    run_action(key_number)
                else:
                    print("OSBuddy not active, action cancelled.")
            else:
                print("No event, not in buttons.")


ctx = disp.record_create_context(
    0,
    [
        record.AllClients
    ],
    [
        {
            'core_requests': (0, 0),
            'core_replies': (0, 0),
            'ext_requests': (0, 0, 0, 0),
            'ext_replies': (0, 0, 0, 0),
            'delivered_events': (0, 0),
            'device_events': (X.KeyReleaseMask, X.ButtonReleaseMask),
            'errors': (0, 0),
            'client_started': False,
            'client_died': False,
        }
    ]
)


disp.record_enable_context(ctx, handler)
disp.record_free_context(ctx)


while True:
    current_event = root.display.next_event()


"""
----------------------------------------END REQUIREMENTS FOR KEY HANDLING-----------------------------------------------
"""
