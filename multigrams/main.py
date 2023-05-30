import random, time

class Multigrams:
    def __init__(self, dataset_file: str) -> None:
        print(f"[Multigrams] Reading '{dataset_file}';")

        self.dataset: list = \
            open(dataset_file, "r").read().lower().replace("\n", "").split(" ")

        print(f"[Multigrams] Dataset initialized;")
    
    def generate_multigram(self, group_size: int) -> dict:
        print(f"[Multigrams] Generating multigram, {group_size=};")

        self.multigram: dict = {}
        self.group_size: int = group_size

        # Create a multigram
        for index in range(len(self.dataset)):
            group = self.dataset[index:index + group_size]

            # If we hit the end of the dataset
            if len(group) < group_size: break
            
            if " ".join(group[:-1]) in self.multigram:
                self.multigram[
                    " ".join(group[:-1])
                ].append(group[-1])

            else:
                self.multigram[
                    " ".join(group[:-1])
                ] = [group[-1]]
        
        print("[Multigrams] Multigram generated;")

        return self.multigram
    
    def generate_next(self, params: list) -> str:
        # Convert list to string

        # Potential key in multigram
        params: str = " ".join(
            params[-(self.group_size - 1):]
        )

        if params in self.multigram:
            # If the parameters were found in multigram
            
            # Example of self.multigram:
            #     self.multigram = {"parameter1 parameter2": ["parameter3", "parameter2.5"]}

            return random.choice(
                self.multigram[params]
            )        
        else:
            # If the parameters were not found in multigram

            # Find any occurrence of the last parameter and return word after it
            return self.dataset[
                self.dataset.index(
                    params.split(" ")[-1]
                ) + 1
            ]
        
def main() -> None:
    multigram = Multigrams("./data.txt")
    multigram.generate_multigram(3)

    generation: list = input("\nPrompt: ").lower().split(" ")

    print(" ".join(generation), end = " ")
    while generation[-1][-1] != ".":
        generation.append(multigram.generate_next(generation))
        print(generation[-1], end = " ", flush = True)
        time.sleep(0.1)

    print("\n")

if __name__ == "__main__":
    main()