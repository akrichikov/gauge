# Gauge

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/gauge-llm.svg)](https://pypi.org/project/gauge-llm/)

Gauge is a powerful and easy-to-use Python library for evaluating and comparing various language models (LLMs) using custom benchmarks. It allows you to try out different temperatures and prompts, and compare the results across multiple models. The library is designed to be extensible, with support for more models to be added in the future.

## Features

- Evaluate and compare multiple LLMs using custom benchmarks
- Supports different temperatures and prompts
- Easy-to-use API for running and evaluating LLMs
- Extensible architecture for adding more models in the future

## Installation

To install Gauge, simply run the following command:

```bash
!pip install gauge-llm
```

## Usage

Here's a quick example of how to use Gauge:

```python
import gauge
gauge.evaluate("Tell a story about a brave knight but stay in first person perspective the whole time.")
```

## API

### `gauge.run(model, query)`

Runs the specified model with the given query and returns the output, latency, and cost.

**Parameters:**

- `model`: A dictionary containing the model's information (type, name, id, and price_per_second).
- `query`: The input query for the model.

**Returns:**

- `output`: The generated output from the model.
- `latency`: The time taken to run the model.
- `cost`: The cost of running the model.

### `gauge.evaluate(query)`

Evaluates multiple LLMs using the given query and displays a table with the results, including the model's name, response, score, explanation, latency, and cost.

**Parameters:**

- `query`: The input query for the models.

## Example

Here's an example of how Gauge can be used to evaluate and compare multiple LLMs:

```python
import gauge

query = "Tell a story about a brave knight but stay in first person perspective the whole time."
gauge.evaluate(query)
```

This will display a table with the results for each model, including their name, response, score, explanation, latency, and cost.

## Contributing

We welcome contributions to Gauge! If you'd like to add a new model or improve the existing code, please feel free to submit a pull request. If you encounter any issues or have suggestions, please open an issue on GitHub.

## License

Gauge is released under the [MIT License](https://opensource.org/licenses/MIT).