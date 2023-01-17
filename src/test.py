import unittest
from unittest.mock import patch, MagicMock
import discord
from discord.ext import commands
import responses
import os

from src.bot import run_discord_bot


class TestDiscordBot(unittest.TestCase):
    def setUp(self):
        # Create a mock discord client
        self.client = MagicMock(spec=discord.Client)
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.typing = False
        intents.presences = False
        self.bot = commands.Bot(command_prefix='$', client=self.client, intents=intents)

    @patch('responses.get_response')
    @patch('os.getenv')
    @patch('discord.Client.run')
    def test_run_discord_bot(self, run_mock, getenv_mock, get_response_mock):
        # Set up mocks
        getenv_mock.return_value = 'test_token'
        get_response_mock.return_value = 'test_response'
        message = MagicMock(spec=discord.Message)

        # Test the function
        run_discord_bot()
        run_mock.assert_called_with('test_token')
        self.client.on_message.assert_called_with(message)
        getenv_mock.assert_called_with('token_key')

    @patch('responses.get_response')
    def test_on_message(self, get_response_mock):
        # Set up mocks
        get_response_mock.return_value = 'test_response'
        message = MagicMock(spec=discord.Message)
        message.author = 'test_author'
        message.content = 'test_content'
        message.channel = 'test_channel'
        message.author.send = MagicMock()

        # Test the on_message event
        self.client.on_message(message)
        message.author.send.assert_called_with('test_response')
        get_response_mock.assert_called_with('test_content')

    @patch('responses.get_response')
    def test_resources_cmd(self, get_response_mock):
        # Set up mocks
        get_response_mock.return_value = 'test_response'
        ctx = MagicMock(spec=discord.ext.commands.Context)
        ctx.send = MagicMock()

        # Test the resources command
        self.bot.resources(ctx)
        ctx.send.assert_called_with('test_response')
        get_response_mock.assert_called_with('$resources')


if __name__ == '__main__':
    unittest.main()
