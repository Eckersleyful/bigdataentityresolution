class Structure:

    def __init__(self, key_value_pairs):
        self._key_value_pairs = key_value_pairs

    
    def get_key_value_pairs(self):
        return self._key_value_pairs


    def set_similar_attribute(self, pair_tuple):
        self._pair_tuple = pair_tuple