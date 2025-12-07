# TODO: Create a letter using invitation_letter.txt

# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()  # read names with list

# Replace the [name] placeholder with the actual name
with open("Input/Letters/invitation_letter.txt") as letter_file:
    letter_contents = letter_file.read()

# Save the letters in the folder "ReadyToSend"
for name in names:
    stripped_name = name.strip()    # delete line change

    # change [name] to actual name
    new_letter = letter_contents.replace("[name]", stripped_name)

    # save files
    output_path = f"Output/ReadyToSend/invitation_for_{stripped_name}.txt"
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(new_letter)

    print(f"Created: {output_path}")