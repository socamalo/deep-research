"""
Comprehensive unit tests for main.py
"""
import asyncio
import os
import unittest
from datetime import datetime
from unittest.mock import AsyncMock, MagicMock, Mock, patch, call
from functools import partial

import pytest


def create_mock_mcp():
    """Create a mock MCP instance with tool() decorator that works correctly."""
    mock_mcp = MagicMock()
    
    def tool_decorator(func):
        # Call tool() again with the function to simulate FastMCP's behavior
        mock_mcp.tool(func)
        return func
    
    # Make tool() return the decorator when called with no args
    mock_mcp.tool.return_value = tool_decorator
    
    return mock_mcp


class TestTavilyKeyManager(unittest.TestCase):
    """Test cases for TavilyKeyManager class"""

    def setUp(self):
        """Set up test fixtures"""
        self.test_keys = ["key1", "key2", "key3"]

    def test_init_with_keys(self):
        """Test initialization with provided keys"""
        from main import TavilyKeyManager

        manager = TavilyKeyManager(keys=self.test_keys)
        self.assertEqual(manager.keys, self.test_keys)
        self.assertEqual(manager.days_per_key, 11)  # ceil(31/3) = 11

    @patch("main.os.getenv")
    def test_init_load_from_env(self, mock_getenv):
        """Test initialization by loading keys from environment"""
        from main import TavilyKeyManager

        mock_getenv.side_effect = lambda x: {
            "TAVILY_API_KEY_1": "env_key1",
            "TAVILY_API_KEY_2": "env_key2",
            "TAVILY_API_KEY_3": None,  # Stop loading here
        }.get(x)

        manager = TavilyKeyManager()
        self.assertEqual(len(manager.keys), 2)
        self.assertEqual(manager.keys[0], "env_key1")
        self.assertEqual(manager.keys[1], "env_key2")

    @patch("main.os.getenv")
    def test_init_no_keys_raises_error(self, mock_getenv):
        """Test that initialization without keys raises ValueError"""
        from main import TavilyKeyManager

        mock_getenv.return_value = None

        with self.assertRaises(ValueError) as context:
            TavilyKeyManager()

        self.assertIn("No Tavily API keys found", str(context.exception))

    def test_api_key_rotation_day_1(self):
        """Test API key selection for day 1"""
        from main import TavilyKeyManager

        manager = TavilyKeyManager(keys=self.test_keys)
        # days_per_key = 11, so day 1 should use key 0
        with patch("main.datetime") as mock_datetime:
            mock_now = MagicMock()
            mock_now.day = 1
            mock_datetime.now.return_value = mock_now
            key = manager.api_key
            self.assertEqual(key, "key1")

    def test_api_key_rotation_day_12(self):
        """Test API key selection for day 12 (should use key 1)"""
        from main import TavilyKeyManager

        manager = TavilyKeyManager(keys=self.test_keys)
        # days_per_key = 11, so day 12 should use key 1
        with patch("main.datetime") as mock_datetime:
            mock_now = MagicMock()
            mock_now.day = 12
            mock_datetime.now.return_value = mock_now
            key = manager.api_key
            self.assertEqual(key, "key2")

    def test_api_key_rotation_day_31(self):
        """Test API key selection for day 31 (should use last key)"""
        from main import TavilyKeyManager

        manager = TavilyKeyManager(keys=self.test_keys)
        # days_per_key = 11, so day 31 should use key 2 (last key)
        with patch("main.datetime") as mock_datetime:
            mock_now = MagicMock()
            mock_now.day = 31
            mock_datetime.now.return_value = mock_now
            key = manager.api_key
            self.assertEqual(key, "key3")

    def test_api_key_rotation_single_key(self):
        """Test API key rotation with single key"""
        from main import TavilyKeyManager

        manager = TavilyKeyManager(keys=["single_key"])
        self.assertEqual(manager.days_per_key, 31)

        with patch("main.datetime") as mock_datetime:
            mock_now = MagicMock()
            mock_now.day = 15
            mock_datetime.now.return_value = mock_now
            key = manager.api_key
            self.assertEqual(key, "single_key")

    def test_api_key_rotation_multiple_keys(self):
        """Test API key rotation with 5 keys"""
        from main import TavilyKeyManager

        keys = ["key1", "key2", "key3", "key4", "key5"]
        manager = TavilyKeyManager(keys=keys)
        self.assertEqual(manager.days_per_key, 7)  # ceil(31/5) = 7

        # Day 1-7 should use key1
        with patch("main.datetime") as mock_datetime:
            mock_now = MagicMock()
            mock_now.day = 5
            mock_datetime.now.return_value = mock_now
            self.assertEqual(manager.api_key, "key1")

        # Day 8-14 should use key2
        with patch("main.datetime") as mock_datetime:
            mock_now = MagicMock()
            mock_now.day = 10
            mock_datetime.now.return_value = mock_now
            self.assertEqual(manager.api_key, "key2")

    def test_load_keys_from_env_sequential(self):
        """Test loading keys sequentially from environment"""
        from main import TavilyKeyManager

        manager = TavilyKeyManager(keys=self.test_keys)
        
        with patch("main.os.getenv") as mock_getenv:
            mock_getenv.side_effect = lambda x: {
                "TAVILY_API_KEY_1": "key1",
                "TAVILY_API_KEY_2": "key2",
                "TAVILY_API_KEY_3": "key3",
                "TAVILY_API_KEY_4": None,
            }.get(x)
            
            keys = manager._load_keys_from_env()
            self.assertEqual(keys, ["key1", "key2", "key3"])


