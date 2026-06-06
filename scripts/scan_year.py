#!/usr/bin/env python3
"""
Reverse-lookup: find solar date(s) matching known 八字 four pillars.
Usage: python3 scan_year.py <year> <gender> [--year-pillar XX] [--month-pillar XX] [--day-pillar XX] [--hour-pillar XX] [--hour HH:MM]

Examples:
  # Full match (all four pillars)
  python3 scan_year.py 1996 0 --year-pillar 丙子 --month-pillar 辛卯 --day-pillar 甲寅 --hour-pillar 壬申

  # Partial match (just year + month + day, any hour)
  python3 scan_year.py 1996 0 --year-pillar 丙子 --month-pillar 辛卯 --day-pillar 甲寅

  # Scan multiple years
  for y in 1936 1996; do python3 scan_year.py $y 0 --day-pillar 甲寅; done
"""
import argparse
import subprocess
import sys
import datetime
import os

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD_SCRIPT = os.path.join(SKILL_DIR, "scripts", "buildBaziFromSolar.ts")


def scan_year(year: int, gender: int, hour_str: str = "15:30:00",
              year_pillar=None, month_pillar=None, day_pillar=None, hour_pillar=None):
    results = []
    start = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    d = start
    while d <= end:
        dt_str = d.strftime(f"%Y-%m-%dT{hour_str}")
        try:
            r = subprocess.run(
                ["node", BUILD_SCRIPT, dt_str, str(gender), "2"],
                capture_output=True, text=True, timeout=15, cwd=SKILL_DIR
            )
            for line in r.stdout.split("\n"):
                if "八字：" in line:
                    bz = line.split("八字：")[1].strip()
                    parts = bz.split()
                    if len(parts) < 4:
                        continue
                    match = True
                    if year_pillar and parts[0] != year_pillar:
                        match = False
                    if month_pillar and parts[1] != month_pillar:
                        match = False
                    if day_pillar and parts[2] != day_pillar:
                        match = False
                    if hour_pillar and parts[3] != hour_pillar:
                        match = False
                    if match:
                        results.append((d.isoformat(), bz))
                        print(f"MATCH: {d.isoformat()} -> {bz}")
        except Exception as e:
            pass  # skip invalid dates
        d += datetime.timedelta(days=1)
    return results


def main():
    parser = argparse.ArgumentParser(description="Scan a year for bazi matches")
    parser.add_argument("year", type=int, help="Year to scan")
    parser.add_argument("gender", type=int, choices=[0, 1], help="0=female, 1=male")
    parser.add_argument("--year-pillar", default=None, help="年柱 to match")
    parser.add_argument("--month-pillar", default=None, help="月柱 to match")
    parser.add_argument("--day-pillar", default=None, help="日柱 to match")
    parser.add_argument("--hour-pillar", default=None, help="时柱 to match")
    parser.add_argument("--hour", default="15:30:00", help="Time to use (default: 15:30:00 for 申时)")
    args = parser.parse_args()

    print(f"Scanning {args.year} for gender={args.gender}, hour={args.hour}...")
    print(f"Filters: year={args.year_pillar} month={args.month_pillar} day={args.day_pillar} hour={args.hour_pillar}")
    print()

    results = scan_year(
        args.year, args.gender, args.hour,
        args.year_pillar, args.month_pillar, args.day_pillar, args.hour_pillar
    )

    print(f"\n{'='*50}")
    print(f"Found {len(results)} match(es) in {args.year}")
    if not results:
        print("No matches found. Try scanning adjacent years or different hour.")


if __name__ == "__main__":
    main()
