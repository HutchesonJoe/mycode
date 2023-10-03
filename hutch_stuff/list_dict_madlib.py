word_types = ["noun1", "verb1", "adj1", "noun2"]

ui_dict = {}

for wt in word_types:
  user_input = input(f"Give me a {wt}:")
  ui_dict[wt] = user_input

for wt, answer in ui_dict.items():
  print("Word type: \n", wt, "user input: ", answer)
