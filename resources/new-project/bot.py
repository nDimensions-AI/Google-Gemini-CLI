import discord
import os

# Function to load FAQs from the markdown file
def load_faqs(file_path):
    faqs = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    question = None
    answer = ""
    for line in lines:
        if line.startswith('###'):
            if question:
                faqs[question.strip()] = answer.strip()
            question = line.strip().replace('###', '').strip()
            answer = ""
        elif question:
            answer += line
    if question:
        faqs[question] = answer.strip()
    return faqs

# Load the FAQs
faq_file = 'FAQ.md'
faqs = load_faqs(faq_file)
questions_list = list(faqs.keys())

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!faq'):
        # Send the list of questions if the user just types !faq
        if len(message.content.split()) == 1:
            response = "Here are the questions I can answer:\n"
            for i, q in enumerate(questions_list, 1):
                response += f"{i}. {q}\n"
            response += "\nType `!faq <question>` to get an answer."
            await message.channel.send(response)
            return

        # Find and send the answer to a specific question
        user_question = message.content[5:].strip().lower()
        best_match = None
        highest_score = 0

        # Simple keyword matching to find the best answer
        for q in questions_list:
            score = 0
            for word in user_question.split():
                if word in q.lower():
                    score += 1
            if score > highest_score:
                highest_score = score
                best_match = q
        
        if best_match:
            await message.channel.send(f"**{best_match}**\n{faqs[best_match]}")
        else:
            await message.channel.send("Sorry, I couldn't find an answer to that question. Type `!faq` to see the list of available questions.")

# Get the bot token from an environment variable
bot_token = os.environ.get('DISCORD_BOT_TOKEN')

if not bot_token:
    print("Error: DISCORD_BOT_TOKEN environment variable not set.")
    print("Please set the DISCORD_BOT_TOKEN environment variable with your bot's token.")
else:
    client.run(bot_token)