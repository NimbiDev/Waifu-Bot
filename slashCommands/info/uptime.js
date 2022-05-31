const {
    Client,
    CommandInteraction,
    String,
    MessageEmbed
} = require('discord.js');


module.exports = {
    name: 'uptime',
    description: 'Check Bots uptime',
    /** 
     * @param {Client} client 
     * @param {CommandInteraction} interaction
     */
    run: async (client, interaction) => {
        let totalSeconds = (client.uptime / 1000);
        let days = Math.floor(totalSeconds / 86400);
        totalSeconds %= 86400;
        let hours = Math.floor(totalSeconds / 3600);
        totalSeconds %= 3600;
        let minutes = Math.floor(totalSeconds / 60);
        let seconds = Math.floor(totalSeconds % 60);

        const EMBED = new MessageEmbed()
            .setColor("DARK_PINK")
            .setTimestamp()
            .setDescription(`**Uptime**: \` ${days} Day(s), ${hours} Hour(s), ${minutes} Minute(s), ${seconds} Second(s) \``)

        interaction.reply({ embeds: [EMBED] });
    }
}