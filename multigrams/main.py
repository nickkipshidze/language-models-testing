import random

class Multigrams:
    def __init__(self, dataset_file: str) -> None:
        print(f"[Multigrams] Reading '{dataset_file}';")

        self.dataset: list = \
            open(dataset_file, "r").read().lower().split(" ")

        print(f"[Multigrams] Dataset initialized;")
    
    def generate_multigram(self, group_size: int) -> dict:
        print(f"[Multigrams] Generating multigram, {group_size=};")

        multigram: dict = {}

        # Create a multigram
        for index in range(len(self.dataset)):
            group = self.dataset[index:index + group_size]

            # If we hit the end of the dataset
            if len(group) < group_size: break
            
            if " ".join(group[:-1]) in multigram:
                multigram[
                    " ".join(group[:-1])
                ].append(index)

            else:
                multigram[
                    " ".join(group[:-1])
                ] = [index]
        
        # Clean dict from empty values
        self.multigram: dict = {key: value for key, value in multigram.items() if value}
        self.group_size: int = group_size
        
        print("[Multigrams] Multigram generated;")

        return self.multigram
    
    def generate_next(self, params: list) -> str:
        # Convert list to string

        params: str = " ".join(
            params[-(self.group_size - 1):]
        )

        if params in self.multigram:
            # If the parameters were found in multigram

            return self.dataset[
                random.choice(
                    self.multigram[params]
                ) + (self.group_size - 1)
            ]
        
        else:
            # If the parameters were not found in multigram

            return self.dataset[
                self.dataset.index(
                    params.split(" ")[-1]
                ) + 1
            ]
        
def main() -> None:
    multigram = Multigrams("./data.txt")
    multigram.generate_multigram(3)

    generation: list = input("\nPrompt: ").lower().split(" ")

    while generation[-1][-1] != ".":
        generation.append(multigram.generate_next(generation))

    print(" ".join(generation))

if __name__ == "__main__":
    main()