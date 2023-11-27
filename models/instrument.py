class Instrument:

  def __init__(self, name, instrument_type, displayName, 
               pipLocation, tradeUnitsPrecision, marginRate) -> None:
    self.name = name
    self.instrument_type = instrument_type
    self.displayName = displayName
    self.pipLocation = pow(10, pipLocation)
    self.tradeUnitsPrecision = tradeUnitsPrecision
    self.marginRate = float(marginRate)

  def __repr__(self) -> str:
    return str(vars(self))
  
  @classmethod
  def FromApiObject(cls, ob):
    return Instrument(
      ob['name'],
      ob['type'],
      ob['displayName'],
      ob['pipLocation'],
      ob['tradeUnitsPrecision'],
      ob['marginRate']
    )