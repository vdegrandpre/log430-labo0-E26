"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():    
    assert Calculator().addition(2, 3) == 5

def test_subtraction():
    assert Calculator().subtraction(2, 3) == -1
    assert Calculator().subtraction(-2, 3) == -5
    assert Calculator().subtraction(-2, -3) == 1
    assert Calculator().subtraction(0, -3) == 3

def test_mutiplication():
    assert Calculator().multiplication(-1, -1) == 1
    assert Calculator().multiplication(0, 1) == 0
    assert Calculator().multiplication(1, 0) == 0
    assert Calculator().multiplication(2, -3) == -6
    assert Calculator().multiplication(-1, 2) == -2
    assert Calculator().multiplication(12, 12) == 144

def test_division():
    # assert throw division par 0
    assert Calculator().division(6, 3) == 2
    assert Calculator().division(-6, 6) == -1
    assert Calculator().division(6, 5) == 1.2
