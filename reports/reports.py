from reports.payout import PayoutReport


class Reports:
    def __init__(self):
        self.available_reports = {
            "payout": PayoutReport,
            # другие отчеты
        }

    def get_report(self, report_name):
        report_cls = self.available_reports.get(report_name)
        if not report_cls:
            raise ValueError(f"Unknown report: {report_name}")
        return report_cls()
