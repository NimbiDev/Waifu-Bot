import {
    Client,
    Message,
    String,
    MessageEmbed
} from 'discord.js';

export default module.exports = {
    name: 'uptime',
    description: 'Check Bots uptime',
    /**
     * @param {Client} client 
     * @param {Message} message 
     * @param {String} args 
     * @returns 
     */
    run: async (client, message, args) => {
        if (!tag) {
            const REQUEST = await fetch('https://api.waifu.im/random/');
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im](' + URL + ')')
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await message.reply(':x: Whoopsie! Something went wrong! Please try again.\n\nIf the problem persists, contact my support team at: `discord.me/socket-development`');
            else await message.reply({ embeds: [EMBED] });
        } else if (tag) {
            const REQUEST = await fetch(`https://api.waifu.im/random/?${tag}=true`);
            const DATA = await REQUEST.json();
            const URL = DATA['images'][0]['url'];

            const EMBED = new MessageEmbed()
                .setDescription('**Direct Link**: [waifu.im](' + URL + ')')
                .setImage({ url: String(URL) })
                .setColor('DARK_PINK');
            if (!URL) await message.reply(':x: Whoopsie! Something went wrong! Please try again.\n\nIf the problem persists, contact my support team at: `discord.me/socket-development`');
            else await message.reply({ embeds: [EMBED] });
        }
    }
}