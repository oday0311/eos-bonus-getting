import os
import json
from log import loggingSetting
from ut import pushaction, unlock, getAccounts

logger = loggingSetting("airdrop")


def main(password):
    x = getAccounts()
    unlock(password)
    for i in x[:1]:
        print(
            pushaction("betdicetoken", "signup", [i, "1000.0000 DICE"], i)
        )  # 1000dice
        # print(
        #     pushaction("xxxsevensxxx", "signup", [i, "10000.0000 SEVEN"], i) # 10000 SEVEN
        # )
        # print(pushaction("efinitysicbo", "claim", [i], i))  # 100 CHIPS


if __name__ == "__main__":
    password = ""
    main(password)
