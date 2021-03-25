from bisymmetric_matrix.model.bisymmetric import BisymmetricMatrix
from bisymmetric_matrix.logger.reallogger import RealLogger


def is_correct_vector_size(size):
    k = 1
    while k ** 2 <= size:
        if size == k * k:
            return 2 * k - 1
        if size == k * (k + 1):
            return 2 * k
        k += 1
    return -1


class BisymmetricMatrixViewModel:
    def __init__(self,
                 logger=RealLogger()):
        self.logger = logger
        self.logger.log('Welcome')

        self.button_convert_state = 'disabled'

        self.vector = []
        self.created_matrix_by_vector = []
        self.str_matrix_by_vector = ""

        self.matrix_size = 0
        self.created_random_matrix = []
        self.str_random_matrix = ""

    def get_button_convert_state(self):
        return self.button_convert_state

    def set_button_enabled(self):
        self.button_convert_state = 'normal'

    def set_button_disabled(self):
        self.button_convert_state = 'disabled'

    def set_created_random_matrix(self, matrix):
        self.created_random_matrix = matrix
        self.logger.log('result_random_matrix: \n' + self.convert_matrix_to_str(self.created_random_matrix))

    def set_created_matrix_by_vector(self, matrix):
        self.created_matrix_by_vector = matrix
        self.logger.log('result_matrix_by_vector: \n'
                        + self.convert_matrix_to_str(self.created_matrix_by_vector))

    def get_str_created_random_matrix(self):
        return self.convert_random_matrix_to_str(self.created_random_matrix)

    def get_str_created_matrix_by_vector(self):
        return self.convert_matrix_by_vector_to_str(self.created_matrix_by_vector)

    def set_vector(self, input_vector):
        self.logger.log('trying to set vector')
        if input_vector == '':
            self.set_button_disabled()
            self.logger.log('vector empty')
        elif not input_vector.isdigit():
            self.set_button_disabled()
            self.logger.log('vector is not correct')
        elif is_correct_vector_size(len(input_vector)) == -1:
            self.set_button_disabled()
            self.logger.log('vector size is not correct')
        else:
            self.vector = self.convert_str_to_vector(input_vector)
            self.set_button_enabled()
            self.logger.log('vector set: ' + input_vector)

    def get_input_vector(self):
        return self.vector

    def set_matrix_size(self, size):
        self.logger.log('trying to set the matrix size')
        if size == '':
            self.set_button_disabled()
            self.logger.log('matrix size empty')
        elif not size.isdigit():
            self.set_button_disabled()
            self.logger.log('matrix size is not correct')
        else:
            self.matrix_size = int(size)
            self.logger.log('matrix size is set: %s' % self.matrix_size)
            self.set_button_enabled()

    def create_random_matrix(self):
        self.logger.log('Button create_random_matrix clicked')
        self.created_random_matrix.clear()
        if self.button_convert_state == 'normal':
            matrix = BisymmetricMatrix()
            self.set_created_random_matrix(
                matrix.generate_random_bisymmetric_matrix(self.matrix_size))

    def convert_random_matrix_to_str(self, matrix: list):
        if self.matrix_size != 0:
            self.str_random_matrix = ''
            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    self.str_random_matrix += ' ' + str(matrix[i][j])
                self.str_random_matrix += '\n'
        return self.str_random_matrix

    def create_matrix_by_vector(self):
        self.logger.log('Button create_matrix_by_vector clicked')
        self.created_matrix_by_vector.clear()
        if self.button_convert_state == 'normal':
            matrix = BisymmetricMatrix()
            self.matrix_size = is_correct_vector_size(len(self.vector))
            self.set_created_matrix_by_vector(
                matrix.generate_bisymmetric_matrix_by_vector(self.vector))

    def convert_matrix_by_vector_to_str(self, matrix: list):
        if self.matrix_size != 0:
            self.str_matrix_by_vector = ''
            for i in range(self.matrix_size):
                for j in range(self.matrix_size):
                    self.str_matrix_by_vector += ' ' + str(matrix[i][j])
                self.str_matrix_by_vector += '\n'
        return self.str_matrix_by_vector

    def convert_str_to_vector(self, input_str_vector: list):
        self.vector.clear()
        for symb in input_str_vector:
            try:
                self.vector.append(int(symb))
            finally:
                pass
        return self.vector

    def convert_matrix_to_str(self, matrix: list):
        str_matrix_log = ''
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                str_matrix_log += ' ' + str(matrix[i][j])
            str_matrix_log += '\n'
        return str_matrix_log
