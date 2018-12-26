import os
import sys
import subprocess
from coverage import Coverage
from django.core.management.commands.test import Command as TestCommand


class Command(TestCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--coverage", action="store_true", help="Enable coverage collection"
        )
        parser.add_argument(
            "--xml", action="store_true", help="Create XML coverage report"
        )
        parser.add_argument(
            "--html", action="store_true", help="Create HTML coverage report"
        )
        super().add_arguments(parser)

    def handle(self, *args, **options):
        # If --coverage is specified, fork a subprocess and exec:
        #    coverage run manage.py test ...
        # with an env variable set to prevent infinite recursion/forking.
        # Else let parent class handle test command normally.

        if options["coverage"] and not os.environ.get("RUNNING_COVERAGE_SUBPROCESS"):
            self.handle_with_coverage(xml=options["xml"], html=options["html"])
        else:
            super().handle(*args, **options)

    def handle_with_coverage(self, xml=False, html=False):
        coverage = Coverage()
        coverage.erase()

        # Create the coverage command to fork and exec
        cmd = ["coverage", "run"]
        cmd.extend(sys.argv)

        os.environ["RUNNING_COVERAGE_SUBPROCESS"] = "true"
        returncode = subprocess.run(cmd).returncode
        del (os.environ["RUNNING_COVERAGE_SUBPROCESS"])

        if returncode == 0:
            coverage.combine()
            coverage.load()
            print("\n")
            coverage.report()
            if html:
                coverage.html_report()
            if xml:
                coverage.xml_report()
            coverage.erase()
        else:
            coverage.erase()
            sys.exit(returncode)
