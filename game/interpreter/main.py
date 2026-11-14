import re

name = input("Input the name of the file you want to convert. ")

characters = {
    "jensen": "jh",
    "lisa": "ls",
    "alice": "ah",
    "lori": "lh",
    "dealer": "dd",
}

with open(f"game/raw/{name}.md", "r", encoding="utf-8") as file, \
    open(f"game/SCRIPT/{name}.rpy", "w", encoding="utf-8") as outfile:

    for line in file:
        content = line.strip()
        if re.search(r"scene [a-z ]+", content):
            reformat = re.sub(r"[\(\)]", "", content)
            reformat = reformat.replace("scene", "scene bg")
            outfile.write(f"{reformat}\n")
        elif ":" not in content:
            if content == "":
                outfile.write(f"{content}\n")
            else:
                outfile.write(f"\"{content}\"\n")
        elif "decision" in content:
            reformat = content.replace("decision: ", "")
            outfile.write(f"\"{reformat}\"\n")
        elif re.search(r"[a-z ]+: [a-z ]+", content):
            dialogue = content.split(": ")
            person = characters[dialogue[0].lower()]
            outfile.write(f"{person} \"{dialogue[1]}\"\n")