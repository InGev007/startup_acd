class Matrix:
    def __init__(self, m_list):
        self.__ismatrix(m_list)
        self.matrix = m_list
        
        
    def __str__(self):
        rows_string = ""
        for row in self.matrix:
            rows_string += f"{row}\n"
        return rows_string
    
    
    def __len__(self):
        return len(self.matrix)
    
    
    def __getitem__(self,key):
        return self.matrix[key]

    
    def __ismatrix(self, m_list):
        for i in range(len(m_list)-1):
            if len(m_list[i]) != len(m_list[i+1]):
                raise Exception (f"Не могу создать матрицу из данного списка")
        return True

    
    def transpose(self):
        transpose_matrix = [[0] * len(self.matrix) for _ in range(len(self.matrix[0]))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                transpose_matrix[j][i] = self.matrix[i][j]
        self.matrix = transpose_matrix
        return self
    
    
    def __add__(self, data):
      temp_matrix=self.__null_matrix(max(len(self.matrix),len(data)), max(len(self.matrix[0]),len(data[0])))
      temp_matrix=self.__add_matrix(temp_matrix, self.matrix)
      temp_matrix=self.__add_matrix(temp_matrix, data)
      return Matrix(temp_matrix)


    def __sub__(self, data):
      temp_matrix=self.__null_matrix(max(len(self.matrix),len(data)), max(len(self.matrix[0]),len(data[0])))
      temp_matrix=self.__add_matrix(temp_matrix, self.matrix)
      temp_matrix=self.__sub_matrix(temp_matrix, data)
      return Matrix(temp_matrix)


    def __mul__(self, other):
      if isinstance(other,int) or isinstance(other, float):
        return Matrix(self.__mul_of_number(other))
      elif isinstance(other, Matrix) or isinstance(other, list):
        if isinstance(other, list):
          self.__ismatrix(other)
        self_j_len=len(self.matrix[0])
        other_i_len=len(other)
        if self_j_len == other_i_len:
            temp_matrix = self.__null_matrix(len(self.matrix), len(other[0]))
            for i in range(len(self.matrix)):
              for j in range(len(other[i])):
                for k in range(len(other)):
                    temp_matrix[i][j] += self.matrix[i][k] * other[k][j]
            return Matrix(temp_matrix)
        else:
          raise Exception("Данные матрицы невозможно умножить")
      else:
        raise Exception("Аргумент не является числом или матрицей")
        
        
    def  __mul_of_number(self, other):
      temp_matrix=self.__null_matrix(len(self.matrix), len(self.matrix[0]))
      for row in range(len(self.matrix)):
        for column in range(len(self.matrix[row])):
          temp_matrix[row][column] = self.matrix[row][column] * other
      return temp_matrix

      
    def __sub_matrix(self, matrix1, matrix2):
      for row in range(len(matrix2)):
        for column in range(len(matrix2[row])):
          matrix1[row][column] = matrix1[row][column] - matrix2[row][column]
      return matrix1

  
    def __add_matrix(self, matrix1, matrix2):
      for row in range(len(matrix2)):
        for column in range(len(matrix2[row])):
          matrix1[row][column] = matrix1[row][column] + matrix2[row][column]
      return matrix1

      
    def __null_matrix(self, row, column):
        temp_matrix=[]
        for i in range(row):
            temp_matrix.append([])
            for j in range(column):
                temp_matrix[i].append(0)
        return temp_matrix



matrix_b = Matrix([[8, 3, 7, 1], [6, 5, 4, 1], [6, 5, 4, 1]])
matrix_a = Matrix([[12, 7, 3], [4, 5, 6]])

matrix_c = [[12, 7, 3], [4, 5, 6], [4, 5, 6]]
print(matrix_b)
print("")
print(matrix_b.transpose())
matrix_b.transpose()
print("")
print(matrix_a+matrix_b)

print("")
print(matrix_a-matrix_b)

print("")
print(matrix_a*1.2)

print("")
print(matrix_a*matrix_b)

      