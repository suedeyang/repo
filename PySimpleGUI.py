import PySimpleGUI as sg
name=sg.popup_get_text('enter your name')
sg.popup_no_buttons('your name is',name)