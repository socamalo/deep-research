"""
Main entry point for backward compatibility.

This module re-exports the main function from local_tavily.server
for backward compatibility with existing usage.

New code should import directly from local_tavily:
    from local_tavily.server import main
    from local_tavily.cli import cli
"""

from local_tavily.server import main, register_tools, mcp
from local_tavily.key_manager import TavilyKeyManager, get_key_manager, key_manager
from local_tavily.utils import normalize_country, COUNTRY_CODE_MAP, VALID_TAVILY_COUNTRIES

__all__ = [
    "main",
    "register_tools",
    "mcp",
    "TavilyKeyManager",
    "get_key_manager",
    "key_manager",
    "normalize_country",
    "COUNTRY_CODE_MAP",
    "VALID_TAVILY_COUNTRIES",
]

if __name__ == "__main__":
    main()
