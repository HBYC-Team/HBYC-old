/* THIS FILE IS STILL IN DEVELOP AND TESTING
PLEASE DO NOT CHANGE THIS FILE IF YOU DON'T KNOW WHAT YOU ARE DOING*/
const { Client } = require("discord.js");
const client = new Client({ intents: ['GUILDS', 'GUILD_MESSAGES'] });
const token = process.env.js_token;

client.on("message", msg => {
		if(msg.content === "ping") {
				msg.reply("pong");
		}
})

client.login("token");
