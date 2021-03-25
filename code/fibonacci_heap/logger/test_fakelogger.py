import unittest

from fibonacci_heap.logger.fakelogger import FakeLogger as Logger


def test_log_msg(msg_index: int) -> str:
    """
    Get the test log msg and insert its number by order
    :param msg_index: the id of test message
    :return: the message
    """
    return 'This is the [{}] test log msg'.format(msg_index)


class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()

    def test_can_create_logger(self):
        self.assertTrue(isinstance(self.logger, Logger))

    def test_by_default_log_is_empty(self):
        log = self.logger.get_log_messages()

        self.assertEqual(log, [])

    def test_after_logging_message_in_log(self):
        self.logger.log(test_log_msg(msg_index=1))

        self.assertEqual([test_log_msg(msg_index=1)], self.logger.get_log_messages())

    def test_can_log_several_messages(self):
        self.logger.log(test_log_msg(msg_index=1))
        self.logger.log(test_log_msg(msg_index=2))

        self.assertEqual([test_log_msg(msg_index=1), test_log_msg(msg_index=2)],
                         self.logger.get_log_messages())

    def test_can_get_last_log(self):
        self.logger.log(test_log_msg(msg_index=1))
        self.logger.log(test_log_msg(msg_index=2))

        self.assertEqual(test_log_msg(msg_index=2), self.logger.get_last_message())
