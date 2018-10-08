#!/usr/bin/env python
# coding: utf-8

# In[27]:

"""Just tests"""

import pytest
import hangman


@pytest.mark.parametrize("test_input,expected", [
    (hangman.input_check('word', []), False),
    (hangman.input_check('w', []), 'w'),
    (hangman.input_check('W', []), 'w'),
    (hangman.input_check('123', []), False),
])
def test_input_check(test_input, expected):
    """Test the validator"""
    assert test_input == expected


@pytest.mark.parametrize("test_input,exp", [
    (hangman.try_guess('w', ['*'], 'w'), (['w'], True)),
    (hangman.try_guess('w', ['*', '*'], 'ww'), (['w', 'w'], True)),
    (hangman.try_guess('g', ['*'], 'w'), (['*'], False))
])
def test_try_guess(test_input, exp):
    """Test the core func"""
    assert test_input == exp
