[Unit]
Description=My Telegram Bot
After=network.target

[Service]
User=root
WorkingDirectory=/root/Telegram_bot/
ExecStart=/root/Telegram_bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
