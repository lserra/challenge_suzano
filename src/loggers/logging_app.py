#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging
import logging.handlers


class LoggingApp:

    @staticmethod
    def logging_application_to_log_file(app_name, log_path, log_filename):
        # Logger initialization
        logger = logging.getLogger(app_name)
        logger.setLevel(logging.DEBUG)

        # Creating file log handler and set level to debug
        ch = logging.FileHandler(log_path + log_filename, 'w+')
        ch.setLevel(logging.DEBUG)

        # Creating formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Adding formatter to ch
        ch.setFormatter(formatter)

        # Adding ch to logger
        logger.addHandler(ch)

        # Setting the Logger Level (INFO)
        logger.setLevel(logging.INFO)

        return logger

    @staticmethod
    def logging_application_to_console(app_name):
        # Logger initialization
        logger = logging.getLogger(app_name)
        logger.setLevel(logging.DEBUG)

        # Creating file log handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Creating formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Adding formatter to ch
        ch.setFormatter(formatter)

        # Adding ch to logger
        logger.addHandler(ch)

        # Setting the Logger Level (INFO)
        logger.setLevel(logging.INFO)

        return logger
