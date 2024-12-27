# Magic8bot 🎱

Magic8bot is a tiny and lightweight Discord bot inspired by the classic Magic 8-Ball, offering users the chance to ask questions and receive fun, randomized responses. It's built using the `discord.py` library and includes commands to interact with the bot via Discord slash commands.

## Project Structure

Here's a breakdown of the project files:

```
Magic8bot
├── /src
│   ├── ball.py        # Contains logic for generating responses
│   └── bot.py         # Main bot file for handling interactions and commands
│
├── .gitignore
├── LICENSE
└── README.md
```

## Dependencies

The bot requires the following Python libraries:
- `discord.py`: For interacting with the Discord API.

## Setting Up a Virtual Environment

To avoid polluting your system Python environment, it's recommended to set up a virtual environment:

1. **Create the virtual environment:**
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment:**
   - On **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - On **Linux/macOS**:
     ```bash
     source .venv/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install discord.py
   ```

## Setting Environment Variables

To store your Discord bot token, set an environment variable for BOT_TOKEN:

- On **Windows**:

```powershell
set BOT_TOKEN=your_discord_bot_token
```

- On **Linux/macOS**:

```bash
export BOT_TOKEN=your_discord_bot_token
```

## How to Run the Project

1. Ensure the virtual environment is active (see instructions above).
2. Set the environment variable as shown above.
3. Run the bot:

```bash
cd src
python bot.py
```


Once started, the bot will sync and listen for the `/ask` command in Discord, allowing users to ask questions.

## License

This project is licensed under the MIT License.
