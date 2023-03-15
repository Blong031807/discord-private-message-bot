import discord
#A module that contains all the functions and code necessary to run a discord bot
#DO NOT TURN THIS OFF







def run_discord_bot():
     TOKEN = "im not dumb enough to give everyone on the internet access to my bot"
  
     #what this does is tells discord that this is this specific bot

     intents = discord.Intents.all()
     intents.message_content = True
     client = discord.Client(intents=intents)
     #tells discord what this bot needs to be able to do for security reasons apparently, there are permission on the discord developer portal related to this
     #I gave it all intents because I intended to add more to this bot but then I actually realized I needed to write my IWA for AP Seminar and by the time I had freetime again had
     #an idea for a different project

     async def send_message(user_message): #this code has the bot send a the user_message (the message the user sent) to a specific channel
         try:
             messagechannel = client.get_channel(1058409572596989952)

             await messagechannel.send(user_message)
         except Exception as e:
             print(e)

     @client.event #tells me when the bot starts running in the console so I know if somethings wrong and
     #dont spend 12 hours trying to find out why its not messaging
     async def on_ready():
         print(f'{client.user} IS NOW RUNNING SIR!')

     @client.event #has it wait for the user to send something, has code to make sure the bot is
     #not the user, and then has it send whatever the user sent make
     async def on_message(message):
         if message.author == client.user:
             return

         user_message = str(message.content)
         channel = str(message.channel)

         if channel == 'Direct Message with Unknown User': #checks if the channel is with the bot
             print("asd") #for potential debugging purposes
             await send_message(user_message)


     client.run(TOKEN) #runs the bot

run_discord_bot() #runs the bot but as a function to make it neater and easier to build on
