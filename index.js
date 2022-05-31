const Cluster = require("discord-hybrid-sharding");
const { Collection, Client } = require("discord.js");


const client = new Client({
    shards: Cluster.data.SHARD_LIST,
    shardCount: Cluster.data.TOTAL_SHARDS,
    allowedMentions: {
        repliedUser: true,
        parse: ["users", "roles", "everyone"]
    },
    intents: 131071,
});

client.cluster = new Cluster.Client(client);
client.cluster.broadcastEval(c => c.guilds.cache.size)
    .then(results => console.log(`${results.reduce((prev, val) => prev + val, 0)} total guilds`));

module.exports = client;

client.commands = new Collection();
client.aliases = new Collection();
client.SlashCommands = new Collection();

require('./Handler/handler')(client);