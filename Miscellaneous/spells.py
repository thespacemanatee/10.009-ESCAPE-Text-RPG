class Hero:
	def __init__(self, name, intel, strength, agi):
		self.name = name
		self.intel = intel
		self.strength = strength
		self.agi = agi
		self.hp = strength * 2
		self.alive = True

    def isDead(self):
        return not self.alive

    def getStats(self):
        return self.hp, self.intel, self.strength, self.agi

    def attack(self):
        if self.alive:
            return self.agi * 0.77
        else:
            return 0

    def defend(self, damage):
        self.hp = self.hp - damage
        if (self.hp < 0):
            print("{0} is dead and lost!".format(self.name))
            self.alive = False
        print("{0} received {1:.3f} damage, current HP is: {2:.3f}".format(
            self.name, damage, self.hp))


class Cast:
    def __init__(self, damage):
        self.damage = damage

    def cast(self, intel):
        return self.damage + intel * 1.05

class Physical(Cast):
    def __init__(self, warrior_damage):
        self.type = "PHYSICAL"
        super().__init__(physical_damage)


class Magical(Cast):
    def __init__(self, mage_damage):
        self.type = "MAGICAL"
        super().__init__(magical_damage)

# class Priest(Cast):
#     def __init__(self, priest_damage):
#         self.type = "PRIEST"
#         super().__init__(priest_damage)

# class SupernovaSpell(FireSpell):
#     def __init__(self, fire_damage):
#         super().__init__(fire_damage * 1.5)

#     def cast(self, intel):
#         original_damage = super().cast(intel)
#         # critical hit
#         return original_damage * (float(random.randint(1, 10))/10 + 1)

class Vest:
    def __init__(self, strength):
        self.damageReduction = strength * 0.11

    def receiveDamage(self, incoming_damage):
        if (incoming_damage < self.damageReduction):
            return 0
        else:
            return incoming_damage - self.damageReduction

class Shield:
    def __init__(self, strength):
        self.damageBlockProbability = 0.1

    def blockDamage(self, incoming_damage):
        blockDamage = False
        if (random.randint(1, 1/self.damageBlockProbability) == 0):
            return 0
        else:
            return incoming_damage

class Armor(Shield, Vest):
    def __init__(self, strength):
        Shield.__init__(self, strength)
        Vest.__init__(self, strength)

    def receiveDamage(self, incoming_damage, spell_type):
        blocked_damage = Shield.blockDamage(self, incoming_damage)
        if spell_type == "PHYSICAL":
            return Vest.receiveDamage(self, incoming_damage) * 0.5
        else:
            return Vest.receiveDamage(self, incoming_damage)


class MagicResist(Shield, Vest):
    def __init__(self, strength):
        Shield.__init__(self, strength)
        Vest.__init__(self, strength)

    def receiveDamage(self, incoming_damage, spell_type):
        blocked_damage = Shield.blockDamage(self, incoming_damage)
        if spell_type == "MAGICAL":
            return Vest.receiveDamage(self, incoming_damage) * 0.5
        else:
            return Vest.receiveDamage(self, incoming_damage)

### Composition and Inheritance ###
class Wizard(Player):
    def __init__(self, name, stats):
        intel, hp, strength, agi, spell_type = stats
        super().__init__(name, hp, intel, strength, agi)
        if (spell_type == "PHYSICAL"):
            self.shield = Armor(self.strength)
            self.spell = Physical(self.intel * 0.1)
        elif (spell_type == "MAGICAL"):
            self.shield = MagicResist(self.strength)
            self.spell = Magical(self.intel * 0.1)
        # elif (spell_type == "SUPERNOVA"):
        #     self.shield = FireArmor(self.strength)
        #     self.spell = SupernovaSpell(self.intel * 0.1)
        print("Wizard {0} is successfully instantiated.".format(self.name))

    def attack(self):
        base_damage = super().attack()
        magic_damage = self.spell.cast(self.intel)
        print("{0} attacks {1:.2f} damage".format(
            self.name, base_damage + magic_damage))
        return base_damage + magic_damage, self.spell.type

    def defend(self, input_event):
        raw_damage, spell_type = input_event
        reduced_damage = self.shield.receiveDamage(raw_damage, spell_type)
        super().defend(reduced_damage)