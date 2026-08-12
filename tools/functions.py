"""All tools for the agent - weather, time, search, etc."""

import requests
import json
from datetime import datetime
from duckduckgo_search import DDGS

def get_tools():
    """Return list of available tools"""
    return {
        "get_weather": get_weather,
        "get_time": get_time,
        "search_web": search_web,
        "calculate": calculate,
        "get_fact": get_fact
    }

def get_weather(city: str) -> str:
    """Get weather for a city using free API"""
    try:
        # Using free weather API (no API key needed)
        url = f"https://wttr.in/{city}?format=%C+%t"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"Weather in {city}: {response.text}"
        else:
            return f"Could not get weather for {city}"
    except Exception as e:
        return f"Weather API error: {str(e)}"

def get_time(timezone: str = "UTC") -> str:
    """Get current time"""
    try:
        if timezone == "UTC":
            now = datetime.utcnow()
        else:
            now = datetime.now()
        return f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"
    except Exception as e:
        return f"Time API error: {str(e)}"

def search_web(query: str) -> str:
    """Search the web using DuckDuckGo"""
    try:
        with DDGS() as ddgs:
            results = []
            for r in ddgs.text(query, max_results=3):
                results.append(f"{r['title']}: {r['body'][:200]}...")
            if results:
                return "\n\n".join(results)
            else:
                return "No results found"
    except Exception as e:
        return f"Search error: {str(e)}"

def calculate(expression: str) -> str:
    """Calculate mathematical expression"""
    try:
        # Security: only allow safe operations
        allowed = ['+', '-', '*', '/', '(', ')', ' ']
        if not all(c in allowed or c.isdigit() for c in expression):
            return "Invalid expression"
        
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"

def get_fact(topic: str = "") -> str:
    """Get a random fact about a topic"""
    facts = {
        "space": "Space is completely silent because there's no air for sound to travel through.",
        "ai": "The first AI program was written in 1951 by Christopher Strachey.",
        "python": "Python was named after Monty Python, not the snake.",
        "default": "Did you know? The first computer mouse was made of wood."
    }
    
    for key in facts:
        if key in topic.lower():
            return facts[key]
    return facts["default"]