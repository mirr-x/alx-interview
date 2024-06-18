#!/usr/bin/python3
"""
Log Parsing
"""

import sys
import re


class LogParser:
    """
        Class logPraser
    """

    def __init__(self):
        """
            init for auto created from a class
        """
        self.regex = re.compile(
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} '
            r'\d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" '
            r'(\d{3}) (\d+)'
        )
        self.line_count = 0
        self.log = {
            "file_size": 0,
            "code_frequency": {
                200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0
            }
        }

    def output_statistics(self):
        """
            output_statistics
        """
        print("File size:", self.log["file_size"])
        for code, count in sorted(self.log["code_frequency"].items()):
            if count:
                print(f"{code}: {count}")

    def parse_line(self, line):
        """
            parse_line
        """
        match = self.regex.fullmatch(line)
        if match:
            code = int(match.group(1))
            file_size = int(match.group(2))

            self.log["file_size"] += file_size

            if code in self.log["code_frequency"]:
                self.log["code_frequency"][code] += 1

            self.line_count += 1

    def parse_logs(self):
        """
            parse_line
        """
        try:
            for line in sys.stdin:
                line = line.strip()
                self.parse_line(line)
                if self.line_count % 10 == 0:
                    self.output_statistics()
        finally:
            self.output_statistics()


if __name__ == "__main__":
    parser = LogParser()
    parser.parse_logs()
