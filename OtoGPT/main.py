import random, time

def count_words(text: str) -> dict:
    frequency: dict = {}
    words: list = text.lower().split(" ")

    for index, word in enumerate(words):
        if words.count(word) > 1:
            if word in frequency:
                frequency[word].append(index)
            else:
                frequency[word] = [index]
    
    return frequency

def generate_preview(content: str) -> None:
    preview_dir: str = "./preview"
    template: str = open(f"{preview_dir}/layout.html", "r").read()
    
    index: str = template.replace("{{ content }}", content)

    open(f"{preview_dir}/index.html", "w").write(index)

def main() -> None:
    text: str = open("./text.txt", "r").read()

    words: list = text.lower().split(" ")
    frequency: dict = count_words(text)

    print("TEXT LENGTH    :", len(text))
    print("DATABASE WORDS :", len(words))
    print("NODES          :", len(frequency))
    input("")

    print("GENERATED:", end=" ")

    generation: str = ""

    try:
        word: int = random.randint(len(words)//4, len(words))
        while word < len(words):
            print(words[word], end = " ", flush = True)
            generation += words[word] + " "

            if words[word] in frequency:
                word = random.choice(frequency[words[word]])
                time.sleep(0.1)
            
            word += 1
    except KeyboardInterrupt:
        print("\n\nStopping...")
    
    generate_preview(generation)

if __name__ == "__main__":
    main()