class TestNormalizeCountry(unittest.TestCase):
    """Test cases for normalize_country function"""

    def test_normalize_country_none(self):
        """Test normalize_country with None"""
        from main import normalize_country

        result = normalize_country(None)
        self.assertIsNone(result)

    def test_normalize_country_empty_string(self):
        """Test normalize_country with empty string"""
        from main import normalize_country

        result = normalize_country("")
        self.assertIsNone(result)

    def test_normalize_country_valid_full_name(self):
        """Test normalize_country with valid full country name"""
        from main import normalize_country

        result = normalize_country("united states")
        self.assertEqual(result, "united states")

    def test_normalize_country_valid_iso_code(self):
        """Test normalize_country with valid ISO code"""
        from main import normalize_country

        result = normalize_country("us")
        self.assertEqual(result, "united states")

    def test_normalize_country_valid_iso_code_uppercase(self):
        """Test normalize_country with uppercase ISO code"""
        from main import normalize_country

        result = normalize_country("US")
        self.assertEqual(result, "united states")

    def test_normalize_country_with_periods(self):
        """Test normalize_country with periods in abbreviation"""
        from main import normalize_country

        result = normalize_country("u.s.")
        self.assertEqual(result, "united states")

    def test_normalize_country_invalid(self):
        """Test normalize_country with invalid country"""
        from main import normalize_country

        with self.assertRaises(ValueError) as context:
            normalize_country("invalid_country")

        self.assertIn("Invalid country", str(context.exception))

    def test_normalize_country_whitespace(self):
        """Test normalize_country with whitespace"""
        from main import normalize_country

        result = normalize_country("  uk  ")
        self.assertEqual(result, "united kingdom")

    def test_normalize_country_multiple_codes(self):
        """Test normalize_country with various country codes"""
        from main import normalize_country

        test_cases = [
            ("cn", "china"),
            ("jp", "japan"),
            ("de", "germany"),
            ("fr", "france"),
            ("gb", "united kingdom"),
            ("ae", "united arab emirates"),
            ("uae", "united arab emirates"),
        ]

        for code, expected in test_cases:
            with self.subTest(code=code):
                result = normalize_country(code)
                self.assertEqual(result, expected)


