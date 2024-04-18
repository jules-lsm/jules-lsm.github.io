#!/usr/bin/env python3

"""
Automate the steps required to deploy the jules documentation.
"""

# pylint: disable=useless-return


import os
import re
import logging
from argparse import ArgumentParser
from datetime import datetime
from fileinput import FileInput
from subprocess import run, Popen, STDOUT, PIPE, CalledProcessError



class JulesDocsRelease:
    """Class which deploys the jules docs."""

    def __init__(self, vnumber):
        self.vnumber = str(vnumber)
        self.changed = False
        return

    def update_config(self, target):
        """Update the sphinx configuration file."""

        year = str(datetime.now().year)

        cr_pattern = re.compile(r"\s*copyright\s*=\s*.(\d+).")
        vn_pattern = re.compile(r"\s*(release|version)\s*=\s*.([\d\.]+).")

        with FileInput(target, inplace=True) as fd:
            # An in-place update the copyright and version number in
            # the sphinx configuration file.

            for line in fd:
                if match := cr_pattern.match(line):
                    if match.group(1) != year:
                        line = f"copyright = '{year}'\n"
                        self.changed = True
                        logging.info("Updated sphinx copyright year")
                elif match := vn_pattern.match(line):
                    if match.group(2) != self.vnumber:
                        line = f"{match.group(1)} = '{self.vnumber}'\n"
                        self.changed = True
                        logging.info(
                            "Updated sphinx %s number to %s",
                            match.group(1),
                            self.vnumber,
                        )
                print(line, end="")

        return

    def update_index(self, target):
        """Update the index page with the new release."""

        # Check whether an update is required
        with FileInput(target) as fd:
            match = f'a href="vn{self.vnumber}"'
            found = False

            for line in fd:
                if match in line:
                    found = True
                    break

        if found:
            # Stop if version is already present
            return

        # Add the missing version link
        with FileInput(target, inplace=True) as fd:
            for line in fd:
                if 'href="latest/index.html"' in line:
                    line += " " * 16
                    line += (
                        f'<li><a href="vn{self.vnumber}">vn{self.vnumber}</a></li>\n'
                    )
                    self.changed = True
                    logging.info("Added reference to vn%s to index", self.vnumber)
                print(line, end="")

        return

    def mkdocs(self):
        """Run sphinx to build the HTML documentation."""

        dest = f"vn{self.vnumber}"

        if not os.path.exists(dest):
            # Build the sphinx documentation
            cmd = [
                "sphinx-build",
                "-qb",
                "html",
                "user_guide/doc/source",
                f"vn{self.vnumber}",
            ]
            run(cmd, check=True)
            logging.info("Successfully built the sphinx documentation")

        if os.path.exists(dest):
            # Check directory exists and create a symlink
            if os.path.islink("latest") and os.readlink("latest") != dest:
                os.unlink("latest")
            if not os.path.exists("latest"):
                os.symlink(dest, "latest")
                logging.info("Set latest link to %s", dest)

        return


def last_log_message(branch):
    """Get the log message of the last commit to trunk."""

    cmd = ["git", "log", "--pretty=format:message: %s", "--branches", branch, "-1"]

    with Popen(cmd, stdout=PIPE, stderr=STDOUT, encoding="utf-8") as proc:
        message = "unknown update"

        for line in proc.stdout:
            if line.startswith("message: "):
                message = line.split(": ", 1)[-1]
                break

    return message


def commit_changes(args):
    """Commit any new change to the trunk."""

    cmd = ["git", "add", "-A"]
    run(cmd, check=False)

    cmd = ["git", "diff", "--cached", "--quiet"]
    if run(cmd, check=False) == 0:
        logging.info("no changes need to be committed")

    message = last_log_message(args.trunk_name)
    message = f"Docs build for {message}"

    cmd = ["git", "commit", "--no-gpg-sign", "-a", "--quiet", "-m", message]

    if not args.no_commit:
        run(cmd, check=True)
        logging.info("Committed change %r", message)
        run(["git", "push"], check=True)
        logging.info("Pushed automatic commit")
    else:
        logging.info("Need to commit change for %r", message)

    return


def main():
    """Main function."""

    parser = ArgumentParser()
    parser.add_argument("--verbose", action="store_true", help="enable verbose output")
    parser.add_argument(
        "--trunk-name", type=str, default="master", help="name of trunk"
    )
    parser.add_argument(
        "--no-commit", action="store_true", help="do not commit the changes"
    )
    parser.add_argument("release", type=str, help="github release reference")
    args = parser.parse_args()

    match = re.match(r".*vn?([\.\d]+)-*\S*$", args.release)
    if match:
        vnumber = match.group(1)
    else:
        parser.error(f"unable to identify version number '{args.release}'")

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(message)s")

    release = JulesDocsRelease(vnumber)

    try:
        release.update_config("user_guide/doc/source/conf.py")
        release.mkdocs()
        release.update_index("index.html")
    except (FileNotFoundError, CalledProcessError)  as error:
        logging.error(str(error))
        raise SystemExit(1) from error

    if release.changed:
        # There are at least some updates to apply
        commit_changes(args)

    else:
        logging.info("No changes made")
        raise SystemExit(2)

    return


if __name__ == "__main__":
    main()
