import dotenv from "dotenv"
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

import "client.cjs";

client.login(process.env.TOKEN)