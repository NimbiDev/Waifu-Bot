import { Client } from 'discord.js';
import glob from 'glob';
import promisify from 'util';
import chalk from 'chalk';
/**
 * @param {Client} client
 */

export default module.exports = async (client) => {
    const globPromise = promisify(glob);
    const LegacyCommands = await globPromise(`${process.cwd()}/commands/*/*.js`);
    LegacyCommands.map(async (path) => {
        const file = require(path);
        const splitted = path.split("/");
        const dir = splitted[splitted.length - 2];
        const cmdName = file?.name;
        const cmdAliases = file?.aliases;
        const files = {
            dir,
            ...file
        }

        if (cmdName) {
            client.commands.set(cmdName, files);
            if (cmdAliases < 1) return;
            if (cmdAliases && Array.isArray(cmdAliases)) {
                cmdAliases.forEach(alias => client.aliases.set(alias, files))
            }
        }
    });

    const slashCommands = [];
    const SlashCommandsFiles = await globPromise(`${process.cwd()}/slashCommands/*/*.js`);
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