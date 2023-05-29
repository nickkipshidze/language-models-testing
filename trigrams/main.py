import random, time

def generate_trigram(text: str) -> dict:
    words: list = text.lower().replace("\n", "").split(" ")
    trigram: dict = {}

    for index in range(len(words)):
        triplet = words[index:index+3]
        if len(triplet) < 3: break

        if " ".join(triplet[:-1]) in trigram:
            trigram[" ".join(triplet[:-1])].append(index)
        else:
            trigram[" ".join(triplet[:-1])] = []
    
    return trigram

def main() -> None:
    text: str = open("./data.txt", "r").read()

    words: list = text.lower().replace("\n", "").split(" ")
    trigram: dict = generate_trigram(text)

    print("TEXT LENGTH    :", len(text))
    print("DATABASE WORDS :", len(words))
    print("NODES          :", len(trigram))
    input("")

    print("GENERATED:", end=" ")

    generation: list = []

    try:
        word: int = random.randint(len(words)//4, len(words))
        while word < len(words):
            print(words[word], end = " ", flush = True)
            generation.append(words[word])

            if " ".join(generation[-2:]) in trigram:
                if trigram[" ".join(generation[-2:])]:
                    word = random.choice(trigram[" ".join(generation[-2:])]) + 1
                    time.sleep(0.1)
            
            word += 1
    except KeyboardInterrupt:
        print("\n\nStopping...")

if __name__ == "__main__":
    main()