import { Client, CommandInteraction, MessageEmbed } from discord.js;

module.exports = {
    name: 'waifu',
    description: 'Get a waifu from waifu.im with an optional tag. eg: /waifu maid',
    /** 
     * @param {Client} client 
     * @param {CommandInteraction} interaction
     */
    run: async (client, interaction) => {
        if (!tag) {
            const REQUEST = await fetch('https://api.waifu.im/random/');
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im](' + URL + ')')
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await interaction.reply(':x: Whoopsie! Something went wrong! Please try again.\n\nIf the problem persists, contact my support team at: `discord.me/socket-development`');
            else await interaction.respond({ embeds: [EMBED] });
        } else if (tag) {
            const REQUEST = await fetch(`https://api.waifu.im/random/?${tag}=true`);
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im](' + URL + ')')
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await interaction.reply(':x: Whoopsie! Something went wrong! Please try again.\n\nIf the problem persists, contact my support team at: `discord.me/socket-development`');
            else await interaction.respond({ embeds: [EMBED] });
        }
    }
}