from flask import render_template
from . import main

@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function that handles the 404 file not found error

    Args:
        error
    '''
    return render_template('fourOwfour.html'),404
    