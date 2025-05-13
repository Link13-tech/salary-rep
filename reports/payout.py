from typing import List, Dict


class PayoutReport:
    def generate(self, records: List[Dict]) -> str:
        lines = ["Отчёт по зарплатам:"]
        for r in records:
            payout = r["hours_worked"] * r["hourly_rate"]
            lines.append(f"{r['name']} ({r['department']}): ${payout:.2f}")
        return "\n".join(lines)
