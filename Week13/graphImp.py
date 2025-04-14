# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 16:06:09 2025

@author: hkg
"""


# Adjacency List
AL = {
    "0": ["1", "4"],
    "1": ["0", "2", "4"],
    "2": ["1", "4", "3"],
    "3": ["2"],
    "4": ["0", "1", "2"]
}

# Adjacency Matrix
AM = {
    "0": {"0": False, "1": True, "2": False, "3": False, "4": True},
    "1": {"0": True, "1": False, "2": True, "3": False, "4": True},
    "2": {"0": False, "1": True, "2": False, "3": True, "4": True},
    "3": {"0": False, "1": False, "2": True, "3": False, "4": False},
    "4": {"0": True, "1": True, "2": True, "3": False, "4": False}

}

#################### FROM NOTES

# Adjacency List
AL = {
    "a": ["b", "c"],
    "b": ["c", "d", "a"],
    "c": ["b", "a", "d"],
    "d": ["c", "b"]
}

# Adjacency Matrix
AM = {
    "a": {"a": False, "b": True, "c": True, "d": False},
    "b": {"a": True, "b": False, "c": True, "d": True},
    "c": {"a": True, "b": True, "c": False, "d": True},
    "d": {"a": False, "b": True, "c": True, "d": False}
}
