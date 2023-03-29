class Television:
  def __init__(self, size) -> None:
    self.__volume: int = 50
    self.__chanel: int = 1
    self.__size: int or str = size
    self.__is_on: bool = False

  def volume_up(self) -> None:
    if (self.__volume < 99): self.__volume += 1

  def volume_down(self) -> None:
    if (self.__volume > 0): self.__volume -= 1

  @property
  def volume(self):
    return self.__volume

  def change_chanel(self, chanel) -> None:
    if (not chanel >= 1 and not chanel <= 99):
      raise ValueError("Valor incoretto de canal")
      
    self.__chanel = chanel
    
  def on_off(self) -> None:
    self.__is_on = not self.__is_on

  def __str__(self):
    return f"""
      -volume: {self.__volume}
      -chanel: {self.__chanel}
      -size: {self.__size}
      -is_on: {self.__is_on}
    """
