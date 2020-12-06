import unittest

from dijkstra_algorithm.viewmodel.dijkstra_algorithm_viewmodel import DAViewModel


class TestDAViewModel(unittest.TestCase):

    def test_by_default_button_create_graph_disable(self):
        model = DAViewModel()
        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_when_enter_correct_number_button_create_graph_enabled(self):
        model = DAViewModel()
        model.set_num_vertex('5')
        self.assertEqual('normal', model.get_btn_create_graph_state())

    def test_when_clear_number_button_create_graph_disabled(self):
        model = DAViewModel()
        model.set_num_vertex(None)

        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_when_enter_less_zero_number_button_create_graph_disabled(self):
        model = DAViewModel()
        model.set_num_vertex('-1')

        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_when_enter_un_correct_number_button_create_graph_keeps_disabled(self):
        model = DAViewModel()
        model.set_num_vertex('some un correct input')
        self.assertEqual('disabled', model.get_btn_create_graph_state())

    def test_can_get_vertex_number(self):
        model = DAViewModel()
        model.set_num_vertex('5')
        self.assertEqual('5', model.get_num_vertex())