class TestTavilySearchTool(unittest.TestCase):
    """Test cases for tavily_search tool registration and logic"""

    def setUp(self):
        """Set up test fixtures"""
        self.mock_mcp = create_mock_mcp()
        self.test_query = "test query"

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    @patch("main.asyncio.get_event_loop")
    @patch("main.logger")
    def test_tavily_search_tool_registration(self, mock_logger, mock_loop, mock_client_class, mock_key_manager):
        """Test that tavily_search registers tools correctly"""
        from main import tavily_search

        mock_key_manager.api_key = "test_key"
        tavily_search(self.mock_mcp)

        # Verify that tool was called (registration happened)
        self.assertTrue(self.mock_mcp.tool.called)
        # Should register multiple tools (search, get_status, get_results)
        self.assertGreaterEqual(self.mock_mcp.tool.call_count, 1)

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_search_parameter_validation(self, mock_client_class, mock_key_manager):
        """Test parameter validation in tavily_search"""
        from main import tavily_search

        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        tavily_search(self.mock_mcp)
        
        # Get the first tool function (tavily_search) - it's in call_args_list[1] (second call, first tool)
        tool_func = self.mock_mcp.tool.call_args_list[1][0][0]

        async def test_invalid_chunks():
            result = await tool_func(
                query="test",
                chunks_per_source=5,  # Invalid: should be 1-3
                search_depth="advanced",
                ctx=None,
            )
            return result

        result = asyncio.run(test_invalid_chunks())
        self.assertEqual(result["status"], "error")
        self.assertIn("chunks_per_source", result["message"])

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    @patch("main.asyncio.get_event_loop")
    def test_tavily_search_string_conversion(self, mock_loop, mock_client_class, mock_key_manager):
        """Test string to int conversion for days and timeout"""
        from main import tavily_search

        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_response = {
            "results": [],
            "query": "test",
            "response_time": 0.5,
        }

        loop = MagicMock()
        mock_loop.return_value = loop
        
        async def mock_executor(*args, **kwargs):
            return mock_response
        
        loop.run_in_executor = AsyncMock(side_effect=mock_executor)

        tavily_search(self.mock_mcp)
        # Get the first tool function (tavily_search) - it's in call_args_list[1]
        tool_func = self.mock_mcp.tool.call_args_list[1][0][0]

        async def test_string_params():
            result = await tool_func(
                query="test",
                days="7",
                timeout="30",
                ctx=None,
            )
            return result

        result = asyncio.run(test_string_params())
        self.assertEqual(result["status"], "success")

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_search_country_normalization(self, mock_client_class, mock_key_manager):
        """Test country normalization in search"""
        from main import tavily_search

        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_response = {
            "results": [],
            "query": "test",
            "response_time": 0.5,
        }

        loop = MagicMock()
        loop.run_in_executor = AsyncMock(return_value=mock_response)

        with patch("main.asyncio.get_event_loop", return_value=loop):
            tavily_search(self.mock_mcp)
            # Get the first tool function (tavily_search) - it's in call_args_list[1]
            tool_func = self.mock_mcp.tool.call_args_list[1][0][0]

            async def test_country():
                result = await tool_func(
                    query="test",
                    country="us",
                    topic="general",
                    ctx=None,
                )
                return result

            result = asyncio.run(test_country())
            self.assertEqual(result["status"], "success")

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_search_invalid_country(self, mock_client_class, mock_key_manager):
        """Test search with invalid country"""
        from main import tavily_search

        mock_key_manager.api_key = "test_key"
        tavily_search(self.mock_mcp)
        # Get the first tool function (tavily_search) - it's in call_args_list[1]
        tool_func = self.mock_mcp.tool.call_args_list[1][0][0]

        async def test_invalid_country():
            result = await tool_func(
                query="test",
                country="invalid_country_xyz",
                topic="general",
                ctx=None,
            )
            return result

        result = asyncio.run(test_invalid_country())
        self.assertEqual(result["status"], "error")
        self.assertIn("Invalid country", result["message"])


class TestTavilyExtractTool(unittest.TestCase):
    """Test cases for tavily_extract tool"""

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_extract_single_url(self, mock_client_class, mock_key_manager):
        """Test Tavily extract with single URL"""
        from main import tavily_extract

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_response = {
            "results": [{"url": "https://test.com", "content": "Test content"}],
            "failed_results": [],
            "response_time": 0.5,
            "request_id": "test_id",
        }
        mock_client_instance.extract.return_value = mock_response

        tavily_extract(mock_mcp)
        tool_func = mock_mcp.tool.call_args[0][0]

        result = tool_func(urls="https://test.com")

        self.assertEqual(result["status"], "success")
        self.assertIn("results", result)
        # Verify single URL was converted to list
        call_args = mock_client_instance.extract.call_args
        self.assertIsInstance(call_args[1]["urls"], list)

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_extract_multiple_urls(self, mock_client_class, mock_key_manager):
        """Test Tavily extract with multiple URLs"""
        from main import tavily_extract

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_response = {
            "results": [],
            "failed_results": [],
            "response_time": 0.5,
        }
        mock_client_instance.extract.return_value = mock_response

        tavily_extract(mock_mcp)
        tool_func = mock_mcp.tool.call_args[0][0]

        result = tool_func(urls=["https://test1.com", "https://test2.com"])

        self.assertEqual(result["status"], "success")
        # Verify URLs were passed as list
        call_args = mock_client_instance.extract.call_args
        self.assertIsInstance(call_args[1]["urls"], list)
        self.assertEqual(len(call_args[1]["urls"]), 2)

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_extract_with_timeout(self, mock_client_class, mock_key_manager):
        """Test Tavily extract with timeout parameter"""
        from main import tavily_extract

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_response = {
            "results": [],
            "failed_results": [],
            "response_time": 0.5,
        }
        mock_client_instance.extract.return_value = mock_response

        tavily_extract(mock_mcp)
        tool_func = mock_mcp.tool.call_args[0][0]

        result = tool_func(urls="https://test.com", timeout=30.0)

        self.assertEqual(result["status"], "success")
        # Verify timeout was passed
        call_args = mock_client_instance.extract.call_args
        self.assertEqual(call_args[1]["timeout"], 30.0)

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_extract_error(self, mock_client_class, mock_key_manager):
        """Test Tavily extract with error"""
        from main import tavily_extract

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance
        mock_client_instance.extract.side_effect = Exception("Test error")

        tavily_extract(mock_mcp)
        tool_func = mock_mcp.tool.call_args[0][0]

        result = tool_func(urls="https://test.com")

        self.assertEqual(result["status"], "error")
        self.assertIn("Error during Tavily extract", result["message"])

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_extract_import_error(self, mock_client_class, mock_key_manager):
        """Test Tavily extract with ImportError"""
        from main import tavily_extract

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_class.side_effect = ImportError("Module not found")

        tavily_extract(mock_mcp)
        tool_func = mock_mcp.tool.call_args[0][0]

        result = tool_func(urls="https://test.com")

        self.assertEqual(result["status"], "error")
        self.assertIn("not installed", result["message"])


