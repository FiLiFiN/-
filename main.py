import discord
from discord.ext import commands
import random
from random import randint

bot = commands.Bot(command_prefix="/", intents = discord.Intents.all())

pet = {
    'health': 100,
    'defence': 1,
    'strenghth': 1
}

@bot.command('feed')
async def feed(message):
    pet['health'] +=10
    pet['defence'] +=10
    await message.send('Ваш питомец насытился!: ' + str(pet))

@bot.command('train')
async def train(message):
    pet['health'] -=5
    pet['defence'] +=5
    pet['strenghth'] +=10
    await message.send('Ваш питомец натренерован!: ' + str(pet))

@bot.command('fight')
async def fight(message):
    enemy = {
    'health': randint(1,100),
    'defence': randint(1,10),
    'strenghth': randint(1,10)
    }
    await message.send("БОЙ!!!")
    while enemy["health"] >= 0 and pet['health'] >= 0:
        pet["health"] -= enemy['strenght'] - pet['defence']
        enemy["health"] -= pet['strenght'] - enemy['defence']
        await message.send('Ваш питомец' + str(pet))
        await message.send('Ваш соперник' + str(enemy))
    if enemy['health'] > pet["health"]:
        await message.send('Вы проиграли')
    else:
        await message.send('Вы выиграли')
    
bot.run('MTIzODg1Mzg5NDY1MDcyNDU0NA.GGbbIb.hEnj7rzy4V9CLAQK6FM7t_d5Bd5BNcU6HVjjVk')
