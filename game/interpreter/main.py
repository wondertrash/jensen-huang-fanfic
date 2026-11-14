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
        if "[CHARACTER]" in content:
            reformat = re.split(r"(?<=\])\s*", content)
            reformat[2] = reformat[2].replace(": ", "")
            reformat[1] = re.sub(r"[\[\]]", "", reformat[1])
            character = characters[reformat[1].lower()]
            response = re.sub(r"[\[\]]", "", reformat[2])
            outfile.write(character + f" \"{response}\"\n")
        elif "[NARRATIVE]" in content:
            reformat = content.replace("[NARRATIVE]: ", "")
            reformat = re.sub(r"[\[\]]", "", reformat)
            outfile.write(f"\"{reformat}\"\n")
        elif "[SCENE CHANGE]" in content:
            reformat = content.replace("[SCENE CHANGE]: ", "")
            outfile.write(f"scene bg {reformat}\n")
        elif re.search(r"scene [a-z ]+", content):
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