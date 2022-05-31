import chalk from 'chalk';
import client from '../index.js';
import { dependencies } from '../package.json';

const ver = dependencies['discord.js'];
const mongooseConnectionString = process.env.MONGO_CONNECTION_URL;

import { connect } from 'mongoose';

client.on("ready", async () => {
    setInterval(() => {
        client.user.setPresence({
            activities: [{
                name: `${client.guilds.cache.size} Servers!`,
                type: 'WATCHING'
            }],
            status: 'online'
        });
    }, 60000)

    console.clear();
    console.log("")
    console.log(
        chalk.red.bold("——————————[Basic Info]——————————")
    )
    console.log(
        chalk.white(`${client.guilds.cache.reduce((a, b) => a + b.memberCount, 0) > 1 ? "Users:" : "User:"}`),
        chalk.red(`${client.guilds.cache.reduce((a, b) => a + b.memberCount, 0)}`),
        chalk.white("||"),
        chalk.white(`${client.guilds.cache.size > 1 ? "Servers:" : "Server:"}`),
        chalk.red(`${client.guilds.cache.size}`),
    )
    console.log(
        chalk.white(`Slash Commands:`),
        chalk.red(`${client.SlashCommands.size}`)
    )

    console.log("")
    console.log(chalk.red.bold("——————————[Statistics]——————————"))
    console.log(
        chalk.white(`Running on Node`),
        chalk.green(process.version),
        chalk.white('on'),
        chalk.green(`${process.platform} ${process.arch}`)
    )
    console.log(
        chalk.white('Memory:'),
        chalk.green(`${(process.memoryUsage().rss / 1024 / 1024).toFixed(2)}`),
        chalk.white('MB')
    )
    console.log(
        chalk.white('RSS:'),
        chalk.green(`${(process.memoryUsage().heapUsed / 1024 / 1024).toFixed(2)}`),
        chalk.white('MB')
    )
    console.log(
        chalk.white('Discord.js Verion:'),
        chalk.green(ver)
    )
    console.log("")
    console.log(
        chalk.red.bold("——————————[Connections]——————————")
    )
    console.log(
        chalk.white("✅ Successfully Connected To"),
        chalk.red(`${client.user.tag}`),
        chalk.white('('),
        chalk.green(client.user.id),
        chalk.white(')'))
    connect(mongooseConnectionString, {})
        .then(console.log(chalk.white("✅ Successfully Connected To"),
            chalk.red(`Mongoose Data Base`)))
})