class SushiPlatter():
    def __init__(self, salmon, tuna, shrimp, squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid
    
    @classmethod
    def lunch_special_A(cls):
        return cls(salmon=2, tuna=2, shrimp=2, squid=10)
    
    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0, tuna=10, shrimp=0, squid=1)

boris = SushiPlatter(salmon=8, tuna=4, squid=6, shrimp=10)

print(boris.shrimp, boris.salmon)

for atributo, valor in boris.__dict__.items():
    print(f"{atributo}: {valor}")

lunch_eater = SushiPlatter.lunch_special_A()

for atributo, valor in lunch_eater.__dict__.items():
    print(f"{atributo}: {valor}")

tuna_fan = SushiPlatter.tuna_lover()
for atributo, valor in tuna_fan.__dict__.items():
    print(f"{atributo}: {valor}")