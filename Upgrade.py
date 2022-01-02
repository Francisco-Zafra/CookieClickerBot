class Upgrade:
    def __init__(self, Driver) -> None:
        self.DRIVER = Driver

    def buyUnlockedNotBought(self):
        idsFunc = 'return Game.UpgradesById.filter(x => x.bought == 0 && x.unlocked == 1).sort((x,y) => (x.basePrice > y.basePrice)?1:-1).map(x => x.id)'
        for i in self.DRIVER.execute_script(idsFunc):
            canBuy = self.DRIVER.execute_script(f'return Game.UpgradesById[{i}].canBuy()')
            if canBuy:
                self.DRIVER.execute_script(f'Game.UpgradesById[{i}].buy()')
            else:
                break

