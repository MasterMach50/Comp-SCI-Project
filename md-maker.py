for i in range(1,21):
    with open(f"Record Program {i}.py") as f:
        lines = f.readlines()
    
    with open(f"Record Program {i}.md", "w") as f:
        chk_enabled = True
        first_line = True
        for line in lines:
            if chk_enabled:
                if line[0] == "#":
                    if first_line:
                        f.write("# "+line[2:])
                        first_line = False
                    else:
                        f.write(line[2:])
                else:
                    f.write("\n## Source Code\n```py\n")
                    chk_enabled = False
            else:
                f.write(line)

        f.write("```\n\n")
        f.write("## OUTPUT\n```\n\n```\n")
