# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
from OTXv2 import OTXv2
import json

from intelmq.bots.collectors.http.lib import fetch_url
from intelmq.lib.bot import Bot
from intelmq.lib.message import Report


class AlienVaultOTXCollectorBot(Bot):

    def process(self):
        self.logger.info("Downloading report through API")
        otx = OTXv2(self.parameters.api_key)
        pulses = otx.getall()
        self.logger.info("Report downloaded.")

        report = Report()
        report.add("raw", json.dumps(pulses), sanitize=True)
        report.add("feed.name", self.parameters.feed, sanitize=True)
        self.send_message(report)


if __name__ == "__main__":
    bot = AlienVaultOTXCollectorBot(sys.argv[1])
    bot.start()
