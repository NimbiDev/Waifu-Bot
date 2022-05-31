const client = require('./index.js');
const { MessageEmbed, Client, Collection } = require('discord.js');
const { inspect } = require("util");
const Handler = require('./Handler/handler.js')(client);