class TestRegisterTools(unittest.TestCase):
    """Test cases for register_tools function"""

    def test_register_tools(self):
        """Test that register_tools calls all tool registration functions"""
        from main import register_tools

        mock_mcp = create_mock_mcp()

        with patch("main.tavily_search") as mock_tavily_search, patch(
            "main.tavily_extract"
        ) as mock_tavily_extract:
            register_tools(mock_mcp)

            mock_tavily_search.assert_called_once_with(mock_mcp)
            mock_tavily_extract.assert_called_once_with(mock_mcp)


class TestGetWindowsProxyConfig(unittest.TestCase):
    """Test cases for get_windows_proxy_config function"""

    def test_get_windows_proxy_config(self):
        """Test get_windows_proxy_config returns None"""
        from main import get_windows_proxy_config

        result = get_windows_proxy_config()
        self.assertIsNone(result)


class TestTavilyGetSearchStatus(unittest.TestCase):
    """Test cases for tavily_get_search_status function"""

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_get_search_status_success(self, mock_client_class, mock_key_manager):
        """Test successful search status retrieval"""
        from main import tavily_search

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_status = {"status": "completed"}
        mock_client_instance.get_search_status.return_value = mock_status

        tavily_search(mock_mcp)
        # Get the second tool (tavily_get_search_status) - calls 2,3 are for second tool
        tool_func = mock_mcp.tool.call_args_list[3][0][0]

        result = tool_func(query_id="test_query_id")

        self.assertEqual(result["status"], "success")
        self.assertEqual(result["query_id"], "test_query_id")

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_get_search_status_error(self, mock_client_class, mock_key_manager):
        """Test search status retrieval with error"""
        from main import tavily_search

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance
        mock_client_instance.get_search_status.side_effect = Exception("Test error")

        tavily_search(mock_mcp)
        # Get the second tool (tavily_get_search_status) - calls 2,3 are for second tool
        tool_func = mock_mcp.tool.call_args_list[3][0][0]

        result = tool_func(query_id="test_query_id")

        self.assertEqual(result["status"], "error")
        self.assertIn("Error checking search status", result["message"])


class TestTavilyGetSearchResults(unittest.TestCase):
    """Test cases for tavily_get_search_results function"""

    @patch("main.key_manager")
    @patch("main.TavilyClient")
    def test_tavily_get_search_results_success(self, mock_client_class, mock_key_manager):
        """Test successful search results retrieval"""
        from main import tavily_search

        mock_mcp = create_mock_mcp()
        mock_key_manager.api_key = "test_key"
        mock_client_instance = MagicMock()
        mock_client_class.return_value = mock_client_instance

        mock_response = {
            "results": [{"title": "Test"}],
            "query": "test",
            "response_time": 0.5,
            "answer": "Answer",
            "images": [],
        }
        mock_client_instance.get_search_results.return_value = mock_response

        tavily_search(mock_mcp)
        # Get the third tool (tavily_get_search_results) - calls 4,5 are for third tool
        tool_func = mock_mcp.tool.call_args_list[5][0][0]

        result = tool_func(query_id="test_query_id")

        self.assertEqual(result["status"], "success")
        self.assertIn("results", result)


if __name__ == "__main__":
    unittest.main()
