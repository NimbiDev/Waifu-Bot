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

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im](' + URL + ')')
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await interaction.reply(':x: Whoopsie! Something went wrong!');
            else await interaction.respond({ embeds: [EMBED] });
        } else if (tag) {
            const REQUEST = await fetch(`https://api.waifu.im/random/?${tag}=true`);
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im](' + URL + ')')
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await interaction.reply(':x: Whoopsie! Something went wrong!');
            else await interaction.respond({ embeds: [EMBED] });
        }
    }
}