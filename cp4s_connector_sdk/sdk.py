#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright Ryan Gordon. 2021. All Rights Reserved. MIT

""" TODO: module docstring """

import sys
import logging
from cp4s_connector_sdk.cmds.codegen_connector import ConnectorCodegenCmd
from resilient_sdk.util import sdk_helpers
from resilient_sdk.util.sdk_exception import SDKException
from resilient_sdk.util.sdk_argparse import SDKArgumentParser

# Setup logging
LOG = logging.getLogger("cp4s_connector_sdk_log")
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def get_main_app_parser():
    """
    Creates the main 'entry point' parser for cp4s-connector-sdk.

    :return: Main App Parser
    :rtype: argparse.ArgumentParser
    """
    # Define main parser object
    # We use SDKArgumentParser which overwrites the 'error' method
    parser = SDKArgumentParser(
        prog="connector-sdk",
        description="Python SDK for developing CP4S Connectors",
        epilog="For support, please visit ibm.biz/soarcommunity")

    parser.usage = """
    $ connector-sdk <subcommand> ...
    $ connector-sdk -v <subcommand> ...
    $ connector-sdk -h
    """

    # Add --verbose argument
    parser.add_argument("-v", "--verbose",
                        help="Set the log level to DEBUG",
                        action="store_true")

    return parser


def get_main_app_sub_parser(parent_parser):
    """
    Creates and adds a sub_parser to parent_parser.
    Returns the sub_parser

    :param parent_parser: Parser to add the sub_parser to
    :type parent_parser: argparse.ArgumentParser
    :return: Sub Parser
    :rtype: argparse.ArgumentParser
    """
    # Define sub_parser object, its dest is cmd
    sub_parser = parent_parser.add_subparsers(
        title="subcommands",
        description="one of these subcommands must be provided",
        metavar="",
        dest="cmd"
    )

    return sub_parser


def main():
    """
    Main entry point for cp4s-connector-sdk
    """

    # Get main parser object
    parser = get_main_app_parser()

    # Get sub_parser object, its dest is cmd
    sub_parser = get_main_app_sub_parser(parser)

    # Add any subcommands to main app parser here
    cmd_codegen = ConnectorCodegenCmd(sub_parser)

    try:
        # Parse the arguments
        args = parser.parse_args()

        if args.cmd is None:
            parser.print_help()
            sys.exit()

    except SDKException as err:
        # Get main_cmd (codegen, docgen etc.)
        main_cmd = sdk_helpers.get_main_cmd()

        LOG.error(err)
        LOG.info("\n-----------------\n")

        # Print specifc usage for that cmd for these errors
        if "too few arguments" in err.message or "no subcommand provided" in err.message:
            if main_cmd == cmd_codegen.CMD_NAME:
                cmd_codegen.parser.print_usage()
            else:
                parser.print_help()

        # Exit
        sys.exit()

    # If -v was specified, set the log level to DEBUG
    if args.verbose:
        LOG.setLevel(logging.DEBUG)
        LOG.debug("Logging set to DEBUG mode")

    if args.cmd == cmd_codegen.CMD_NAME:
        cmd_codegen.execute_command(args)


if __name__ == "__main__":
    main()
