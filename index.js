import dotenv from "dotenv";
dotenv.config();

import {
    Collection,
    Client
} from "discord.js";


const client = new Client({
    allowedMentions: {
        repliedUser: true,
        parse: ["users", "roles", "everyone"]
    },
    intents: 513,
});


client.module.exports = client;

client.commands = new Collection();
client.aliases = new Collection();
client.SlashCommands = new Collection();

import './Handler/handler.js';

client.login(process.env.TOKEN)