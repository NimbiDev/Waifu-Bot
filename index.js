const { Collection, Client } = require("discord.js");
require("dotenv").config();


const client = new Client({
    allowedMentions: {
        repliedUser: true,
        parse: ["users", "roles", "everyone"]
    },
    intents: 512,
});


module.exports = client;

client.commands = new Collection();
client.aliases = new Collection();
client.SlashCommands = new Collection();

require('./Handler/handler')(client);

client.logon(process.env.TOKEN)