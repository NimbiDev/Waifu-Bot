export const client = require('./index.js');
export const { MessageEmbed, Client, Collection } = require('discord.js');
export const { inspect } = require("util");
export const Handler = require('./Handler/handler.js')(client);
