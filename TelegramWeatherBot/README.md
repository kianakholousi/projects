
# Weather Telegram Bot

This is a simple Telegram bot that provides weather information for various cities. Users can interact with the bot by sending commands and selecting options from the provided keyboard.

## Getting Started

To use this bot, you will need to have a Telegram account and obtain an API token. Follow these steps to get started:

1. Create a new bot on Telegram by talking to the [BotFather](https://core.telegram.org/bots#botfather).
2. Obtain the API token for your bot.
3. Clone this repository to your local machine.

## Prerequisites

Before running the bot, make sure you have the following requirements installed:

- Python 3.x
- `requests` library
- `json` library
- `logging` library

You can install the required libraries by running the following command:

```
pip install requests
```

## Configuration

Open the `main.py` file and locate the following lines:

```python
TOKEN = "XXXXXXXXXXX"
OWM_KEY = "XXXXXXXXXXX"
```

Replace `"XXXXXXXXXXX"` with your Telegram API token and OpenWeatherMap API key, respectively.

## Usage

To start the bot, run the following command in your terminal:

```
python main.py
```

Once the bot is running, you can interact with it by sending commands in a Telegram chat. Here are the available commands:

- `/start`: Displays a welcome message and instructions on how to use the bot.
- `/weather`: Prompts you to select a city from the provided keyboard.

When you select a city, the bot will retrieve the current weather information for that city and display it in the chat.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This bot was developed using the Telegram Bot API and the OpenWeatherMap API.
- Special thanks to the developers of the `requests` library for making HTTP requests in Python easier.
