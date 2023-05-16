class MainMemory:
  def __init__(self):
      self.clean()

  def load(self, value):
      self.loaded_memory.append(value)

  def get(self, index):
      return float(self.loaded_memory[index])

  def clean(self):
      self.loaded_memory = []