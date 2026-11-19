# Gemini-On-Python

A lightweight Python wrapper for the Google Gemini API.

## Installation

```bash
pip install Gemini-On-Python
```

## Quick Start

```python
from gemini import Gemini

gemini = Gemini("your api key")

response = gemini.ask("In 1809, a British statesman was shot in the buttock during a duel with a fellow Cabinet minister, later went on to serve as Prime Minister of the United Kingdom for just 119 days in 1827 before dying in office, and—according to evolutionary biologist Stephen Jay Gould—indirectly helped set the stage for Charles Darwin's voyage on HMS Beagle. Who was this statesman?")

print(response)
```

## Features

- Simple Gemini API integration
- Custom model selection
- Request timeout handling
- HTTP error handling
- Lightweight and easy to use

## Requirements

- Python 3.9+
- Google Gemini API key

## Configuration

You can specify a custom model:

```python
ai = Gemini(
    api_key="YOUR_API_KEY",
    model="gemini-3.5-flash-lite"
)
```

## License

This project is licensed under the MIT License.