"""
MKV Tags Package

This package provides classes for managing Matroska video file tags:
- BaseTags: Abstract base class with common tag functionality
- MovieTags: Specialized class for movie tag management
- EpisodeTags: Specialized class for TV episode tag management

Features:
- Matroska-compliant XML generation
- Tag extraction and manipulation
- Type-specific tag structures
- XML utilities for Matroska tag structure
"""

from .base_tags import BaseTags
from .episodes import EpisodeTags
from .movies import MovieTags

__all__ = ["BaseTags", "MovieTags", "EpisodeTags"]
