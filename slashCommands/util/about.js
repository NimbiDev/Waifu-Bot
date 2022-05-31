const { Discord } = require('discord.js');

module.exports = {
    name: 'about',
    description: 'Responds with information about the bot.',
    /** 
     * @param {Discord.Client} client 
     * @param {Discord.CommandInteraction} interaction
     */
    run: async (client, interaction) => {
        const Website = new Discord.MessageButton()
            .setCustomId('website-button')
            .setLabel('Website')
            .setStyle('LINK')
            .setUrl('https://waifu-im.socket-development.nl');
        const Github = new Discord.MessageButton()
            .setCustomId('github-button')
            .setLabel('Github')
            .setStyle('LINK')
            .setUrl('https://github.com/socket-development/waifu-im');
        const Commands = new Discord.MessageButton()
            .setCustomId('commands-button')
            .setLabel('Commands')
            .setStyle('LINK')
            .setUrl('https://github.com/socket-development/waifu-im/README.md#Commands');
        const Support = new Discord.MessageButton()
            .setCustomId('support-button')
            .setLabel('Commands')
            .setStyle('LINK')
            .setUrl('https://github.com/socket-development/waifu-im/issues');

        const ROW = new Discord.MessageActionRow()
            .addComponents(
                Website,
                Github,
                Commands,
                Support
            );

        const EMBED = new Discord.MessageEmbed()
            .setColor('DARK_PINK')
            .setDescription('Waifu Collection and Battle Discord bot using waifu.im api.');

        await interaction.reply({ ephemeral: true, embeds: [EMBED], components: [ROW] });
    }
};