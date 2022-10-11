from tqdm import tqdm



def find_dividers(n):
    dividers = []
    for i in tqdm(range(2, n)):
        if n % i == 0:
            dividers.append(i)
    print(dividers)
