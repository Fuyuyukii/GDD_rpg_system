from base.Constructor import constructor
from completed.Player import player
from completed.Party import party

dkz = constructor(party)
dkz.party_name = "Dark Kingdom"

yuki = constructor(player)
yuki.name = "Yuki"
yuki.party = dkz

