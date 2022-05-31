require('dotenv').config;

const {
    Collection,
    Client
} = require('discord.js');

const client = new Client({
    allowedMentions: {
        repliedUser: true,
        parse: ["users", "roles", "everyone"]
    },
    intents: 513,
});

module.exports = client;

client.commands = new Collection();
client.aliases = new Collection();
client.SlashCommands = new Collection();

import Handler from "./imports.cjs"

client.login(process.env.TOKEN)