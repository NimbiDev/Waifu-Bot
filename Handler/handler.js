const { Client } = require('discord.js');
const { glob } = require('glob');
const { promisify } = require('util');
const globPromise = promisify(glob);/**
* @file import compiled ES modules as a workaround
*/

const chalk = require('chalk')
const fs = require('fs')
const Module = require('module')


// Node: bypass [ERR_REQUIRE_ESM]
const orig = Module._extensions['.js']
Module._extensions['.js'] = function (module, filename) {
   try {
       return orig(module, filename)
   } catch (e) {
       if (e.code === 'ERR_REQUIRE_ESM') {
           const content = fs.readFileSync(filename, 'utf8')
           module._compile(content, filename)
       }
   }
}

const _esmRequire = esm(module, {
   cjs: true,
   mode: 'all',
})

// don't pollute Module
Module._extensions['.js'] = orig


module.exports = function esmRequire(id) {
   return _esmRequire(id)
}

/**
 * @param {Client} client
 */

module.exports = async (client) => {
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