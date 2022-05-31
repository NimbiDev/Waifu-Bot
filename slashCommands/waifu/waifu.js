const {
    Client,
    CommandInteraction,
    String,
    MessageEmbed
} = require('discord.js');
const { fetch } = require('fetch');


module.exports = {
    name: 'waifu',
    description: 'Get a waifu from waifu.im with an optional tag. eg: /waifu maid',
    arguments: '[tag]',
    /** 
     * @param {Client} client 
     * @param {CommandInteraction} interaction
     * @param {String} tag
     * @returns 
     */
    run: async (client, interaction, tag) => {
        if (!tag) {
            const REQUEST = await fetch('https://api.waifu.im/random/');
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];
            if (!URL) await interaction.reply(':x: Whoopsie! Something went wrong!');
            else await interaction.respond(URL);
        } else if (tag) {
            const REQUEST = await fetch('https://api.waifu.im/random/?{}=true'.join(tag));
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];
            if (!URL) await interaction.reply(':x: Whoopsie! Something went wrong!');
            else await interaction.respond(URL);
        }
    }
}