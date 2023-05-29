import random, time

def generate_multigram(text: str, group_size: int) -> dict:
    words: list = list(text.lower().replace("\n", ""))
    multigram: dict = {}

    for index in range(len(words)):
        group = words[index:index+group_size]
        if len(group) < group_size: break

        if "".join(group[:-1]) in multigram:
            multigram["".join(group[:-1])].append(index)
        else:
            multigram["".join(group[:-1])] = []
    
    return {k: v for k, v in multigram.items() if v}

def main() -> None:
    text: str = open("./data.txt", "r").read()

    words: list = list(text.lower().replace("\n", ""))
    group_size: int = 50
    multigram: dict = generate_multigram(text, group_size)

    print("TEXT LENGTH    :", len(text))
    print("DATABASE WORDS :", len(words))
    print("NODES          :", len(multigram))
    input("")

    print("GENERATED:", end = " ")

    generation: list = []

    try:
        word: int = random.randint(len(words)//4, len(words))
        while word < len(words):
            print(words[word], end = "", flush = True)
            generation.append(words[word])

            if "".join(generation[-(group_size-1):]) in multigram:
                word = random.choice(multigram["".join(generation[-(group_size-1):])]) + (group_size - 2)
                time.sleep(0.1)
            
            word += 1
    except KeyboardInterrupt:
        print("\n\nStopping...")

if __name__ == "__main__":
    main()