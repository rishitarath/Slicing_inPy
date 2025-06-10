def triple_to_list(start, stop, step):
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result

class RLE:
    def __init__(self, sequence):
        self.sequence = sequence

    def print_seq(self):
        print(self.sequence)

    def length(self):
        sum = 0
        for pair in self.sequence:
            sum += pair[0]
        return sum

    def get_element(self, n):
        if n >= 0 and n > self.length():
            raise IndexError('list index out of range')
        else:
            for (m,c) in self.sequence:
                if n < m:
                    return c
                else:
                    n = n - m

    def slice_to_triple(self, s):
        step = s.step if s.step is not None else 1
        # Calculate the full length of the sequence
        length = self.length()
   
         # Handle start
        if s.start is None:
            start = 0
        elif s.start < 0:
              start = length + s.start
        else:
              start = s.start
              # Handle stop
        if s.stop is None:
              stop = length
        elif s.stop < 0:
              stop = length + s.stop
        else:
              stop = s.stop

        return (start, stop, step)

    def get_slice(self, s):
        # Step 1: Convert the slice into a (start, stop, step) triple
        start, stop, step = self.slice_to_triple(s)
    
        # Step 2: Generate the list of indices to extract
        indices = triple_to_list(start, stop, step)

        # Step 3: Extract elements from the RLE sequence at those indices
        elements = [self.get_element(i) for i in indices]

        # Step 4: Reconstruct RLE from the elements
        if not elements:
            return RLE([])

        new_rle = []
        count = 1
        current_char = elements[0]

        for i in range(1, len(elements)):
            if elements[i] == current_char:
              count += 1
            else:
              new_rle.append((count, current_char))
              current_char = elements[i]
              count = 1
        new_rle.append((count, current_char))
        return RLE(new_rle)
        

# In get_slice, we:
# 1. Use slice_to_triple to handle None and negative values and get a usable (start, stop, step).
# 2. Use triple_to_list to get the list of indices to extract from the RLE sequence.
# 3. Use get_element to extract the values at those indices.
# 4. Rebuild a new RLE by compressing consecutive identical elements with their counts.


    def __getitem__(self, index):
        if isinstance(index, int):
            return self.get_element(index)
        elif isinstance(index, slice):
            return self.get_slice(index)
        

