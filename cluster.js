require("dotenv").config();

const Cluster = require("discord-hybrid-sharding");

const manager = new Cluster.Manager(`${__dirname}/bot.js`, {
    totalShards: auto,
    shardsPerClusters: 5,
    mode: "process",
    token: process.env.TOKEN,
})
manager.on('clusterCreate', cluster => console.log(`Launched Cluster ${cluster.id}`));
manager.spawn({ timeout: -1 });