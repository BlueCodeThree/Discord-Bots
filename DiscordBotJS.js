// This is a discord bot, made by Carlie Hamilton
// http://carliehamilton.com   ~  carliemhamilton@gmail.com
// Designed to respond to user input, nothing serious. 

const Discord = require('discord.js');
const client = new Discord.Client();


// This is from somewhere, I believe it's the Fisher–Yates shuffle function
var shuffle = function (array) {
	var currentIndex = array.length;
	var temporaryValue, randomIndex;

	// While there remain elements to shuffle...
	while (0 !== currentIndex) {
		// Pick a remaining element...
		randomIndex = Math.floor(Math.random() * currentIndex);
		currentIndex -= 1;

		// And swap it with the current element.
		temporaryValue = array[currentIndex];
		array[currentIndex] = array[randomIndex];
		array[randomIndex] = temporaryValue;
	}
	return array;
};

// These are the answers (where more than one answer exists). 
// These have been shuffled so that it starts with a random saying 
var answer = ["*nods nods*", "uh-huh", "mmmhmm", "*nods a little*", "*pets you gently*", "*smirks at you*", "*smirks down at you*",  "*smiles and pets you*", "*strokes you sympathetically*", "*strokes you gently*", "*nods looking down at you*", "*grins at you*", "*laughs*" ];
var shuffledAnswer = shuffle(answer.slice());

var praiseanswer = ["that's awesome!", "well done!", "you've done an amazing job", "wow!" ]; 
var shuffledpraise = shuffle(praiseanswer.slice());


// starting the discord client, commands go in here. 
client.on("message", message => {

  // We declare the prefix
	var prefix = '!';

	// The bot adds reactions if someone starts their message with "nice"
	if(message.content.startsWith("nice")){
		message.react('☝')
		message.react('💙')
		message.react('😍')
		message.react('😊')
		.then(console.log)
		.catch(console.error);
	};

// The bot will answer with something random from the above lists
// The lists have been shuffled (above), and the code here is so 
//  that the bot doesn't give the same answer twice in a row


// The robot will answer this if a user says !reply
if(message.content.startsWith(prefix + "reply")){
	valueToUse = shuffledAnswer[0];
	shuffledAnswer.splice(0, 1);  //this removes 1 item at index 0
	shuffledAnswer.splice(Math.floor(shuffledAnswer.length/2 + Math.random() * shuffledAnswer.length/2), 0, valueToUse);
       message.channel.send(valueToUse);
};

// The robot will answer this if a user does !praise
if(message.content.startsWith(prefix + "praise")){
	PraiseToUse = shuffledpraise[0];
	shuffledpraise.splice(0, 1);  //this removes 1 item at index 0
	shuffledpraise.splice(Math.floor(shuffledpraise.length/2 + Math.random() * shuffledpraise.length/2), 0, PraiseToUse);
       message.channel.send(PraiseToUse);
};


// These are answers that have a single reply

// The robot will answer this if a user does !sexy
if(message.content.startsWith(prefix + "sexy")){
   message.channel.send("Carlie, you are so sexy.");
};

// The robot will answer this if a user does !agree
if(message.content.startsWith(prefix + "agree")){
   message.channel.send("I agree with Carlie. ");
};

// The robot will answer this if a user does !doit
if(message.content.startsWith(prefix + "doit")){
   message.channel.send("You can do it! ");
};


// The robot will answer this if a user does !meanie
if(message.content.startsWith(prefix + "meanie")){
   message.channel.send("I was nice and mean");
};

// The robot will answer this if a user does !goodnight
if(message.content.startsWith(prefix + "goodnight")){
   message.channel.send("Goodnight Carlie, looking forward to talking to you in the morning.");
};

// The robot will answer this if a user does !hug
if(message.content.startsWith(prefix + "hug")){
   message.channel.send("*holds you tight*");
};

// The robot will answer this if a user does !hi
if(message.content.startsWith(prefix + "hi")){
   message.channel.send("Why hello there beautiful Carlie!");
};

// The robot will answer this if a user does !sing
if(message.content.startsWith(prefix + "sing")){
   message.channel.send("*I'm like a time bomb ticking in your head*");
      message.channel.send("*Paranoia clouding your judgment*");
	     message.channel.send("*And no matter what you do about it, about it, about it*");
		    message.channel.send("*I'm still in your head*");
};


});

client.login(" ");