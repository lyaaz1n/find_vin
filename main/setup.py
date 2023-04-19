# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 13:27:26 2022

@author: a.lyzin
"""

from cx_Freeze import setup, Executable

executables = [Executable('example.py')]

setup(name='hello_world',
      version='0.0.1',
      description='My Hello World App!',
      executables=executables)