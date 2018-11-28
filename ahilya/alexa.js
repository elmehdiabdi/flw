/* eslint-disable  func-names */
/* eslint quote-props: ["error", "consistent"]*/
/**
 * This sample demonstrates a simple skill built with the Amazon Alexa Skills
 * nodejs skill development kit.
 * This sample supports multiple lauguages. (en-US, en-GB, de-DE).
 * The Intent Schema, Custom Slots and Sample Utterances for this skill, as well
 * as testing instructions are located at https://github.com/alexa/skill-sample-nodejs-fact
 **/

'use strict';

const Alexa = require('alexa-sdk');

const APP_ID = undefined;  // TODO replace with your app ID (OPTIONAL).

const languageStrings = {
    'en': {
        translation: {
            FACTS: ['Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live','All computers wait at the same speed', 'A misplaced decimal point will always end up where it will do the greatest damage', 'A good programmer looks both ways before crossing a one-way street', 'A computer program does what you tell it to do not what you want it to do', 'Intel Inside is a Government Warning required by Law', 'Common sense gets a lot of credit that belongs to cold feet', 'Chuck Norris doesnt go hunting Chuck Norris goes killing', 'Chuck Norris counted to infinity twice', 'C is quirky flawed and an enormous success', 'Beta is Latin for still doesnt work', 'ASCII stupid question get a stupid ANSI', 'Artificial Intelligence usually beats natural stupidity', 'Any fool can use a computer Many do', 'Hey It compiles Ship it', 'Hate cannot drive out hate only love can do that', 'Guns dont kill people Chuck Norris kills people', 'God is real unless declared integer', 'First solve the problem. Then write the code.', 'Experience is the name everyone gives to their mistakes', 'Every piece of software written today is likely going to infringe on someone elses patent', 'Computers make very fast very accurate mistakes', 'Computers do not solve problems they execute solutions', 'I have NOT lost my mindI have it backed up on tape somewhere', 'If brute force doesnt solve your problems then you arent using enough', 'It works on my machine', 'Java is in many ways C++??', 'Keyboard not found...Press any key to continue.', 'Life would be so much easier if we only had the source code.', 'Mac users swear by their Mac PC users swear at their PC', 'Microsoft is not the answer Microsoft is the question No is the answer', 'MS-DOS isnt dead it just smells that way', ' Only half of programming is coding The other 90% is debugging', ' Pasting code from the Internet into production code is like chewing gum found in the street', 'Press any key to continue or any other key to quit.', 'Profanity is the one language all programmers know best', 'The best thing about a boolean is even if you are wrong you are only off by a bit', 'The nice thing about standards is that there are so many to choose from', 'There are 3 kinds of people those who can count and those who cant', 'There is no place like localhost', 'There is nothing quite so permanent as a quick fix', 'Theres no test like production',],
            SKILL_NAME: 'Developer Quotes',
            GET_FACT_MESSAGE: "Here's your Quote: ",
            HELP_MESSAGE: 'You can say tell me a developer quote, or, you can say exit... What can I help you with?',
            HELP_REPROMPT: 'What can I help you with?',
            STOP_MESSAGE: 'Goodbye!',
        },
    },
    'en-US': {
        translation: {
            FACTS: ['Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live','All computers wait at the same speed', 'A misplaced decimal point will always end up where it will do the greatest damage', 'A good programmer looks both ways before crossing a one-way street', 'A computer program does what you tell it to do not what you want it to do', 'Intel Inside is a Government Warning required by Law', 'Common sense gets a lot of credit that belongs to cold feet', 'Chuck Norris doesnt go hunting Chuck Norris goes killing', 'Chuck Norris counted to infinity twice', 'C is quirky flawed and an enormous success', 'Beta is Latin for still doesnt work', 'ASCII stupid question get a stupid ANSI', 'Artificial Intelligence usually beats natural stupidity', 'Any fool can use a computer Many do', 'Hey It compiles Ship it', 'Hate cannot drive out hate only love can do that', 'Guns dont kill people Chuck Norris kills people', 'God is real unless declared integer', 'First solve the problem. Then write the code.', 'Experience is the name everyone gives to their mistakes', 'Every piece of software written today is likely going to infringe on someone elses patent', 'Computers make very fast very accurate mistakes', 'Computers do not solve problems they execute solutions', 'I have NOT lost my mindI have it backed up on tape somewhere', 'If brute force doesnt solve your problems then you arent using enough', 'It works on my machine', 'Java is in many ways C++??', 'Keyboard not found...Press any key to continue.', 'Life would be so much easier if we only had the source code.', 'Mac users swear by their Mac PC users swear at their PC', 'Microsoft is not the answer Microsoft is the question No is the answer', 'MS-DOS isnt dead it just smells that way', ' Only half of programming is coding The other 90% is debugging', ' Pasting code from the Internet into production code is like chewing gum found in the street', 'Press any key to continue or any other key to quit.', 'Profanity is the one language all programmers know best', 'The best thing about a boolean is even if you are wrong you are only off by a bit', 'The nice thing about standards is that there are so many to choose from', 'There are 3 kinds of people those who can count and those who cant', 'There is no place like localhost', 'There is nothing quite so permanent as a quick fix', 'Theres no test like production',],
            SKILL_NAME: 'Innovator and developer Quotes',
        },
    },
    'en-GB': {
        translation: {
            FACTS: ['Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live','All computers wait at the same speed', 'A misplaced decimal point will always end up where it will do the greatest damage', 'A good programmer looks both ways before crossing a one-way street', 'A computer program does what you tell it to do not what you want it to do', 'Intel Inside is a Government Warning required by Law', 'Common sense gets a lot of credit that belongs to cold feet', 'Chuck Norris doesnt go hunting Chuck Norris goes killing', 'Chuck Norris counted to infinity twice', 'C is quirky flawed and an enormous success', 'Beta is Latin for still doesnt work', 'ASCII stupid question get a stupid ANSI', 'Artificial Intelligence usually beats natural stupidity', 'Any fool can use a computer Many do', 'Hey It compiles Ship it', 'Hate cannot drive out hate only love can do that', 'Guns dont kill people Chuck Norris kills people', 'God is real unless declared integer', 'First solve the problem. Then write the code.', 'Experience is the name everyone gives to their mistakes', 'Every piece of software written today is likely going to infringe on someone elses patent', 'Computers make very fast very accurate mistakes', 'Computers do not solve problems they execute solutions', 'I have NOT lost my mindI have it backed up on tape somewhere', 'If brute force doesnt solve your problems then you arent using enough', 'It works on my machine', 'Java is in many ways C++??', 'Keyboard not found...Press any key to continue.', 'Life would be so much easier if we only had the source code.', 'Mac users swear by their Mac PC users swear at their PC', 'Microsoft is not the answer Microsoft is the question No is the answer', 'MS-DOS isnt dead it just smells that way', ' Only half of programming is coding The other 90% is debugging', ' Pasting code from the Internet into production code is like chewing gum found in the street', 'Press any key to continue or any other key to quit.', 'Profanity is the one language all programmers know best', 'The best thing about a boolean is even if you are wrong you are only off by a bit', 'The nice thing about standards is that there are so many to choose from', 'There are 3 kinds of people those who can count and those who cant', 'There is no place like localhost', 'There is nothing quite so permanent as a quick fix', 'Theres no test like production',],
            SKILL_NAME: 'Innovator and developer Quotes',
        },
    },
    'de': {
        translation: {
            FACTS: [
                'Ein Jahr dauert auf dem Merkur nur 88 Tage.',
                'Die Venus ist zwar weiter von der Sonne entfernt, hat aber höhere Temperaturen als Merkur.',
                'Venus dreht sich entgegen dem Uhrzeigersinn, möglicherweise aufgrund eines früheren Zusammenstoßes mit einem Asteroiden.',
                'Auf dem Mars erscheint die Sonne nur halb so groß wie auf der Erde.',
                'Die Erde ist der einzige Planet, der nicht nach einem Gott benannt ist.',
                'Jupiter hat den kürzesten Tag aller Planeten.',
                'Die Milchstraßengalaxis wird in etwa 5 Milliarden Jahren mit der Andromeda-Galaxis zusammenstoßen.',
                'Die Sonne macht rund 99,86 % der Masse im Sonnensystem aus.',
                'Die Sonne ist eine fast perfekte Kugel.',
                'Eine Sonnenfinsternis kann alle ein bis zwei Jahre eintreten. Sie ist daher ein seltenes Ereignis.',
                'Der Saturn strahlt zweieinhalb mal mehr Energie in den Weltraum aus als er von der Sonne erhält.',
                'Die Temperatur in der Sonne kann 15 Millionen Grad Celsius erreichen.',
                'Der Mond entfernt sich von unserem Planeten etwa 3,8 cm pro Jahr.',
            ],
            SKILL_NAME: 'Weltraumwissen auf Deutsch',
            GET_FACT_MESSAGE: 'Hier sind deine Fakten: ',
            HELP_MESSAGE: 'Du kannst sagen, „Nenne mir einen Fakt über den Weltraum“, oder du kannst „Beenden“ sagen... Wie kann ich dir helfen?',
            HELP_REPROMPT: 'Wie kann ich dir helfen?',
            STOP_MESSAGE: 'Auf Wiedersehen!',
        },
    },
};

const handlers = {
    'LaunchRequest': function () {
        this.emit('GetQuotes');
    },
    'GetNewFactIntent': function () {
        this.emit('GetQuotes');
    },
    'GetQuotes': function () {
        // Get a random space fact from the space facts list
        // Use this.t() to get corresponding language data
        const factArr = this.t('FACTS');
        const factIndex = Math.floor(Math.random() * factArr.length);
        const randomFact = factArr[factIndex];

        // Create speech output
        const speechOutput = this.t('GET_FACT_MESSAGE') + randomFact;
        this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), randomFact);
    },
    'AMAZON.HelpIntent': function () {
        const speechOutput = this.t('HELP_MESSAGE');
        const reprompt = this.t('HELP_MESSAGE');
        this.emit(':ask', speechOutput, reprompt);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', this.t('STOP_MESSAGE'));
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', this.t('STOP_MESSAGE'));
    },
};

exports.handler = function (event, context) {
    const alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    // To enable string internationalization (i18n) features, set a resources object.
    alexa.resources = languageStrings;
    alexa.registerHandlers(handlers);
    alexa.execute();
};
