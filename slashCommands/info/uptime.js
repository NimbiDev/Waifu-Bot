const { Discord } = require('discord.js');

module.exports = {
    name: 'uptime',
    description: 'Check Bots uptime',
    /** 
     * @param {Discord.Client} client 
     * @param {Discord.CommandInteraction} interaction
     */
    run: async (client, interaction) => {
        let totalSeconds = (client.uptime / 1000);
        let days = Math.floor(totalSeconds / 86400);
        totalSeconds %= 86400;
        let hours = Math.floor(totalSeconds / 3600);
        totalSeconds %= 3600;
        let minutes = Math.floor(totalSeconds / 60);
        let seconds = Math.floor(totalSeconds % 60);

        const EMBED = new Discord.MessageEmbed()
            .setColor("RED")
            .setTimestamp()
            .setDescription(`**Uptime**: \` ${days} Day(s), ${hours} Hour(s), ${minutes} Minute(s), ${seconds} Second(s) \``)

        interaction.reply({ embeds: [EMBED] });
    }
}