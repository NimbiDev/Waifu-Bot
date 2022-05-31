const {
    Client,
    Message,
    String,
    MessageEmbed
} = require('discord.js');
const { fetch } = require('fetch');


module.exports = {
    name: 'waifu',
    description: 'Get a waifu from waifu.im with an optional tag. eg: w.waifu maid',
    aliases: ['w'],
    arguments: '[tag]',
    /**
     * @param {Client} client 
     * @param {Message} message 
     * @param {String} tag
     * @returns 
     */
    run: async (client, message, tag) => {
        if (!tag) {
            const REQUEST = await fetch('https://api.waifu.im/random/');
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im]({})'.join(URL))
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await message.reply(':x: Whoopsie! Something went wrong!');
            else await message.reply({ embeds: [EMBED], });
        } else if (tag) {
            const REQUEST = await fetch('https://api.waifu.im/random/?{}=true'.join(tag));
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im]({})'.join(URL))
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await message.reply(':x: Whoopsie! Something went wrong!');
            else await message.reply({ embeds: [EMBED], });
        }
    }
}