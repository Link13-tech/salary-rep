from typing import List, Dict
from collections import defaultdict


class PayoutReport:
    def generate(self, records: List[Dict]) -> str:
        departments = defaultdict(list)
        for r in records:
            payout = r["hours_worked"] * r["hourly_rate"]
            departments[r["department"]].append({
                "name": r["name"],
                "hours": r["hours_worked"],
                "rate": r["hourly_rate"],
                "payout": payout
            })

        lines = ["\n" + " " * 14 + "name             hours   rate  payout"]
        for dept, people in departments.items():
            lines.append(f"{dept}")
            for person in people:
                lines.append(
                    f"{'-' * 12}  "
                    f"{person['name']:<15}"
                    f"{int(person['hours']):>5}  "
                    f"{int(person['rate']):>5}    "
                    f"${int(person['payout']):,}".replace(",", "")
                )
        return "\n".join(lines)
