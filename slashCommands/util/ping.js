const { Discord } = require('discord.js');

module.exports = {
    name: 'ping',
    description: 'Check Bots ping',
    /** 
     * @param {Discord.Client} client 
     * @param {Discord.CommandInteraction} interaction
     */
    run: async (client, interaction) => {
        const EMBED = new Discord.MessageEmbed()
            .setColor('DARK_PINK')
            .setDescription(`**Client's Ping**: \` ${client.ws.ping}ms \`\n**Message Ping**: \` ${Date.now() - interaction.createdTimestamp}ms\``)

        interaction.reply({ embeds: [EMBED] })
    }
}