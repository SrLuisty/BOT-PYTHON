import discord
import asyncio
import random
import time
import re
import datetime

client = discord.Client()
players = {}

COR =0xFF0000
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('-------$rLuis-------')   

qntdd = int

def toint(s):
    try:
        return int(s)
    except ValueError:
        return float(s)

@client.event
async def on_message(message):

    if message.content.lower().startswith('ra!delete'):
            qntdd = message.content.strip('ra!delete ')
            qntdd = toint(qntdd)
            if qntdd <= 500:
                msg_author = message.author.mention
                await client.delete_message(message)
                #await asyncio.sleep(1)
                deleted = await client.purge_from(message.channel, limit=qntdd)
                botmsgdelete = await client.send_message(message.channel, 'Deletei {} mensagens.'.format(len(deleted), qntdd, msg_author))
                await asyncio.sleep(5)
                await client.delete_message(botmsgdelete)

            else:
                botmsgdelete = await client.send_message(message.channel,'Utilize o comando digitando ra!delete <numero de 1 a 500>')
                await asyncio.sleep(5)
                await client.delete_message(message)
                await client.delete_message(botmsgdelete)        

    if message.content.startswith('ra!serverinfo'):
        
        user = message.author.name
        
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        
        serverinfo_embed = discord.Embed(title="\n", description="Abaixo está as informaçoes principais do servidor!", color=COR)
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)
        serverinfo_embed.set_footer(text="{} • {}".format(user, horario))
        serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)
        serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)
        serverinfo_embed.add_field(name="ID:", value=message.server.id, inline=True)
        serverinfo_embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        serverinfo_embed.add_field(name="Canais de texto:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.text]), inline=True)
        serverinfo_embed.add_field(name="Canais de voz:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.voice]), inline=True)
        serverinfo_embed.add_field(name="Membros:", value=len(message.server.members), inline=True)
        serverinfo_embed.add_field(name="Bots:", value=len([user.mention for user in message.server.members if user.bot]), inline=True)        
        serverinfo_embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"), inline=True)
        serverinfo_embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        await client.send_message(message.channel,embed=serverinfo_embed)

    if message.content.startswith('ra!userinfo'):       
            
            user = message.author.name
            
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            
            userinfo_embed = discord.Embed(title="\n", description="Abaixo está as informaçoes do usuario!", color=COR)
            userinfo_embed.set_thumbnail(url=message.author.avatar_url)
            userinfo_embed.set_footer(text="{} • {}".format(user, horario))            
            userinfo_embed.add_field(name="Nome:", value=message.author.name, inline=True)
            userinfo_embed.add_field(name='Apelido', value=message.author.nick, inline=True)
            userinfo_embed.add_field(name="ID:", value=message.author.id, inline=True)
            userinfo_embed.add_field(name="Cargos:", value=len(message.author.roles), inline=True)
            userinfo_embed.add_field(name="Status:", value=message.author.status, inline=True)
            userinfo_embed.add_field(name='Jogando:', value=message.author.game, inline=True)                    
            userinfo_embed.add_field(name="Criou a conta em:", value=message.author.created_at.strftime("%d %b %Y %H:%M"), inline=True) 
            userinfo_embed.add_field(name="Entrou no servirdor em:", value=message.author.joined_at.strftime("%d %b %Y %H:%M"), inline=True)        
            await client.send_message(message.channel, embed=userinfo_embed)                     

    

    if message.channel == client.get_channel('447716248000659457'):
            await client.add_reaction(message, "👍")
            await client.add_reaction(message, "👎")
    
    if message.content.lower().startswith('ra!teste'):   
        await client.send_message(message.channel, "Seu teste foi concluido com sucesso!")
    
    if message.content.lower().startswith('ra!moeda'):
      choice = random.randint(1,2)
      if choice == 1:
          await client.add_reaction(message, '😁')
      if choice == 2:
          await client.add_reaction(message, '👑')
          
    if message.content.lower().startswith('ra!ping'):
        timep = time.time()
        emb = discord.Embed(title = 'Aguarde...', color = COR)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        pingm1 = discord.Embed(title = 'Pong!', description = ':ping_pong: Ping - %.01f segundos' % ping, color=COR)
        await client.edit_message(pingm0, embed=pingm1)

    if message.content.startswith('ra!jogando') and message.author.id == "403345462876438548":
        game = message.content[11:]
        await client.change_presence(game=discord.Game(name=game))
        await client.send_message(message.channel, ":video_game: Mudando o status para: "+game+"")

    if message.content.lower().startswith('ra!convite'):
        embedconvite = discord.Embed(
            title="**----Convite----**",
            color=COR,
            description=":blue_heart: Me convide para seu servidor\n"
                        "Invite do BOT\n"
                        "https://goo.gl/8g13HD")    
        embedconvite.set_footer(text="By: $rLuis#8506")
        message =await client.send_message(message.channel, embed=embedconvite, content=message.author.mention)


    if message.content.lower().startswith('ra!help'):
        
        await client.add_reaction(message, '📩')

        embedhelp = discord.Embed(
            title="**----Ajuda----**",
            color=COR,
            description="Aqui vai meus comandos :mailbox_with_mail:!\n"
                        " \n"
                        "**Eu ainda estou em desenvolvimento mais tenho esses comandos que de alguma forma o ajudará**\n"                         
                        "`COMANDOS DE DIVERSÃO`\n"
                        "ra!moeda  | Cairá cara ou coroa\n"
                        "ra!help  | Irei lhe enviar essa mensagem de **Help**.\n"
                        "ra!avatar  | Irei lhe mandar o avatar do usuario mencionado.\n"
                        "ra!ping  | Irei mostrar seu ping.\n"
                        "ra!serverinfo | Irei mostrar as informações do servidor.\n"
                        "ra!userinfo | Irei mostrar as informações do usuario que usou o comando.\n"
                        "ra!teste | Ira mostrar seu eu estou funcionado no seu servidor.\n"
                        "ra!convite | Irei lhe enviar o meu convite para eu entrar no seu servidor.\n"
                        " \n"
                        "`COMANDOS DE MODERAÇÃO`\n"
                        "ra!ban | Ira banir o usuario marcado.\n"
                        "ra!mutar | Ira mutar o usuario citado.\n"
                        "ra!desmutar | Ira desmutar o usuario citado.\n"
                        "ra!delete | Escolha a quantidade de mensagens que deseja excluir <messagens 1 a 500>\n",)
        embedhelp.set_footer(text="By: $rLuis#8506")
        message =await client.send_message(message.author, embed=embedhelp, content=message.author.mention)
    
    if message.content.lower().startswith('ra!avatar'):
        try:
            usuario = message.mentions[0]
            avatarembed = discord.Embed(
                title="",
                color=COR,
                description="**[Clique aqui]("+ usuario.avatar_url +") para baixar o avatar de {}!**".format(usuario.name))
            avatarembed.set_author(name=message.author.name)
            avatarembed.set_image(url=usuario.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)
        except:
            avatarembed = discord.Embed(
                title="",
                color=COR,
                description="**[Clique aqui]("+ message.author.avatar_url +") para baixar seu avatar!**")
            avatarembed.set_author(name=message.author.name)
            avatarembed.set_image(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)

    if message.content.lower().startswith("ra!ban"):
      try:
        role = discord.utils.get(message.server.roles, name='Admin')
        if not role in message.author.roles:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        user = message.mentions[0]
        await client.ban(user)
        await client.send_message(message.channel,"Usuario: {} banido do server.".format(user.mention))
       #no caso do membro mencionado ser um adm vai enviar uma messagem
      except  discord.errors.Forbidden:
          return await client.send_message(message.channel, '⚠️ Nao posso banir o administrador :{}'.format(user.mention))



    if message.content.lower().startswith("ra!mutar"):
        role = discord.utils.get(message.server.roles, name='Admin')
        if not role in message.author.roles:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        user = message.mentions[0]

        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.add_roles(user, cargo)
        await client.send_message(message.channel, 'O membro: {} foi mutado.'.format(user.mention))

    if message.content.lower().startswith("ra!desmultar"):
        role = discord.utils.get(message.server.roles, name='Admin')
        if not role in message.author.roles:
            return await client.send_message(message.channel, '⚠️Permissão insuficiente')
        user = message.mentions[0]
        cargo = discord.utils.get(message.author.server.roles, name='Mutado')
        await client.remove_roles(user, cargo)
        await client.send_message(message.channel, 'O membro: {} foi Desmultado.'.format(user.mention))

   
    
    elif message.content.lower().startswith("ra!ex") and message.author.id == "403345462876438548":
        try:
            await client.send_message(message.channel, str(eval(message.content[6:])))
        except Exception as e:
            await client.send_message(message.channel, repr(e))
     
    if message.content.lower().startswith("ra!cargos") and message.author.id == "403345462876438548":

     embed1 =discord.Embed(

        title="Escolha seu cargo!",
        color=COR,
        description="- Selecione os jogos que você joga!\n"
                    " \n"
                    "- FORTINITE = ⏩\n"
                    " \n"
                    "- MINECRAFT =  ⏫\n"
                    " \n"
                    "- GTA SAMP  = ⏬\n"
                    " \n"
                    "- +18 = ⏪",)
     botmsg = await client.send_message(message.channel, embed=embed1)

     await client.add_reaction(botmsg, "⏩")
     await client.add_reaction(botmsg, "⏫")
     await client.add_reaction(botmsg, "⏬")
     await client.add_reaction(botmsg, "⏪")

     global msg_id
     msg_id = botmsg.id
     global msg_user
     msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    
    msg = reaction.message
#Lembrado que tem que te o cargo no seu servidor    
    if reaction.emoji == "⏩" and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "FORTINITE", msg.server.roles)
     await client.add_roles(user, role)


    if reaction.emoji == "⏪"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "+18", msg.server.roles)
     await client.add_roles(user, role)

    if reaction.emoji == "⏫"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "MINECRAFT", msg.server.roles)
     await client.add_roles(user, role)


    if reaction.emoji == "⏬"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "GTA SAMP", msg.server.roles)
     await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "⏩" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "FORTINITE", msg.server.roles)
     await client.remove_roles(user, role)
     print("Uma role foi retira pelo recrutamento")

    if reaction.emoji == "⏪" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "+18", msg.server.roles)
     await client.remove_roles(user, role)
     print("Uma role foi retira pelo recrutamento")

    if reaction.emoji == "⏫"and msg.id == msg_id: #and user == msg_user :
     role = discord.utils.find(lambda r: r.name == "MINECRAFT", msg.server.roles)
     await client.remove_roles(user, role)
     print("Uma role foi retira pelo recrutamento")

    if reaction.emoji == "⏬" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "GTA SAMP", msg.server.roles)
     await client.remove_roles(user,role)
     print("Uma role foi retira pelo recrutamento")        


client.run('TOKEN')