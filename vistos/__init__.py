#!python3.8
"""vistos (V)"""
from vistos.src import Congress, CongressMember, search_congress_members, gpo

__all__ = ['gpo', 'Congress', 'CongressMember', 'search_congress_members']

VERSION = str(open('./VERSION', 'r').read())
