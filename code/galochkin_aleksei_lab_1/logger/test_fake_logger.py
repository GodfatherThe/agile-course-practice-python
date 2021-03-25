import unittest

from galochkin_aleksei_lab_1.logger.fake_logger import FakeLogger as Logger


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, Logger))

    def test_by_default_log_is_empty(self):
        log = self.logger.get_messages()

        self.assertEqual(log, [])

    def test_after_logging_message_in_log(self):
        self.logger.log('test message 1')

        self.assertEqual(['test message 1'], self.logger.get_messages())

    def test_can_log_several_messages(self):
        self.logger.log('test message 1')
        self.logger.log('test message 2')

        self.assertEqual(['test message 1', 'test message 2'], self.logger.get_messages())

    def test_can_get_last_log(self):
        self.logger.log('test message 1')
        self.logger.log('test message 2')

        self.assertEqual('test message 2', self.logger.get_last_message())
