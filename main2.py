# this imports a predefined module from Python’s library, in this case the random module
import random

#this function takes prompts and takes  user input to find out their genre, this is done with a while loop #for continuous prompt until the user gives a valid genre. “lowercase_input = user_input.lower()” converts the user input to lower case so that it is not case sensitive
def get_user_input(genres):
  while True:
    print("Welcome to GameGenie!\n\nPlease enter your preferred genre:\n")
    user_input = input()
    lowercase_input = user_input.lower()

    if lowercase_input in genres:
      return lowercase_input
    else:
      print(
          "There seems to be a mistake. Could you please input a valid genre?\n\n\n")

# This search function will search through the genres in the predefined “genre” and “games” list and puts a limit on how many games will be selected for output
def search_genres(genre, games):
  genre_games = games.get(genre, [])
  return random.sample(genre_games, min(
      3, len(genre_games))) if genre_games else []

  #In this function, predefined lists of genres and games are created.then it invokes the user input function to validate the input stored in user_input. Based on this input, the function prints the appropriate message.

def main():
  genres = [
      "action", "crafting", "racing", "shooter", "mmo", "survival", 'strategy',
      'puzzle', 'fighting', "adventure", "rpg", "strategy", "simulation"
  ]
  games = {
      "action": [
          "God of War Ragnarök", "The Legend of Zelda: Breath of the Wild",
          "Red Dead Redemption 2", "Assassin's Creed Valhalla",
          "Spider-Man: Miles Morales", "Ghost of Tsushima",
          "Uncharted 4: A Thief's End", "Cyberpunk 2077",
          "Horizon Forbidden West", "The Witcher 3: Wild Hunt",
          "Resident Evil Village", "Sekiro: Shadows Die Twice"
      ],
      "crafting": [
          "Minecraft", "Stardew Valley", "Terraria", "Don't Starve Together",
          "Subnautica", "Valheim", "Factorio", "Ark: Survival Evolved", "Rust",
          "No Man's Sky", "The Forest", "Starbound"
      ],
      "adventure": [
          "The Last of Us Part II", "Uncharted: The Lost Legacy",
          "Life is Strange: True Colors", "Firewatch",
          "The Walking Dead: The Telltale Series",
          "Ori and the Will of the Wisps", "Journey", "Control",
          "Hellblade: Senua's Sacrifice", "Gris", "A Plague Tale: Innocence",
          "Night in the Woods"
      ],
      "racing": [
          "Forza Horizon 5", "Gran Turismo 7", "Mario Kart 8 Deluxe",
          "Need for Speed Heat", "F1 2021", "Dirt Rally 2.0", "Project CARS 3",
          "Assetto Corsa Competizione", "TrackMania Turbo", "Wreckfest",
          "Burnout Paradise Remastered", "The Crew 2"
      ],
      "shooter": [
          "Call of Duty: Modern Warfare", "Battlefield V", "Overwatch",
          "Destiny 2", "Counter-Strike: Global Offensive", "Rainbow Six Siege",
          "DOOM Eternal", "Borderlands 3", "Halo Infinite", "Titanfall 2",
          "Far Cry 6", "Apex Legends"
      ],
      "mmo": [
          "World of Warcraft", "Final Fantasy XIV", "The Elder Scrolls Online",
          "Guild Wars 2", "Black Desert Online", "Star Wars: The Old Republic",
          "EVE Online", "Runescape", "Albion Online", "New World", "Lost Ark",
          "Blade & Soul"
      ],
      "survival": [
          "The Long Dark", "Rust", "ARK: Survival Evolved", "Subnautica",
          "Don't Starve", "Conan Exiles", "The Forest", "State of Decay 2",
          "7 Days to Die", "Green Hell", "DayZ", "Stranded Deep"
      ],
      "strategy": [
          "StarCraft II", "Civilization VI", "XCOM 2",
          "Total War: Three Kingdoms", "Age of Empires II: Definitive Edition",
          "Crusader Kings III", "Europa Universalis IV", "Hearts of Iron IV",
          "Company of Heroes 2", "Stellaris", "Endless Legend",
          "Warcraft III: Reforged"
      ],
      "puzzle": [
          "The Witness", "Portal 2", "The Talos Principle", "Baba Is You",
          "Tetris Effect", "Monument Valley", "Inside", "LIMBO", "Fez",
          "Return of the Obra Dinn", "Gorogoa", "Braid"
      ],
      "fighting": [
          "Street Fighter V", "Tekken 7", "Mortal Kombat 11",
          "Super Smash Bros. Ultimate", "Dragon Ball FighterZ",
          "Guilty Gear -Strive-", "Injustice 2", "Soulcalibur VI",
          "BlazBlue: Cross Tag Battle", "Marvel vs. Capcom: Infinite",
          "Killer Instinct", "Samurai Shodown"
      ],
      "rpg": [
          "Elden Ring", "The Witcher 3: Wild Hunt", "Divinity: Original Sin 2",
          "Final Fantasy XV", "Persona 5 Royal", "Dragon Age: Inquisition",
          "Mass Effect: Legendary Edition", "Cyberpunk 2077",
          "Monster Hunter: World", "Pillars of Eternity", "Dark Souls III",
          "Baldur's Gate 3"
      ],
      "simulation": [
          "The Sims 4", "Cities: Skylines", "Microsoft Flight Simulator",
          "Stardew Valley", "Factorio", "Kerbal Space Program", "Planet Zoo",
          "Farming Simulator 19", "Euro Truck Simulator 2", "Railway Empire",
          "Two Point Hospital", "Surviving Mars"
      ]
  }
  user_genre = get_user_input(genres)
  recom = search_genres(user_genre, games)

  if recom:
    print(f"Try one of these from the {user_genre.title()} genre:\n")
    for game in recom:
      print(game)
  else:
    print(f"No games found in the {user_genre.title()} genre.")


if __name__ == "__main__":
  main()
