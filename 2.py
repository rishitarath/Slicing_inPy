class PizzaQueue:
    def __init__(self, hunger_list, slices):
        # Store original order
        self.hunger_list = list(hunger_list)  # Don't sort if you want original order
        self.slices = slices
        self.current_index = 0
        self.slice_number = 1

    def eat(self, n):
        if self.slices == 0 or all(h == 0 for _, h in self.hunger_list):
            return None

        name, hunger = self.hunger_list[n]

        if hunger > 0:
            self.hunger_list[n] = (name, hunger - 1)
            self.slices -= 1

        # Find next hungry person
        total = len(self.hunger_list)
        for i in range(1, total + 1):
            next_index = (n + i) % total
            if self.hunger_list[next_index][1] > 0:
                return next_index

        # If no one is hungry anymore
        return None

    def __iter__(self):
        self.current_index = 0
        self.slice_number = 1
        return self

    def __next__(self):
        if self.slices == 0 or all(h == 0 for _, h in self.hunger_list):
            raise StopIteration

        # Feed current person
        name, hunger = self.hunger_list[self.current_index]
        if hunger > 0:
            self.hunger_list[self.current_index] = (name, hunger - 1)
            self.slices -= 1
            result = (name, self.slice_number)
            self.slice_number += 1
        else:
            # Skip to next
            for i in range(1, len(self.hunger_list)):
                next_index = (self.current_index + i) % len(self.hunger_list)
                if self.hunger_list[next_index][1] > 0:
                    self.current_index = next_index
                    return self.__next__()
            raise StopIteration

        # Advance to next hungry student
        for i in range(1, len(self.hunger_list) + 1):
            next_index = (self.current_index + i) % len(self.hunger_list)
            if self.hunger_list[next_index][1] > 0:
                self.current_index = next_index
                break

        return result

hunger_list = [ ("Bart",   5)
              , ("Lisa",   2)
              , ("Homer",  9)
              , ("Marge",  3)
              , ("Maggie", 2)
              ]

pq = PizzaQueue(hunger_list, 30)
print("Testing with 30 slices:")
for x in pq:
    print(x)

# Second test: with 10 slices
pq = PizzaQueue(hunger_list, 10)
print("\nTesting with 10 slices:")
for x in pq:
    print(x)
