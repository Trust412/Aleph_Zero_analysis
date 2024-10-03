import csv

def save_pool_data_to_csv(filename='aleph_zero_pools.csv'):
    # Define the data for all 96 pools
    data = [
        [1, "GATOTECH😸 Top tech decentralisation 🌐gatotech.uk/pools", 561868.82, 16296.363, 1, 520, "Open"],
        [2, "AZF/Banach pool", 152579.725, 6716.822, 1, 197, "Open"],
        [3, "AZF/Turing pool", 167178.296, 5489.215, 1, 216, "Open"],
        [4, "AZF/Erdos pool", 33468.079, 1428.805, 1, 43, "Open"],
        [5, "AZF/Goedel pool", 17881.414, 1257.845, 1, 29, "Open"],
        [6, "AZF/Lovelace pool", 83233.757, 2420.479, 1, 103, "Open"],
        [7, "AZF/Church pool", 5759.89, 560.398, 1, 23, "Open"],
        [8, "AZF/vonNeumann pool", 8730.424, 519.068, 1, 17, "Open"],
        [9, "AZF/Gauss pool", 4763.269, 521.146, 1, 15, "Open"],
        [10, "AZF/Kuratowski pool", 5241.706, 459.181, 1, 16, "Open"],
        [11, "AZF/Feynman pool", 16883.893, 1326.764, 1, 23, "Open"],
        [12, "Sekoya Labs 🚨 High Reward 🚨 Nomination Pool", 137135.67, 1896.528, 1, 101, "Open"],
        [13, "🚀 Low Fees 🚀 BEST Returns", 0, 0, 0, 1, "Destroyed"],
        [14, "Azero to the Moon 🚀", 0, 0, 0, 1, "Destroyed"],
        [15, "Stake Here | Low Fee, High Performance, Best Returns", 0, 0, 0, 1, "Destroyed"],
        [16, "MARMOSET CLUB - POOL", 0, 0.00000000041, 0, 1, "Destroying"],
        [17, "StakeSafe Pool", 36879.025, 1300.963, 1, 46, "Open"],
        [18, "💎 DIAMOND ATLAS | diamondatlas.io 💎", 244704.246, 7054.316, 1, 294, "Open"],
        [19, "VietStaking pool #01", 0, 0, 0, 1, "Destroyed"],
        [20, "ARTZERO POOL", 510493.749, 4719.275, 1, 215, "Open"],
        [21, "🟡 BLACKBOT www.MACRONODE.eu", 55579.654, 1748.658, 1, 61, "Open"],
        [22, "Stakingbridge | 🪐 Saturn Pool", 41202.844, 1134.54, 1, 34, "Open"],
        [23, "2SISTERS Pool 👧👩 twosisters.io", 47563.708, 1330.44, 1, 69, "Open"],
        [24, "AnubisStaking.com", 48489.961, 591.423, 1, 19, "Open"],
        [25, "Nobu Nodes/Pool", 3064.59, 211.111, 1, 5, "Open"],
        [26, "Indonesia First Pool", 2612.809, 310.371, 0, 12, "Open"],
        [27, "ZapFi Pool ⚡ Lowest Commission ⚡", 69032.711, 1501.648, 1, 82, "Open"],
        [28, "Brightlystake.com's pool", 7204.915, 714.444, 1, 8, "Open"],
        [29, "GURU | Pool party 🏖️", 13113.823, 102.401, 1, 8, "Open"],
        [30, "Piconbello Staking Pool", 16874.289, 700.025, 1, 22, "Open"],
        [31, "Ubik Capital Pool", 244992.493, 39959.868, 1, 26, "Open"],
        [32, "P-OPS Team Pool", 14193.167, 1183.197, 1, 23, "Open"],
        [33, "🐟Tuna Pool🐟 -> top reliability & lowest fees", 4473.347, 143.005, 1, 4, "Open"],
        [34, "POOL-ROCKET 🚀", 5230.603, 103.307, 1, 6, "Open"],
        [35, "ZTARZ UNSINGULARITY", 2529.978, 11.18, 1, 3, "Open"],
        [36, "Mile Pool Reliable validators", 6657.816, 182.461, 1, 2, "Open"],
        [37, "High Availability Pool", 2020, 0, 0, 3, "Open"],
        [38, "GoAzero pool", 15310.95, 437.175, 1, 17, "Open"],
        [39, "ALEPHKRATOS®️🌐 | Staking Pool ✔", 18190.096, 173.135, 1, 12, "Open"],
        [40, "Alex Dupre Pool", 0, 0.000000000009, 0, 1, "Destroying"],
        [41, "CANTOR pool", 56787.193, 1383.938, 1, 61, "Open"],
        [42, "BugsBunny", 0, 0, 0, 1, "Destroyed"],
        [43, "🧲 MagnetDAO.io | OG AZERO Fam🤍", 2000, 0, 0, 1, "Open"],
        [44, "FreeiaTech | 🇵🇱 home of A0!", 0, 0, 0, 1, "Destroyed"],
        [45, "🛸 ZPool 🛸 Monthly Giveaway", 0, 0, 0, 1, "Destroyed"],
        [46, "ZNodeTeam💚LowFees High Reward🚀", 0, 0, 0, 1, "Destroyed"],
        [47, "🪬 Talisman Pool 1 | Auto-Compound > $2USD 🪬", 463968.4, 3424.059, 1, 342, "Open"],
        [48, "SWISS POOL 🇨🇭 [Lowest fees]", 91841.668, 465.755, 1, 34, "Open"],
        [49, "🌀  Hermes Stakepool Germany 🌀", 0, 0, 0, 1, "Destroyed"],
        [50, "CANADAZERO", 30942.293, 248.426, 1, 13, "Open"],
        [51, "ALEPH ZERO ITALIA | Lowest fees", 26420.034, 305.586, 1, 25, "Open"],
        [52, "🔥 FIRSTBLOCK | firstblock.io 🔥", 72203.985, 358.43, 1, 26, "Open"],
        [53, "Kryptstar Staking Pool", 82680.743, 3624.878, 1, 105, "Open"],
        [54, "Azerians Validator Pool", 46276.939, 2087.404, 1, 59, "Open"],
        [55, "AZERO.ID POOL", 272260.906, 7644.519, 1, 424, "Open"],
        [56, "Wolfgang Amadeus Mozart", 13535.155, 189.077, 1, 13, "Open"],
        [57, "32venture", 5122, 594.468, 1, 4, "Open"],
        [58, "LIONmountain", 2615, 19.457, 1, 2, "Open"],
        [59, "Chocolate", 0, 0, 0, 1, "Destroyed"],
        [60, "We the Best!", 2230.104, 83.407, 1, 2, "Open"],
        [61, "btn.group", 0, 0, 0, 1, "Destroyed"],
        [62, "Chocolate", 17941.302, 932.686, 1, 24, "Open"],
        [63, "Fair Node Pool", 2000, 6.579, 1, 1, "Open"],
        [64, "", 0, 0, 0, 1, "Destroyed"],
        [65, "Alpha Zero 🐺 | アケロ", 0, 0, 0, 1, "Destroyed"],
        [66, "SBG Pool", 7634.325, 490.673, 1, 10, "Open"],
        [67, "Honest & free", 0, 0, 0, 1, "Destroyed"],
        [68, "gatenox-pk", 6518, 0, 0, 2, "Open"],
        [69, "SwissTech", 0, 0, 0, 1, "Destroyed"],
        [70, "BLOCK54CAPITAL-POOL", 11044.63, 544.571, 1, 34, "Open"],
        [71, "JHD - StackingPool", 3078.713, 23.642, 1, 2, "Open"],
        [72, "Degens' Den", 3209, 303.266, 1, 2, "Open"],
        [73, "Baron_A0 Pool", 2020, 71.717, 1, 2, "Open"],
        [74, "Nova Wallet Pool #1 novawallet.io", 2642955.267, 35559.373, 1, 1840, "Open"],
        [75, "nightly.app", 65186.818, 923.718, 1, 71, "Open"],
        [76, "DRAGONVN", 2014.898, 180.853, 1, 2, "Open"],
        [77, "Coverlet | Lowest fees", 0, 0.587, 0, 1, "Destroying"],
        [78, "HOYO/Acheron Pool 5%", 2030.175, 135.823, 1, 1, "Open"],
        [79, "azero", 2010, 154.187, 1, 2, "Open"],
        [80, "FFL/Rydia Pool 5%", 2162.479, 144.77, 1, 3, "Open"],
        [81, "Kintsu OG Pool", 4277.405, 200.66, 1, 15, "Open"],
        [82, "SubWallet Official", 805632.765, 8287.47, 1, 318, "Open"],
        [83, "Aleph Zero Cow Pool", 2000, 0, 0, 1, "Open"],
        [84, "Abax Finance Pool", 37288.274, 562.849, 1, 149, "Open"],
        [85, "Come and get some stake ;)", 4067, 219.399, 1, 2, "Open"],
        [86, "Weazero", 2943.784, 60.086, 1, 1, "Open"],
        [87, "IZICHANGE World Pool", 0, 0, 0, 1, "Destroyed"],
        [88, "⭐⭐⭐ BABY NODA ⭐⭐⭐", 4854.004, 65.094, 1, 7, "Open"],
        [89, "Burmese Spring", 0, 0, 0, 1, "Destroyed"],
        [90, "StakeNEST Pool | stakenest.io 🪹", 2068.899, 3.598, 1, 4, "Open"],
        [91, "Weazero2", 2051, 41.857, 1, 1, "Open"],
        [92, "AZERO LAB", 0, 0, 0, 1, "Destroyed"],
        [93, "AZERO VIETNAM POOL", 0, 0, 0, 1, "Destroyed"],
        [94, "Kvabitat", 2237.668, 8.032, 0, 1, "Open"],
        [95, "FASTSYSTEM LAB", 2004, 16.81, 1, 1, "Open"],
        [96, "Ashraf Pool", 2148, 9.635, 1, 2, "Open"]
    ]

    # Write to CSV file
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow(["Pool ID", "Name", "Total Bonded (AZERO)", "Reward Pool (AZERO)", "Nominated", "Members", "Status"])
        
        # Write data rows
        for row in data:
            writer.writerow(row)

    print(f"Data has been saved to {filename}")

# Run the function to save the data
save_pool_data_to_csv()