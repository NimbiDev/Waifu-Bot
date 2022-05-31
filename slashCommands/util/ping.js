import { Client, CommandInteraction, MessageEmbed } from "discord.js";

export default {
    name: 'ping',
    description: 'Check Bots ping',
    /** 
     * @param {Client} client 
     * @param {CommandInteraction} interaction
     */
    run: async (client, interaction) => {
        const EMBED = new MessageEmbed()
            .setColor('DARK_PINK')
            .setDescription(`**Client's Ping**: \` ${client.ws.ping}ms \`\n**Message Ping**: \` ${Date.now() - interaction.createdTimestamp}ms\``)

        interaction.reply({ embeds: [EMBED] })
    }
}