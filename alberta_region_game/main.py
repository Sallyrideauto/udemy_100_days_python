from state_game import StateGame

game = StateGame(
    "alberta_map_clean.gif",
    "alberta_regions.csv",
    "alberta_regions_to_learn.csv"
)

game.run()