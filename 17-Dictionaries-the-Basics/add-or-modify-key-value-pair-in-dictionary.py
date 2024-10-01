sports_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

# print(sports_team_rosters["Pittsburgh Steelers"]) KeyError

sports_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]

print(sports_team_rosters["Pittsburgh Steelers"])
print()

print(sports_team_rosters)

sports_team_rosters["New York Giants"] = ["Eli Manning"]

print()

print(sports_team_rosters)


video_game_options = {}
video_game_options = dict()

video_game_options["subtitles"] = True
video_game_options["difficulty"] = "Medium"
video_game_options["volume"] = 7
print()
print(video_game_options)
video_game_options["subtitles"] = False
video_game_options["difficulty"] = "Hard"
print()
print(video_game_options)
print()

words = ["danger", "beware", "danger", "danger"]

def count_words(words):
    counting = {}
    for word in words:
        if word not in counting:
            counting[word] = 1
        else:
            counting[word] += 1
    print(counting)

count_words(words)