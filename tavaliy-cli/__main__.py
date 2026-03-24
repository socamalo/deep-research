"""
Entry point for uvx execution.
Allows running the MCP server via: uvx -m local-tavily
"""

import importlib.util
import os
import sys

# Load the module from main.py
module_path = os.path.join(os.path.dirname(__file__), "main.py")
spec = importlib.util.spec_from_file_location("main", module_path)
main_module = importlib.util.module_from_spec(spec)
sys.modules["main"] = main_module
spec.loader.exec_module(main_module)

if __name__ == "__main__":
    main_module.register_tools(main_module.mcp)
    main_module.mcp.run()
