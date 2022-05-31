const client = require('../index.js');
const {
    owners
} = require('../json/owners.json');

client.on("interactionCreate", async (interaction) => {

    if (interaction.isCommand()) {
        const command = client.SlashCommands.get(interaction.commandName);

        if (!command) return interaction.reply({
            content: "An Error has occurred!",
            ephemeral: true
        }) && client.SlashCommands.delete(interaction.commandName)

        if (!interaction.member.permissions.has(command.userPermissions || [])) return interaction.reply({
            content: `${process.env.FAILURE_EMOJI} You need \`${command.userPermissions || []}\` permissions to run this command`,
            ephemeral: true,
        });

        if (command.maintenance) {
            if (!owners.includes(interaction.user.id)) {
                return interaction.reply({
                    content: `${process.env.FAILURE_EMOJI} This command is on maintenance please try later, Thank you!`
                })
            }
        }

        if (!interaction.guild.me.permissions.has(command.botPermissions || []))
            return interaction.reply({
                content: `${process.env.FAILURE_EMOJI} I need \`${cmd.botPermissions || []}\` permissions to run this command`,
                ephemeral: true
            });

        if (command.ownerOnly) {
            if (!owners.includes(interaction.user.id)) {
                return interaction.reply({
                    content: `${process.env.FAILURE_EMOJI} Only the Bot Developers are allowed to run this command!`
                })
            }
        };

        command.run(client, interaction); 
    }

    if (interaction.isContextMenu()) {
        const command = client.SlashCommands.get(interaction.commandName);
        if (command) command.run(client, interaction);
    }

})