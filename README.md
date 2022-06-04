# RLB-Lottery-Tools
Useful tools for the RLB Lottery on Rollbit.com.
Requires chromedriver and selenium.

scrape_lottery.py will grab all entries in the current lottery and export to .json file. This will open an instance of chrome, and automatically close it on data retrieval. 

run_lottery.py imports lottery entries and runs the lottery with the given information. This code mostly taken from https://rollbit.com/rlb/lottery/provably-fair with some modifications. RESULTS UNVERIFIED! HIGHLY RECOMMENDED TO NOT USE AT THIS TIME!

loterry_entries.json is directly pulled from https://rollbit.com/rlb/lottery/provably-fair. Note that this file will always be outdated as soon as entries are made after the data is retrieved. It is recommended to use scrape_lottery.py to get the most up-to-date information.

Not financial advice, use at your own risk.