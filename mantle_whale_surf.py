import requests, time

def mantle_surf():
    print("Mantle — Whale Just Surfed the BitDAO Treasury (> 500 ETH moved)")
    seen = set()
    while True:
        # Mantle mainnet — watching large native transfers
        r = requests.get("https://explorer.mantle.xyz/api?module=account&action=txlist"
                        "&address=0x0000000000000000000000000000000000000000&sort=desc")
        for tx in r.json().get("result", [])[:35]:
            h = tx["hash"]
            if h in seen: continue
            seen.add(h)

            value = int(tx["value"]) / 1e18
            if value >= 500:  # > 500 ETH on Mantle
                print(f"MANTLE WHALE JUST SURFED\n"
                      f"{value:,.1f} ETH moved on BitDAO L2\n"
                      f"From: {tx['from'][:12]}...\n"
                      f"To:   {tx['to'][:12]}...\n"
                      f"Tx: https://explorer.mantle.xyz/tx/{h}\n"
                      f"→ Probably BitDAO treasury, Bybit, or mega-institution\n"
                      f"→ Mantle fees < $0.001 — this is pure capital flow\n"
                      f"→ Someone is positioning for the next cycle\n"
                      f"{'-'*90}")
        time.sleep(2.7)

if __name__ == "__main__":
    mantle_surf()
