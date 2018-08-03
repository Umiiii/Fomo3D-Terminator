import fomo3d
import config
import time
from util import *


def loop():
    while True:
        time.sleep(5)
        data = fomo3d.get_current_round_info()
        winner_address = data[7]
        fomo3d.print_current_info(data)
        left_time = fomo3d.get_time_left()
        log("Left time "+str(left_time) +" seconds")
        if left_time < config.RUSH_SECONDS:
            if winner_address == config.ADDRESS:
                log("You are holding the last key!")
                log("All your pots are belong to us.")
            else:
                log("Seems like "+winner_address+" try to steal your pots!")
                log("Let's get him down.")
                txid = fomo3d.buy_key()
                fomo3d.get_tx_result(txid)
        else:
            time.sleep(10)
            log("It's not time yet. Your time setting is : "+str(config.RUSH_SECONDS)+" seconds")



if __name__ == "__main__":
    loop()