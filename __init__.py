"""
MKV Files - A Python library for working with MKV files and tags using MKVToolNix.

This package provides tools for:
- Extracting and manipulating MKV file tags
- Working with Matroska metadata
- Movie and TV episode tag management and XML generation
"""

__version__ = "1.0.0"
__author__ = "Your Name"

# Make main classes available at package level
from .mkvpy import MKVToolNix

# New media tags system
from .mkvpy.Tags import BaseTags, EpisodeTags, MovieTags

__all__ = [
    "MKVToolNix",
    "BaseTags",
    "MovieTags",
    "EpisodeTags",
]
