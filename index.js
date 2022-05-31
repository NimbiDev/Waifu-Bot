require('dotenv').config;

const {
    Collection,
    Client
} = require("discord.js");


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

require('./Handler/handler')(client);

client.login(process.env.TOKEN)