// Here is a slash command code that selects a winner and loser and the user who will be the winner and will receive a role, 
// and it will have in the database winning streaks and select the loser if he has winning streaks before those will be removed 
// from the database, using the mongoose library and discord.js 14.13.0:

const { SlashCommandBuilder } = require('@discordjs/builders');
const { CommandInteraction, Client, Role } = require('discord.js');
const mongoose = require('mongoose');

// Create a mongoose model for the database
const WinningStreak = new mongoose.Schema({
  userId: String,
  winningStreak: Number
});

// Connect to the database
mongoose.connect('mongodb://localhost:27017/my-database');

// Get the WinningStreak model
const WinningStreakModel = mongoose.model('WinningStreak', WinningStreak);

// Create a slash command
const slashCommand = new SlashCommandBuilder()
  .setName('winner')
  .setDescription('Selects a winner and loser and the user who will be the winner and will receive a role.')
  .addUserOption('winner', 'The user who will be the winner.', true)
  .addRoleOption('winnerRole', 'The role that the winner will receive.', true);

// Create a command handler
const commandHandler = async (client, interaction) => {
  // Get the winner and loser users
  const winnerUser = interaction.options.getUser('winner');
  const loserUser = interaction.options.getUser('winner');

  // Get the winner role
  const winnerRole = interaction.options.getRole('winnerRole');

  // Check if the winner user is in the database
  const winnerWinningStreak = await WinningStreakModel.findOne({ userId: winnerUser.id });

  // If the winner user is not in the database, create a new record
  if (!winnerWinningStreak) {
    await WinningStreakModel.create({ userId: winnerUser.id, winningStreak: 1 });
  } else {
    // Increment the winner user's winning streak
    await WinningStreakModel.updateOne({ userId: winnerUser.id }, { winningStreak: winnerWinningStreak.winningStreak + 1 });
  }

  // Check if the loser user is in the database
  const loserWinningStreak = await WinningStreakModel.findOne({ userId: loserUser.id });

  // If the loser user is in the database, remove their winning streak
  if (loserWinningStreak) {
    await WinningStreakModel.deleteOne({ userId: loserUser.id });
  }

  // Add the winner role to the winner user
  await winnerUser.roles.add(winnerRole);

  // Send a message to the winner and loser users
  await winnerUser.send('Congratulations, you won!');
  await loserUser.send('Sorry, you lost.');
};

// Register the slash command
client.on('ready', () => {
  client.commands.register(slashCommand);
});

// Handle the slash command
client.on('interactionCreate', async (interaction) => {
  if (interaction.isCommand() && interaction.commandName === 'winner') {
    await commandHandler(client, interaction);
  }
});

