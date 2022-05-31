const client = require("../index.cjs");
const {
    owners
} = require('../json/owners.json');
const prefix = process.env.PREFIX;

client.on("messageCreate", async (message) => {
    if (message.author.bot || !message.guild || !message.content.toLowerCase().startsWith(prefix)) return;

    const args = message.content.slice(prefix.length).trim().split(" ");
    const cmd = args.shift().toLowerCase();
    const command = client.commands.get(cmd) || client.commands.find(c => c.aliases?.includes(cmd));

    if (!command) return;
    if (command) {

        if (!message.member.permissions.has(command.userPermissions || [])) return message.reply({
            content: `${process.env.FAILURE_EMOJI} You need \`${command.userPermissions || []}\` permissions to run this command`,
            ephemeral: true,
        });

        if (command.maintenance) {
            if (!owners.includes(message.user.id)) {
                return message.reply({
                    content: `${process.env.FAILURE_EMOJI} This command is on maintenance please try later, Thank you!`
                })
            }
        }

        if (!message.guild.me.permissions.has(command.botPermissions || []))
            return message.reply({
                content: `${process.env.FAILURE_EMOJI} I need \`${cmd.botPermissions || []}\` permissions to run this command`,
                ephemeral: true
            });

        if (command.ownerOnly) {
            if (!owners.includes(message.user.id)) {
                return message.reply({
                    content: `${process.env.FAILURE_EMOJI} Only the Bot Developers are allowed to run this command!`
                })
            }
        };

        await command.run(client, message, args)
    }
});