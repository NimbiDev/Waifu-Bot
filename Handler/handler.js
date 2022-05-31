import { Client } from 'discord.js';
import glob from "glob-promise";
import chalk from 'chalk';
/**
 * @param {Client} client
 */

export default async (client) => {
    const slashCommands = [];
    const SlashCommandsFiles = await glob.promise(`${process.cwd()}/slashCommands/*/*.js`);
    SlashCommandsFiles.map(async (path) => {
        const file = require(path);
        if (!file?.name) return
        const splitted = path.split("/");
        const dir = splitted[splitted.length - 2];
        const files = {
            dir,
            ...file
        }
        client.SlashCommands.set(file.name, files);
        slashCommands.push(file)

    });
    client.on("ready", async () => {
        await client.application.commands.set(slashCommands)
            .then(console.log(
                chalk.white(`✅ Successfully Registered`), chalk.red(client.SlashCommands.size),
                chalk.white('Slash Commands in'), chalk.red(client.guilds.cache.size),
                chalk.white(`${client.guilds.cache.size > 1 ? "Guilds" : "Guild"}`
                )
            ))
    });

    const eventFiles = await globPromise(`${process.cwd()}/Events/*.js`);
    eventFiles.map(async (filePaths) => require(filePaths));
}